import datetime
import pandas as pd
import requests
import io
import plotly.subplots as subplots
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as offline
class ParticipantsWiseOi:
    def __init__(self):
        # today = datetime.datetime.now()
        # self.date_string = today.strftime("%d%m%Y")
        self.url = f"https://www1.nseindia.com/content/nsccl/fao_participant_oi_04012023.csv"
        self.x_axis = ['Index Futures Long', 'Index Call Long', 'Index Put Shorts', 'Stock Futures Long', 'Stock Call Long', 'Stock Put Short']
        self.x2_axis = ['Index Futures Short', 'Index Call Short', 'Index Put Long', 'Stock Futures Short', 'Stock Call Short', 'Stock Put Long' ]
        self.fetch_participants_wise_oi()
    def fetch_participants_wise_oi(self):
        response = requests.get(self.url)
        data = response.content
        data = io.StringIO(data.decode("utf-8"))
        df = pd.read_csv(data, skiprows=1)
        index_futures_long= df[df.columns[1]]
        index_call_long = df[df.columns[5]]
        index_put_long = df[df.columns[6]]
        stock_futures_long = df[df.columns[3]]
        stock_call_long = df[df.columns[9]]
        stock_put_long = df[df.columns[10]]
        index_futures_short = df[df.columns[2]]
        index_call_short = df[df.columns[7]]
        index_put_short = df[df.columns[8]]
        stock_futures_short = df[df.columns[4]]
        stock_call_short = df[df.columns[11]]
        stock_put_short = df[df.columns[12]]
        fig = go.Figure(data=[go.Bar(name='Client', x=self.x_axis, y=[index_futures_long[0],index_call_long[0],index_put_short[0],stock_futures_long[0],stock_call_long[0],stock_put_short[0]], visible=True),
        go.Bar(name='DII', x=self.x_axis, y=[index_futures_long[1],index_call_long[1],index_put_short[1],stock_futures_long[1],stock_call_long[1],stock_put_short[1]], visible=True),
        go.Bar(name='FII', x=self.x_axis, y=[index_futures_long[2],index_call_long[2],index_put_short[2],stock_futures_long[2],stock_call_long[2],stock_put_short[2]], visible=True),
        go.Bar(name='PRO', x=self.x_axis, y=[index_futures_long[3],index_call_long[3],index_put_short[3],stock_futures_long[3],stock_call_long[3],stock_put_short[3]], visible=True),])
        fig.update_layout(title=dict(text='Bullish Positions', font=dict(size=24, color='#000000'))),
        fig.update_xaxes(tickfont=dict(size=20))
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
    def fetch_participants_wise_oi_graph2(self):
        response = requests.get(self.url)
        data = response.content
        data = io.StringIO(data.decode("utf-8"))
        df = pd.read_csv(data, skiprows=1)
        index_futures_long= df[df.columns[1]]
        index_call_long = df[df.columns[5]]
        index_put_long = df[df.columns[6]]
        stock_futures_long = df[df.columns[3]]
        stock_call_long = df[df.columns[9]]
        stock_put_long = df[df.columns[10]]
        index_futures_short = df[df.columns[2]]
        index_call_short = df[df.columns[7]]
        index_put_short = df[df.columns[8]]
        stock_futures_short = df[df.columns[4]]
        stock_call_short = df[df.columns[11]]
        stock_put_short = df[df.columns[12]]
        fig = go.Figure(data=[
        go.Bar(name='Client', x=self.x2_axis, y=[index_futures_short[0],index_call_short[0],index_put_long[0],stock_futures_short[0],stock_call_short[0],stock_put_long[0]], visible=True),
        go.Bar(name='DII', x=self.x2_axis, y=[index_futures_short[1],index_call_short[1],index_put_long[1],stock_futures_short[1],stock_call_short[1],stock_put_long[1]], visible=True),
        go.Bar(name='FII', x=self.x2_axis,y=[index_futures_short[2],index_call_short[2],index_put_long[2],stock_futures_short[2],stock_call_short[2],stock_put_long[2]], visible=True),
        go.Bar(name='PRO', x=self.x2_axis, y=[index_futures_short[3],index_call_short[3],index_put_long[3],stock_futures_short[3],stock_call_short[3],stock_put_long[3]], visible=True),])
        fig.update_yaxes(autorange="reversed")
        fig.update_xaxes(tickfont=dict(size=20))
        fig.update_xaxes(side='top')
        fig.update_xaxes(tickfont=dict(color='red'))
        fig.update_xaxes(title_standoff=10)
        fig.update_layout(title=dict(text='Bearish Positions', font=dict(size=24, color='#000000'))),
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
    def pie_chart_long(self):
        response = requests.get(self.url)
        data = response.content
        data = io.StringIO(data.decode("utf-8"))
        df = pd.read_csv(data, skiprows=1)
        index_futures_long= df[df.columns[1]]
        index_call_long = df[df.columns[5]]
        index_put_long = df[df.columns[6]]
        stock_futures_long = df[df.columns[3]]
        stock_call_long = df[df.columns[9]]
        stock_put_long = df[df.columns[10]]
        index_futures_short = df[df.columns[2]]
        index_call_short = df[df.columns[7]]
        index_put_short = df[df.columns[8]]
        stock_futures_short = df[df.columns[4]]
        stock_call_short = df[df.columns[11]]
        stock_put_short = df[df.columns[12]]
        total_long = df[df.columns[13]]
        total_short = df[df.columns[14]]
        client_long =[index_futures_long[0],index_call_long[0],index_put_long[0],stock_futures_long[0],stock_call_long[0],stock_put_long[0]]
        client_short = [index_futures_short[0],index_call_short[0],index_put_short[0],stock_futures_short[0],stock_call_short[0],stock_put_short[0]]
        dii_long =[index_futures_long[1],index_call_long[1],index_put_long[1],stock_futures_long[1],stock_call_long[1],stock_put_long[1]]
        dii_short = [index_futures_short[1],index_call_short[1],index_put_short[1],stock_futures_short[1],stock_call_short[1],stock_put_short[1]]
        fii_long = [index_futures_long[2],index_call_long[2],index_put_long[2],stock_futures_long[2],stock_call_long[2],stock_put_long[2]]
        fii_short = [index_futures_short[2],index_call_short[2],index_put_short[2],stock_futures_short[2],stock_call_short[2],stock_put_short[2]]
        pro_long = [index_futures_long[3],index_call_long[3],index_put_long[3],stock_futures_long[3],stock_call_long[3],stock_put_long[3]]
        pro_short = [index_futures_short[3],index_call_short[3],index_put_short[3],stock_futures_short[3],stock_call_short[3],stock_put_short[3]]
        labels = ['Client','DII', 'FII', 'PRO']
        values1 = [sum(client_long), sum(dii_long), sum(fii_long), sum(pro_long)]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
    def pie_chart_short(self):
        response = requests.get(self.url)
        data = response.content
        data = io.StringIO(data.decode("utf-8"))
        df = pd.read_csv(data, skiprows=1)
        index_futures_long= df[df.columns[1]]
        index_call_long = df[df.columns[5]]
        index_put_long = df[df.columns[6]]
        stock_futures_long = df[df.columns[3]]
        stock_call_long = df[df.columns[9]]
        stock_put_long = df[df.columns[10]]
        index_futures_short = df[df.columns[2]]
        index_call_short = df[df.columns[7]]
        index_put_short = df[df.columns[8]]
        stock_futures_short = df[df.columns[4]]
        stock_call_short = df[df.columns[11]]
        stock_put_short = df[df.columns[12]]
        total_long = df[df.columns[13]]
        total_short = df[df.columns[14]]
        client_long =[index_futures_long[0],index_call_long[0],index_put_long[0],stock_futures_long[0],stock_call_long[0],stock_put_long[0]]
        client_short = [index_futures_short[0],index_call_short[0],index_put_short[0],stock_futures_short[0],stock_call_short[0],stock_put_short[0]]
        dii_long =[index_futures_long[1],index_call_long[1],index_put_long[1],stock_futures_long[1],stock_call_long[1],stock_put_long[1]]
        dii_short = [index_futures_short[1],index_call_short[1],index_put_short[1],stock_futures_short[1],stock_call_short[1],stock_put_short[1]]
        fii_long = [index_futures_long[2],index_call_long[2],index_put_long[2],stock_futures_long[2],stock_call_long[2],stock_put_long[2]]
        fii_short = [index_futures_short[2],index_call_short[2],index_put_short[2],stock_futures_short[2],stock_call_short[2],stock_put_short[2]]
        pro_long = [index_futures_long[3],index_call_long[3],index_put_long[3],stock_futures_long[3],stock_call_long[3],stock_put_long[3]]
        pro_short = [index_futures_short[3],index_call_short[3],index_put_short[3],stock_futures_short[3],stock_call_short[3],stock_put_short[3]]
        labels = ['Client','DII', 'FII', 'PRO']
        values2 = [sum(client_short), sum(dii_short), sum(fii_short), sum(pro_short)]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
