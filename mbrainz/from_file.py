import json
import plotly.express as px
import pandas as pd
import datetime

f_filename = 'data/katatonia.json'

artists = []
with open(f_filename) as f:
    data = json.load(f)
    print(f"{data['name']}")
    relations = data['relations']
    for relation in relations:
        artists.append({'name': relation['artist']['name'], 'start': relation['begin'], 'end': relation['end'] or datetime.date.today()})
        print(f"{relation['artist']['name']}: {relation['begin']}  - {relation['end']}")


df = pd.DataFrame([dict(Name=value['name'], Start=value['start'], End=value['end'], Resource='A')
                   for value in artists])

fig = px.timeline(df, x_start="Start", x_end="End", y="Name", color="Resource")
fig.update_yaxes(autorange="reversed")
fig.show()
