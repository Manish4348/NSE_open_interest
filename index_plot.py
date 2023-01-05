from mongo_db_connect import   fetch_for_indices
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objects as go
import plotly.offline as offline
import plotly.express as px
import pandas as pd

# data = fetch_for_indices("BANKNIFTY")
# strikes, f_strikes, call_oi, put_oi, call_oi_change, put_oi_change, call_volume, put_volume = data.plot_data()

# class PlotPlotlyIndex():
#     def __init__(self, index, strikes, f_strikes, call_oi, put_oi, call_oi_change, put_oi_change, call_volume, put_volume):
#         self.index = index
#         self.strikes = strikes
#         self.f_strikes = f_strikes
#         self.call_oi = call_oi
#         self.put_oi = put_oi
#         self.call_oi_change = call_oi_change
#         self.put_oi_change = put_oi_change
#         self.call_volume = call_volume
#         self.put_volume = put_volume
#     def plotly(self):
#         hist1 = go.Bar(x=f_strikes, y=call_oi, marker_color='red', name = "Call OI")
#         hist2 = go.Bar(x=f_strikes, y=put_oi, marker_color='green', name = "Put OI")
#         volume_trace1 = go.Scatter(x=f_strikes, y=self.call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
#         volume_trace2 = go.Scatter(x=f_strikes, y=self.put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
#         fig = go.Figure(data=[hist1, hist2, volume_trace2, volume_trace1])
#         fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
#         fig.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
#         fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
#         fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
#                           xaxis_title=dict(text='Nifty', font=dict(size=20, color='#000000')),
#                           yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
#                           yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
#         plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
#         return plot_html

