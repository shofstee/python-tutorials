import csv

from plotly.graph_objs import Layout
from plotly.offline import offline

f_filename = 'data/world_fires_7_day.csv'

latitudes, longitudes, brightness =[], [], []
min, max = 0, 0
with open(f_filename) as f:
    reader = csv.reader(f)
    headers = {}
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        headers |= {column_header: int(index)}
        print(index, column_header)

    for row in reader:
        latitudes.append(row[headers.get('latitude')])
        longitudes.append(row[headers.get('longitude')])
        brt = float(row[headers.get('bright_ti4')])
        brightness.append(brt)
        if brt > max:
            max = brt
        if brt < min:
            min = brt

data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
     'text': brightness,
     'marker': {
         'color': [brt for brt in brightness],
         'colorscale': 'Viridis',
         'reversescale': True,
         'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='/tmp/global_fires.html')
