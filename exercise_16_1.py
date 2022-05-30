import csv
import matplotlib.pyplot as plt
from datetime import datetime

filenames = ['data/sitka_weather_2018_simple.csv', 'data/death_valley_2018_simple.csv']

highs = []
lows = []
dates = []

for filename in filenames:
    with open(filename) as f:
        reader = csv.reader(f)
        headers = {}
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            headers |= {column_header: int(index)}
            print(index, column_header)

        for row in reader:
            current_date = datetime.strptime(row[headers.get('DATE')], '%Y-%m-%d')
            try:
                high = int(row[headers.get('TMAX')])
                low = int(row[headers.get('TMIN')])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                highs.append(high)
                lows.append(low)
                dates.append(current_date)




plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Temperatures 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()
