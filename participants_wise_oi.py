import datetime
import pandas as pd
import requests
import io
import plotly.subplots as subplots
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.offline as offline




import datetime
import requests

class GetPwoiData:
    def __init__(self):
        self.today = datetime.datetime.now().date()
        self.today_date_string = self.today.strftime("%d%m%Y")
        self.last_5_days_date_string = self.get_last_five_working_days()
        self.data = self.fetch_data()[0]
        self.pwoi_date = self.fetch_data()[1].strftime("%b %d %Y")
        self.decoded_data = io.StringIO(self.data.decode("utf-8"))
        self.x_axis = ['Index Future Long', 'Index Call Long', 'Index Put Short', 'Stock Future Long', 'Stock Call Long', 'Stock Put Short']
        self.x2_axis = ['Index Future Short', 'Index Call Short', 'Index Put Long', 'Stock Future Short', 'Stock Call Short', 'Stock Put Long' ]
        self.df = pd.read_csv(self.decoded_data, skiprows=1)

    def get_last_five_working_days(self):
        working_days = []
        for i in range(5):
            current_day = self.today - datetime.timedelta(days=i)
            if current_day.weekday() not in [5, 6]:
                working_days.append(current_day)
        return [day.strftime("%d%m%Y") for day in working_days]

    def fetch_data(self):
        for date in self.last_5_days_date_string:
            try:
                url = f"https://www1.nseindia.com/content/nsccl/fao_participant_oi_{date}.csv"
                response = requests.get(url)
                if response.status_code == 200:
                    return (response.content, datetime.datetime.strptime(date, "%d%m%Y"))
            except:
                continue
        return None

    def plot_graph1(self):
        index_future_long= self.df[self.df.columns[1]]
        index_call_long = self.df[self.df.columns[5]]
        index_put_long = self.df[self.df.columns[6]]
        stock_future_long = self.df[self.df.columns[3]]
        stock_call_long = self.df[self.df.columns[9]]
        stock_put_long = self.df[self.df.columns[10]]
        index_future_short = self.df[self.df.columns[2]]
        index_call_short = self.df[self.df.columns[7]]
        index_put_short = self.df[self.df.columns[8]]
        stock_future_short = self.df[self.df.columns[4]]
        stock_call_short = self.df[self.df.columns[11]]
        stock_put_short = self.df[self.df.columns[12]]
        fig = go.Figure(data=[go.Bar(name='Client', x=self.x_axis, y=[index_future_long[0],index_call_long[0],index_put_short[0],stock_future_long[0],stock_call_long[0],stock_put_short[0]], visible=True),
        go.Bar(name='DII', x=self.x_axis, y=[index_future_long[1],index_call_long[1],index_put_short[1],stock_future_long[1],stock_call_long[1],stock_put_short[1]], visible=True),
        go.Bar(name='FII', x=self.x_axis, y=[index_future_long[2],index_call_long[2],index_put_short[2],stock_future_long[2],stock_call_long[2],stock_put_short[2]], visible=True),
        go.Bar(name='PRO', x=self.x_axis, y=[index_future_long[3],index_call_long[3],index_put_short[3],stock_future_long[3],stock_call_long[3],stock_put_short[3]], visible=True),])
        fig.update_layout(title=dict(text='Bullish Positions', font=dict(size=24, color='#009933'))),
        fig.update_xaxes(tickfont=dict(size=15))
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
    def plot_graph2(self):
        index_future_long= self.df[self.df.columns[1]]
        index_call_long = self.df[self.df.columns[5]]
        index_put_long = self.df[self.df.columns[6]]
        stock_future_long = self.df[self.df.columns[3]]
        stock_call_long = self.df[self.df.columns[9]]
        stock_put_long = self.df[self.df.columns[10]]
        index_future_short = self.df[self.df.columns[2]]
        index_call_short = self.df[self.df.columns[7]]
        index_put_short = self.df[self.df.columns[8]]
        stock_future_short = self.df[self.df.columns[4]]
        stock_call_short = self.df[self.df.columns[11]]
        stock_put_short = self.df[self.df.columns[12]]
        fig = go.Figure(data=[
        go.Bar(name='Client', x=self.x2_axis, y=[index_future_short[0],index_call_short[0],index_put_long[0],stock_future_short[0],stock_call_short[0],stock_put_long[0]], visible=True),
        go.Bar(name='DII', x=self.x2_axis, y=[index_future_short[1],index_call_short[1],index_put_long[1],stock_future_short[1],stock_call_short[1],stock_put_long[1]], visible=True),
        go.Bar(name='FII', x=self.x2_axis,y=[index_future_short[2],index_call_short[2],index_put_long[2],stock_future_short[2],stock_call_short[2],stock_put_long[2]], visible=True),
        go.Bar(name='PRO', x=self.x2_axis, y=[index_future_short[3],index_call_short[3],index_put_long[3],stock_future_short[3],stock_call_short[3],stock_put_long[3]], visible=True),])
        fig.update_yaxes(autorange="reversed")
        fig.update_xaxes(tickfont=dict(size=12))
        fig.update_xaxes(side='top')
        fig.update_xaxes(tickfont=dict(color='red'))
        fig.update_xaxes(title_standoff=10)
        fig.update_layout(title=dict(text='Bearish Positions', font=dict(size=24, color='red'))),
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html

    def pie_chart_long(self):
        index_future_long= self.df[self.df.columns[1]]
        index_call_long = self.df[self.df.columns[5]]
        index_put_long = self.df[self.df.columns[6]]
        stock_future_long = self.df[self.df.columns[3]]
        stock_call_long = self.df[self.df.columns[9]]
        stock_put_long = self.df[self.df.columns[10]]
        index_future_short = self.df[self.df.columns[2]]
        index_call_short = self.df[self.df.columns[7]]
        index_put_short = self.df[self.df.columns[8]]
        stock_future_short = self.df[self.df.columns[4]]
        stock_call_short = self.df[self.df.columns[11]]
        stock_put_short = self.df[self.df.columns[12]]
        total_long = self.df[self.df.columns[13]]
        total_short = self.df[self.df.columns[14]]
        client_long =[index_future_long[0],index_call_long[0],index_put_long[0],stock_future_long[0],stock_call_long[0],stock_put_long[0]]
        client_short = [index_future_short[0],index_call_short[0],index_put_short[0],stock_future_short[0],stock_call_short[0],stock_put_short[0]]
        dii_long =[index_future_long[1],index_call_long[1],index_put_long[1],stock_future_long[1],stock_call_long[1],stock_put_long[1]]
        dii_short = [index_future_short[1],index_call_short[1],index_put_short[1],stock_future_short[1],stock_call_short[1],stock_put_short[1]]
        fii_long = [index_future_long[2],index_call_long[2],index_put_long[2],stock_future_long[2],stock_call_long[2],stock_put_long[2]]
        fii_short = [index_future_short[2],index_call_short[2],index_put_short[2],stock_future_short[2],stock_call_short[2],stock_put_short[2]]
        pro_long = [index_future_long[3],index_call_long[3],index_put_long[3],stock_future_long[3],stock_call_long[3],stock_put_long[3]]
        pro_short = [index_future_short[3],index_call_short[3],index_put_short[3],stock_future_short[3],stock_call_short[3],stock_put_short[3]]
        labels = ['Client','DII', 'FII', 'PRO']
        values1 = [sum(client_long), sum(dii_long), sum(fii_long), sum(pro_long)]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values1)])
        fig.update_layout(title=dict(text="Longs Position", font=dict(color="Green")),)
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
    def pie_chart_short(self):
        index_future_long= self.df[self.df.columns[1]]
        index_call_long = self.df[self.df.columns[5]]
        index_put_long = self.df[self.df.columns[6]]
        stock_future_long = self.df[self.df.columns[3]]
        stock_call_long = self.df[self.df.columns[9]]
        stock_put_long = self.df[self.df.columns[10]]
        index_future_short = self.df[self.df.columns[2]]
        index_call_short = self.df[self.df.columns[7]]
        index_put_short = self.df[self.df.columns[8]]
        stock_future_short = self.df[self.df.columns[4]]
        stock_call_short = self.df[self.df.columns[11]]
        stock_put_short = self.df[self.df.columns[12]]
        total_long = self.df[self.df.columns[13]]
        total_short = self.df[self.df.columns[14]]
        client_long =[index_future_long[0],index_call_long[0],index_put_long[0],stock_future_long[0],stock_call_long[0],stock_put_long[0]]
        client_short = [index_future_short[0],index_call_short[0],index_put_short[0],stock_future_short[0],stock_call_short[0],stock_put_short[0]]
        dii_long =[index_future_long[1],index_call_long[1],index_put_long[1],stock_future_long[1],stock_call_long[1],stock_put_long[1]]
        dii_short = [index_future_short[1],index_call_short[1],index_put_short[1],stock_future_short[1],stock_call_short[1],stock_put_short[1]]
        fii_long = [index_future_long[2],index_call_long[2],index_put_long[2],stock_future_long[2],stock_call_long[2],stock_put_long[2]]
        fii_short = [index_future_short[2],index_call_short[2],index_put_short[2],stock_future_short[2],stock_call_short[2],stock_put_short[2]]
        pro_long = [index_future_long[3],index_call_long[3],index_put_long[3],stock_future_long[3],stock_call_long[3],stock_put_long[3]]
        pro_short = [index_future_short[3],index_call_short[3],index_put_short[3],stock_future_short[3],stock_call_short[3],stock_put_short[3]]
        labels = ['Client','DII', 'FII', 'PRO']
        values2 = [sum(client_short), sum(dii_short), sum(fii_short), sum(pro_short)]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values2)])
        fig.update_layout(title=dict(text="Shorts Position", font=dict(color="Red")),)
        plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
        return plot_html
