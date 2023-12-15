# Django Weather App

Django Weather App is a web application that provides a 7-day and hourly forecast for any city or country. It utilizes the [WeatherAPI](https://www.weatherapi.com/) to retrieve weather data and presents it in a user-friendly interface.

## Features

- Get the current weather conditions for any location
- View a 7-day forecast for a specific city or country
- Display an hourly forecast for the next 24 hours
- Responsive design for optimal user experience on different devices
- Delegating the return of static and media files to Nginx

## Requirements

- Python 3.x
- Django 4.x
- WeatherAPI key (sign up at https://www.weatherapi.com/ to obtain a free API key)

## Installation:
Clone repos
```bash 
git clone https://github.com/ai-fn/django-weather.git
```
Go to workdir `cd django-weather`

Install via pip: `pip install -r req.txt`

### Configuration
Most configurations are in `setting.py`, others are in backend configurations.

I set many `setting` configuration with my environment variables (such as: `SECRET_KEY`, `DEBUG` and some email configuration parts.) and they did NOT been submitted to the `GitHub`. You can change these in the code with your own configuration or just add them into your environment variables.

In this project utilizes Bing Map API for display searched place, so in order to make it work, you need to get your own API Key on [bingmapsportal](https://www.bingmapsportal.com/) and replace `'Your API KEY'` in WeatherAPI/templates/index.html at 'loadMap' function.

## Docker Compose

Alternatively, you can use Docker Compose to run the application in a containerized environment:

1. Make sure you have Docker and Docker Compose installed on your machine.

2. Navigate to the project directory:
```bash
cd django-weather
```

4. Build and run the Docker containers:
```bash
docker-compose up -d --build
```

## Run

Modify `WeatherApp/setting.py` with database settings, as following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'weatherDB',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 5432,
    }
}
```

### Create database
Run the following command in PostgreSQL shell:
```sql
craetedb `weatherDB`;
```

Run the following commands in Terminal:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
```  

### Create super user

Run command in terminal and follow the steps in bash:
```bash
python manage.py createsuperuser
```

### Collect static files
Run command in terminal:
```bash
python manage.py collectstatic --noinput
```

### Getting start to run server

```python
python manage.py runserver
```
Open up a browser and visit: http://127.0.0.1:8000/ (http://127.0.0.1:80/ for nginx), then you will see the chat.

## Usage

1. Enter a city or country name in the search bar on the home page.
2. Click the "Search" button or press Enter to retrieve the weather information.
3. View the current weather conditions, 7-day forecast, and hourly forecast on the result page.
4. Change metric by move slider to imperial or metric as you need
5. Explore different locations by performing new searches.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

Enjoy the weather app!
