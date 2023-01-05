from flask import Flask, render_template, request
import requests
import json
import pymongo
from pymongo import MongoClient
# import time
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
# from index_plot import plot_finnifty_total_call_oi, plot_finnifty_total_call_oi_change, plot_finnifty_total_put_oi, plot_finnifty_total_put_oi_change, plot_USDINR_total_call_oi, plot_USDINR_total_call_oi_change, plot_USDINR_total_put_oi, plot_USDINR_total_put_oi_change, plot_CRUDEOIL_total_call_oi, plot_CRUDEOIL_total_call_oi_change, plot_CRUDEOIL_total_put_oi, plot_CRUDEOIL_total_put_oi_change, plot_NATURALGAS_total_call_oi, plot_NATURALGAS_total_call_oi_change, plot_NATURALGAS_total_put_oi, plot_NATURALGAS_total_put_oi_change
from mongo_db_connect import fetch_for_indices, fetch_for_commodity
import plotly
import plotly.graph_objects as go
import plotly.offline as offline
import plotly.express as px
import pandas as pd
from participants_wise_oi import ParticipantsWiseOi


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/nifty')
def nifty():
    data = fetch_for_indices("NIFTY")
    spot_price, total_call_oi, total_put_oi = data.fetch()
    time = data.time
    pcr = total_put_oi/total_call_oi
    strikes, f_strikes, call_oi, put_oi, call_oi_change, put_oi_change, call_volume, put_volume = data.plot_data()
    hist1 = go.Bar(x=f_strikes, y=call_oi, marker_color='red', name = "Call OI")
    hist2 = go.Bar(x=f_strikes, y=put_oi, marker_color='green', name = "Put OI")
    volume_trace1 = go.Scatter(x=f_strikes, y=call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
    volume_trace2 = go.Scatter(x=f_strikes, y=put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
    fig = go.Figure(data=[hist1, hist2, volume_trace2, volume_trace1])
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='Nifty', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
    # offline.plot(fig, filename='plot.html', auto_open=False)
    # with open('plot.html', 'r') as f:
    #     plot_html = f.read()
    hist3 = go.Bar(x=f_strikes, y=call_oi_change, marker_color='red', name = "Call OI Change")
    hist4 = go.Bar(x=f_strikes, y=put_oi_change, marker_color='green', name = "Put OI Change")
    fig2=go.Figure(data=[hist3, hist4])
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-45)
    fig2.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig2.update_layout(
    title=dict(text='Open Interest Change', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='Nifty', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot2_html = offline.plot(fig2, include_plotlyjs=True, output_type='div')
    offline.plot(fig2, filename='plot2.html', auto_open=False)
    # with open('plot2.html', 'r') as f:
    #     plot2_html = f.read()
    return render_template('nifty.html',spot_price=spot_price, pcr=round(pcr, 3), total_call_oi=total_call_oi, total_put_oi=total_put_oi, plot_html=plot_html, plot2_html=plot2_html, time=time)


@app.route('/banknifty')
def banknifty():
    data = fetch_for_indices("BANKNIFTY")
    spot_price, total_call_oi, total_put_oi = data.fetch()
    pcr = total_put_oi/total_call_oi
    time = data.time
    strikes, f_strikes, call_oi, put_oi, call_oi_change, put_oi_change, call_volume, put_volume = data.plot_data()
    hist1 = go.Bar(x=f_strikes, y=call_oi, marker_color='red', name = "Call OI")
    hist2 = go.Bar(x=f_strikes, y=put_oi, marker_color='green', name = "Put OI")
    volume_trace1 = go.Scatter(x=f_strikes, y=call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
    volume_trace2 = go.Scatter(x=f_strikes, y=put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
    fig = go.Figure(data=[hist1, hist2, volume_trace2, volume_trace1])
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='BANKNIFTY', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
    # offline.plot(fig, filename='plot.html', auto_open=False)
    # with open('plot.html', 'r') as f:
    #     plot_html = f.read()
    hist3 = go.Bar(x=f_strikes, y=call_oi_change, marker_color='red', name = "Call OI Change")
    hist4 = go.Bar(x=f_strikes, y=put_oi_change, marker_color='green', name = "Put OI Change")
    fig2=go.Figure(data=[hist3, hist4])
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-45)
    fig2.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig2.update_layout(
    title=dict(text='Open Interest Change', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='BANKNITFY', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot2_html = offline.plot(fig2, include_plotlyjs=True, output_type='div')
    offline.plot(fig2, filename='plot2.html', auto_open=False)
    return render_template('banknifty.html', spot_price=spot_price, pcr=round(pcr, 3), total_call_oi=total_call_oi, total_put_oi=total_put_oi, plot_html=plot_html, plot2_html=plot2_html, time=time)

@app.route('/finnifty')
def finnifty():
    data = fetch_for_indices("FINNIFTY")
    spot_price, total_call_oi, total_put_oi = data.fetch()
    pcr = total_put_oi/total_call_oi
    time = data.time
    strikes, f_strikes, call_oi, put_oi, call_oi_change, put_oi_change, call_volume, put_volume = data.plot_data()
    hist1 = go.Bar(x=f_strikes, y=call_oi, marker_color='red', name = "Call OI")
    hist2 = go.Bar(x=f_strikes, y=put_oi, marker_color='green', name = "Put OI")
    volume_trace1 = go.Scatter(x=f_strikes, y=call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
    volume_trace2 = go.Scatter(x=f_strikes, y=put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
    fig = go.Figure(data=[hist1, hist2, volume_trace2, volume_trace1])
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='FinNifty', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
    # offline.plot(fig, filename='plot.html', auto_open=False)
    # with open('plot.html', 'r') as f:
    #     plot_html = f.read()
    hist3 = go.Bar(x=f_strikes, y=call_oi_change, marker_color='red', name = "Call OI Change")
    hist4 = go.Bar(x=f_strikes, y=put_oi_change, marker_color='green', name = "Put OI Change")
    fig2=go.Figure(data=[hist3, hist4])
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-45)
    fig2.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig2.update_layout(
    title=dict(text='Open Interest Change', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='FINNIFTY', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot2_html = offline.plot(fig2, include_plotlyjs=True, output_type='div')
    offline.plot(fig2, filename='plot2.html', auto_open=False)
    return render_template('finnifty.html', spot_price=spot_price, pcr=round(pcr, 3), total_call_oi=total_call_oi, total_put_oi=total_put_oi,plot_html=plot_html, plot2_html=plot2_html, time=time)

@app.route('/usdinr')
def usdinr():
    data = fetch_for_indices("USDINR")
    spot_price, total_call_oi, total_put_oi = data.fetch()
    pcr = total_put_oi/total_call_oi
    time = data.time
    strikes, f_strikes, call_oi, put_oi, call_oi_change, put_oi_change, call_volume, put_volume = data.plot_data()
    hist1 = go.Bar(x=f_strikes, y=call_oi, marker_color='red', name = "Call OI")
    hist2 = go.Bar(x=f_strikes, y=put_oi, marker_color='green', name = "Put OI")
    volume_trace1 = go.Scatter(x=f_strikes, y=call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
    volume_trace2 = go.Scatter(x=f_strikes, y=put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
    fig = go.Figure(data=[hist1, hist2, volume_trace2, volume_trace1])
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='USDINR', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
    # offline.plot(fig, filename='plot.html', auto_open=False)
    # with open('plot.html', 'r') as f:
    #     plot_html = f.read()
    hist3 = go.Bar(x=f_strikes, y=call_oi_change, marker_color='red', name = "Call OI Change")
    hist4 = go.Bar(x=f_strikes, y=put_oi_change, marker_color='green', name = "Put OI Change")
    fig2=go.Figure(data=[hist3, hist4])
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-45)
    fig2.update_layout(xaxis=dict(tickmode='array', tickvals=f_strikes, ticktext=f_strikes, tickformat=',d'))
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig2.update_layout(
    title=dict(text='Open Interest Change', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='USDINR', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot2_html = offline.plot(fig2, include_plotlyjs=True, output_type='div')
    offline.plot(fig2, filename='plot2.html', auto_open=False)
    return render_template('usdinr.html', spot_price=spot_price, pcr=round(pcr, 3), total_call_oi=total_call_oi, total_put_oi=total_put_oi, plot_html=plot_html, plot2_html=plot2_html, time=time)

@app.route('/crudeoil')
def crudeoil():
    data = fetch_for_commodity("CRUDEOIL")
    call_oi , put_oi, spot_price = [], [], data.fetch()['d']['Data'][0]['UnderlyingValue']
    # time = data.last_time
    for i in range(len(data.fetch()['d']['Data'])):
        call_oi.append(data.fetch()['d']['Data'][i]['CE_OpenInterest'])
    for i in range(len(data.fetch()['d']['Data'])):
        put_oi.append(data.fetch()['d']['Data'][i]['PE_OpenInterest'])
    strike_price, call_oi_change, put_oi_change = [], [], []
    for i in range(len(data.fetch()['d']['Data'])):
        strike_price.append(data.fetch()['d']['Data'][i]['CE_StrikePrice'])
    for i in range(len(data.fetch()['d']['Data'])):
        call_oi_change.append(data.fetch()['d']['Data'][i]['CE_ChangeInOI'])
    for i in range(len(data.fetch()['d']['Data'])):
        put_oi_change.append(data.fetch()['d']['Data'][i]['PE_ChangeInOI'])
    pcr = sum(put_oi)/sum(call_oi)

    hist1 = go.Bar(x=strike_price, y=call_oi, marker_color='red', name = "Call OI")
    hist2 = go.Bar(x=strike_price, y=put_oi, marker_color='green', name = "Put OI")
    # volume_trace1 = go.Scatter(x=strike_price, y=call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
    # volume_trace2 = go.Scatter(x=strike_price, y=put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
    fig = go.Figure(data=[hist1, hist2])
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=strike_price, ticktext=strike_price, tickformat=',d'))
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='CRUDEOIL', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
    hist3 = go.Bar(x=strike_price, y=call_oi_change, marker_color='red', name = "Call OI Change")
    hist4 = go.Bar(x=strike_price, y=put_oi_change, marker_color='green', name = "Put OI Change")
    fig2=go.Figure(data=[hist3, hist4])
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-45)
    fig2.update_layout(xaxis=dict(tickmode='array', tickvals=strike_price, ticktext=strike_price, tickformat=',d'))
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig2.update_layout(
    title=dict(text='Open Interest Change', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='CRUDEOIL', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot2_html = offline.plot(fig2, include_plotlyjs=True, output_type='div')
    offline.plot(fig2, filename='plot2.html', auto_open=False)
    return render_template('crudeoil.html', spot_price=spot_price,pcr=round(pcr, 3), total_call_oi = sum(call_oi), total_put_oi = sum(put_oi), plot_html=plot_html, plot2_html=plot2_html)

@app.route('/naturalgas')
def naturalgas():
    data = fetch_for_commodity("NATURALGAS")
    call_oi , put_oi, spot_price = [], [], data.fetch()['d']['Data'][0]['UnderlyingValue']
    # time = data.last_time
    for i in range(len(data.fetch()['d']['Data'])):
        call_oi.append(data.fetch()['d']['Data'][i]['CE_OpenInterest'])
    for i in range(len(data.fetch()['d']['Data'])):
        put_oi.append(data.fetch()['d']['Data'][i]['PE_OpenInterest'])
    strike_price, call_oi_change, put_oi_change = [], [], []
    for i in range(len(data.fetch()['d']['Data'])):
        strike_price.append(data.fetch()['d']['Data'][i]['CE_StrikePrice'])
    for i in range(len(data.fetch()['d']['Data'])):
        call_oi_change.append(data.fetch()['d']['Data'][i]['CE_ChangeInOI'])
    for i in range(len(data.fetch()['d']['Data'])):
        put_oi_change.append(data.fetch()['d']['Data'][i]['PE_ChangeInOI'])
    pcr = sum(put_oi)/sum(call_oi)

    hist1 = go.Bar(x=strike_price, y=call_oi, marker_color='red', name = "Call OI")
    hist2 = go.Bar(x=strike_price, y=put_oi, marker_color='green', name = "Put OI")
    # volume_trace1 = go.Scatter(x=strike_price, y=call_volume, mode='lines', name='Volume Call OI', yaxis='y2')
    # volume_trace2 = go.Scatter(x=strike_price, y=put_volume, mode='lines', name='Volume Put OI', yaxis='y2')
    fig = go.Figure(data=[hist1, hist2])
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-60)
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=strike_price, ticktext=strike_price, tickformat=',d'))
    fig.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig.update_layout(title=dict(text='Open Interest', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='NATURALGAS', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot_html = offline.plot(fig, include_plotlyjs=True, output_type='div')
    hist3 = go.Bar(x=strike_price, y=call_oi_change, marker_color='red', name = "Call OI Change")
    hist4 = go.Bar(x=strike_price, y=put_oi_change, marker_color='green', name = "Put OI Change")
    fig2=go.Figure(data=[hist3, hist4])
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'),xaxis_tickangle=-45)
    fig2.update_layout(xaxis=dict(tickmode='array', tickvals=strike_price, ticktext=strike_price, tickformat=',d'))
    fig2.update_layout(yaxis2=dict(overlaying='y', side='right'), xaxis=dict(rangeslider=dict(visible=False)))
    fig2.update_layout(
    title=dict(text='Open Interest Change', font=dict(size=24, color='#000000')),
    xaxis_title=dict(text='NATURALGAS', font=dict(size=20, color='#000000')),
    yaxis_title=dict(text='Open Interest (in M)', font=dict(size=20, color='#000000')),
    yaxis2_title=dict(text='Volume', font=dict(size=20, color='#000000')))
    plot2_html = offline.plot(fig2, include_plotlyjs=True, output_type='div')
    offline.plot(fig2, filename='plot2.html', auto_open=False)

    return render_template('naturalgas.html', spot_price=spot_price,pcr=round(pcr,3), total_call_oi = sum(call_oi), total_put_oi = sum(put_oi), plot_html=plot_html, plot2_html=plot2_html)

@app.route('/pwi')
def pwi():
    data = ParticipantsWiseOi()
    plot_data = data.fetch_participants_wise_oi()
    plot_data2 = data.fetch_participants_wise_oi_graph2()
    plot_data3 = data.pie_chart_long()
    plot_data4 = data.pie_chart_short()
    return render_template('pwi.html', plot_data=plot_data, plot_data2=plot_data2, plot_data3 = plot_data3, plot_data4=plot_data4)
@app.route("/timelapseoi")
def timelapseoi():
    return render_template('timelapseoi.html')

@app.route('/get_input')
def get_input():
    table = []
    table.append(["FII", "DII", "PRO", "CLIENTS"])
    subheadings = ["Index Futures", "Index Call", "Index Puts", "Stock Futures", "Stock Calls", "Stock Puts"]
    for subheading in subheadings:
        table.append([subheading, subheading, subheading, subheading])
    data = ["Today", "Yesterday", "Day before yesterday"]
    for i in range(3):
        row = []
        for j in range(4):
            row.append(data[i])
        table.append(row)
    for row in table:
        print(row)

    # Render the calendar template and pass it the current date
    return render_template('get_input.html', name = request.args.get("selectdate"), table=table)

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

if __name__ == '__main__':
    app.run()