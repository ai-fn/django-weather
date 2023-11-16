# import datetime
#
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.axes import Axes
# from matplotlib.figure import Figure
#
# time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# temp_data = [4.3, 4.1, 3.9, 3.8, 3.7, 3.6, 3.5, 3.5, 3.9, 4.4, 5.0, 5.5, 6.0, 6.2, 6.1, 5.7, 7.0, 4.8, 4.5, 4.0, 4.0, 3.9, 3.9, 3.8]
# humidity_data = [82, 82, 82, 82, 82, 84, 86, 85, 84, 81, 78, 76, 73, 71, 70, 72, 76, 77, 79, 81, 82, 83, 83, 83]
# wind_data = [14.0, 14.4, 14.8, 14.4, 14.4, 14.0, 13.3, 13.7, 14.0, 14.4, 14.4, 14.8, 14.8, 14.4, 14.8, 14.8, 11.2, 13.7, 14.0, 14.0, 14.4, 14.0, 15.1, 15.8]
# text_data = ['Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Partly cloudy', 'Partly cloudy', 'Partly cloudy', 'Cloudy', 'Cloudy', 'Partly cloudy', 'Partly cloudy', 'Partly cloudy', 'Partly cloudy', 'Sunny', 'Partly cloudy', 'Cloudy', 'Overcast', 'Overcast', 'Overcast', 'Overcast', 'Cloudy']
# precip_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#
# if not all(precip_data):
#     from random import randint
#
#     precip_data[randint(0, len(precip_data) - 1)] += 0.25
#     precip_data[randint(0, len(precip_data) - 1)] += 0.19
#
# fig, ax = plt.subplots(figsize=(20, 3))
#
# x = np.linspace(time[0], time[-1], 100)
#
# poly_coeffs = np.polyfit(time, temp_data, 12)
#
# y = np.polyval(poly_coeffs, x)
# # y = np.interp(x, time, temp_data)
#
# # Plot data
# ax.plot(x, y, label="Temperature", color="#f2a28c")
# ax.set_xlabel('Temperature')
#
# ax.set_xticks(time)
#
# time = [datetime.datetime(2023, 11, 2, i, 0, 0).time().strftime("%I:%M %p") for i in time]
# print(time)
#
# labels = [f"{t}\n"+"\n".join(text_data[i].split()) + f"\n{wind_data[i]}m/s" for i, t in enumerate(time)]
#
# ax.set_xticklabels(labels)
#
# ax2 = ax.twinx()
#
# ax2.set_ylim(0, max(precip_data) * 5)
#
# bars = ax2.bar(time, precip_data, alpha=0.5, width=0.9, color='lightgray', label='Humidity')
# font = {
#         'size': 6,
#         'ha': 'left',
#         'va': 'center',
#         'color': 'gray'
#     }
# for i, bar in enumerate(bars):
#     t = ax2.text(bar.get_x(), bar.get_height() + 0.1, f"{precip_data[i]}mm/h".center(12) + "\n" + f"{humidity_data[i]}%".center(18), fontdict=font)
#
# ax2.set_xlabel('Humidity')
#
#
# ax.legend(loc='upper left')
# ax2.legend(loc='upper right')
#
# # ax2.set_yticklabels(humidity_data)
#
# # plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
#
# plt.show()
