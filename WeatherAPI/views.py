import calendar

import numpy as np
import requests
import logging

from django.core.cache import cache
from datetime import datetime as dt
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from WeatherApp import settings

logger = logging.getLogger(__name__)

# Create your views here.

fig: Figure
CITY_FORECAST_CACHE_PREFIX = "FORECAST_CACHE_PREFIX"
CITY_FORECAST_CACHE_DURATION = 3_600


class IndexWeatherView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.city = 'Moscow'

    def get(self, request):
        logger.debug("Index page rendered")
        return render(request, "index.html", context=get_weather_data(self.city))


def graph_view(request):
    global fig

    # Save the figure as an image
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)

    return response


def create_graph(time, temp_data, humidity_data, wind_data, text_data, precip_data) -> Figure:
    fig, ax = plt.subplots(figsize=(20, 4))

    hours = map(lambda i: i.strftime('%I%p').lower(), time)
    time = [i.hour for i in time]
    xticks = range(time[0], time[0] + 24)

    x = np.linspace(xticks[0], xticks[-1], 100)
    poly_coeffs = np.polyfit(xticks, temp_data, 12)
    y = np.polyval(poly_coeffs, x)

    labels = [f"{t}\n" + "\n".join(text_data[i].split()) + f"\n{wind_data[i]}m/s" for i, t in enumerate(hours)]

    # Plot data
    ax.plot(x, y, label="Temperature", color="#f2a28c")
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)

    yticks_labels = ax.get_yticklabels()
    ax.set_yticklabels([yticks_label.get_text() + "°C" for yticks_label in yticks_labels])

    ax2 = ax.twinx()
    ax2.set_ylim(0, max(precip_data) + 1 if max(precip_data) else 1)

    bars = ax2.bar(xticks, precip_data, alpha=0.5, width=0.7, color='lightgray', label='Humidity')
    font = {
        'size': 8,
        'ha': 'left',
        'va': 'center',
        'color': 'gray'
    }
    for i, bar in enumerate(bars):
        string = f"{precip_data[i]}mm/h".center(8) if precip_data[i] else ""
        string += "\n" + f"{humidity_data[i]}%".center(13)
        ax2.text(
            bar.get_x(), bar.get_height() + 0.2,
            string,
            fontdict=font
        )

    ax2.set_xlabel('Humidity')

    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.subplots_adjust(left=0.06, right=0.97, bottom=0.3, top=0.94)
    return fig


def search_city(request):
    city = "London"

    if request.GET['city-name']:
        city = request.GET['city-name']
    logger.debug("Requested weather info for %s city" % city)
    context = get_weather_data(city)
    if 'error' in context:
        messages.warning(request, _(context['error']['message']))
        return redirect('index')
    return render(request, 'index.html', context=context)


def get_weather_data(city_name: str) -> dict:
    global fig

    cache_key = get_city_forecast_cache_key(city_name)
    cached_forecast = cache.get(key=cache_key)

    if not cached_forecast:

        url = f'https://api.weatherapi.com/v1/forecast.json?key={settings.WEATHER_API_CODE}' \
              f'&q={city_name}&days=7&aqi=no&alerts=no'
        r = requests.get(url).json()

        if 'error' in r:
            return r
        forecast = r['forecast']

        hours = [i for i in r['forecast']['forecastday'][0]['hour'][dt.now().hour:]]
        if len(hours) < 24:
            hours += r['forecast']['forecastday'][1]['hour'][:24 - len(hours)]

        time, temp_data, humidity_data, wind_data, text_data, precip_data = [], [], [], [], [], []
        for hour in hours:
            time.append(dt.strptime(hour['time'], "%Y-%m-%d %H:%M").time())
            temp_data.append(hour['temp_c'])
            humidity_data.append(hour['humidity'])
            wind_data.append(hour['wind_kph'])
            text_data.append(hour['condition']['text'])
            precip_data.append(hour['precip_mm'])

        fig = create_graph(time, temp_data, humidity_data, wind_data, text_data, precip_data)
        city_weather = {
                'city': city_name,
                'location': r['location'],
                'current': r['current'],
                'wind': round(r['current']['wind_kph'] / 3.6, 1),
                'forecastday': [
                    {
                        "day_name": calendar.day_name[
                                        dt.strptime(day['date'], "%Y-%m-%d").date().weekday()
                                    ][:3],
                        'wind': round(day['hour'][12]['wind_kph'] / 3.6, 1),
                        'loc_t': dt.strptime(day['date'], "%Y-%m-%d").date(),
                        'day': day['day'],
                        'astro': day['astro'],
                        'morning': day['hour'][6],
                        'afternoon': day['hour'][12],
                        'evening': day['hour'][18],
                        'night': day['hour'][23],
                    }
                    for day in forecast['forecastday']
                ]
            }
        val = {
            "fig": fig,
            "cw": city_weather,
        }
        cache.set(
            key=cache_key,
            value=val,
            timeout=CITY_FORECAST_CACHE_DURATION
        )
        logger.debug("Set cache forecast for city: %s" % city_name)
    else:
        city_weather = cached_forecast['cw']
        logger.debug("Return forecast data from cache for city %s" % city_name)
    context = {"cw": city_weather}
    return context


def get_city_forecast_cache_key(city: str) -> str:
    return f"{CITY_FORECAST_CACHE_PREFIX}_{city.upper()}"


def invalidate_forecast_cache(cache_key: str) -> None:
    cache.delete(key=cache_key)
    logger.debug("Invalidate cache with key: %s" % cache_key)
