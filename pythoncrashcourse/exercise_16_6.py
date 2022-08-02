import json
from plotly.graph_objs import Layout
from plotly import offline, colors

# Explore the structure of the data.
eq_filename = 'data/eq_data_30_day_m1.json'

mags, lons, lats, hover_texts = [], [], [], []

with open(eq_filename) as f:
    all_eq_data = json.load(f)
    all_eq_dicts = all_eq_data['features']


for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

print(mags[:10])
print(len(all_eq_dicts))

for key in colors.PLOTLY_SCALES.keys():
    print(key)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='/tmp/global_earthquakes.html')
