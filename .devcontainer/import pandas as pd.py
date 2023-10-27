import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"

data = pd.read_excel("/kaggle/input/hiv-new-cases-2017-ke/HIV New cases 2017.xlsx")
print(data.head())
