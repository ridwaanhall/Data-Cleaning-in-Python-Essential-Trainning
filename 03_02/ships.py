# %%
import pandas as pd

df = pd.read_csv('ships.csv')
df
# %%
import pandera as pa
import numpy as np

# there error, because pandera doesn't support nan
schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String),
    'lat': pa.Column(pa.Float, nullable=True), # so, we must add nullable=True
    'lng': pa.Column(pa.Float, nullable=True),
})

schema.validate(df)

# %%
