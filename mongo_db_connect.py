import pymongo
import json
import requests
from pymongo import MongoClient
import time
import datetime

def get_range(lst, n):
    # Find the index of n in the list
    index = lst.index(n)

    # Get the 10 numbers before n
    start = max(0, index - 10)
    before = lst[start:index]

    # Get the 10 numbers after n
    end = min(len(lst), index + 11)
    after = lst[index+1:end]

    # Return the combined list
    return before + [n] + after

# index_dict = {
#         "NIFTY": {"slicer": 25, "lot_size": 50},
#         "BANKNIFTY": {"slicer": 100, "lot_size": 25},
#         "FINNIFTY": {"slicer": 25, "lot_size": 50},
#         "USDINR": {
#             "slicer": 0.1250,
#             "lot_size": 1,
#         },  #  USDINR is leveraged for 1000 USD for 1 Qty
#     }

index_dict = {
        "NIFTY": {"slicer": 25, "lot_size": 50},
        "BANKNIFTY": {"slicer": 100, "lot_size": 25},
        "FINNIFTY": {"slicer": 25, "lot_size": 50},
        "USDINR": {"slicer": 0.1250,"lot_size": 1},
        "CRUDEOIL":{"slicer": 25, "lot_size": 1},
        "NATURALGAS":{"slicer": 2.5, "lot_size": 1}
}


class fetch_for_indices():
    def __init__(self, index):
        self.index = index
        self.atm_slicer = index_dict[index]["slicer"]
        self.lot_size = index_dict[index]["lot_size"]
        # ## for connecting to mongodb
        # self.data = {}
        # client = MongoClient("mongodb://localhost:27017/")
        # db = client[f"{self.index}_daily_oi"]
        # collection = db[f"{self.index}_oi_collection"]
        # fifth_document = collection.find().skip(4).limit(1)
        # # docu = db.getLastInsertedDocument.find({}).sort({'_id',pymongo.ASCENDING}).limit(1)[0]
        # docu = collection.find().sort("_id", -1).limit(1)
        # self.data = [doc for doc in docu][0]

        # for fetching directly from nse
        url = f"https://www.nseindia.com/api/option-chain-indices?symbol={index}"
        headers = headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }
        response = requests.get(url, headers=headers)

        while response.status_code != 200:
            response = requests.get(url, headers=headers)
            time.sleep(1)

        content = response.content
        content_decoded = content.decode('utf-8')
        dictionary_content_decoded = json.loads(content_decoded)
        self.data=dictionary_content_decoded


        self.time = self.data['records']['timestamp']

# selecting +- 10 strike_prices near the atm

    def fetch(self):
        return (self.data['records']['underlyingValue'], self.data['filtered']['CE']['totOI'], self.data['filtered']['PE']['totOI'])
    def plot_data(self):
        strikesPrices = self.data['records']['strikePrices']
        expiry = self.data['records']['expiryDates'][0]
        call_oi = []
        put_oi = []
        call_change_oi = []
        put_change_oi = []
        call_volume=[]
        put_volume=[]
        f_strikes = []
        spot = self.data['records']['underlyingValue']
        for item in strikesPrices:
            if abs(item - float(spot)) < self.atm_slicer:
                atm=item
        self.near_atm_strikes = get_range(strikesPrices, atm)
        for item in self.data["filtered"]["data"]:
            if item["strikePrice"] in self.near_atm_strikes:
                if item["expiryDate"] == expiry:
                    f_strikes.append(item["strikePrice"])
                    if "CE" in item.keys():
                        call_oi.append(item["CE"]["openInterest"])
                        call_change_oi.append(item["CE"]["changeinOpenInterest"])
                        call_volume.append(item["CE"]["totalTradedVolume"])

                    else:
                        call_oi.append(0)
                        call_change_oi.append(0)
                        call_volume.append(0)
                    if "PE" in item.keys():
                        put_oi.append(item["PE"]["openInterest"])
                        put_change_oi.append(item["PE"]["changeinOpenInterest"])
                        put_volume.append(item['PE']['totalTradedVolume'])
                    else:
                        put_oi.append(0)
                        put_change_oi.append(0)
                        put_volume.append(0)
                else:
                    pass
            else:
                pass
        
        return (strikesPrices, f_strikes, call_oi, put_oi, call_change_oi, put_change_oi, call_volume, put_volume)

class fetch_for_commodity():
    def __init__(self, index):
        self.index = index
        # client = MongoClient("mongodb://localhost:27017/")
        # db = client[f"{self.index}_daily_oi"]
        # collection = db[f"{self.index}_oi_collection"]
        # self.fifth_document = collection.find().skip(4).limit(1)
        self.url = "https://www.mcxindia.com/backpage.aspx/GetOptionChain"
        self.body = {"Commodity": "CRUDEOIL", "Expiry": "17JAN2023"}
        self.headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }
        self.response = requests.post(self.url, json=self.body)
        while self.response.status_code != 200:
            self.response = requests.get(self.url, headers=self.headers)
        self.content = self.response.content
        self.content_decoded = self.content.decode('utf-8')
        self.dictionary_content_decoded = json.loads(self.content_decoded)
        # self.docu = collection.find().sort("_id", -1).limit(1)
        self.data = self.dictionary_content_decoded
        # self.data = [doc for doc in self.docu][0]
        self.datetime = int(self.data['d']['Summary']['AsOn'][6:-5])
        # self.last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.datetime))

    def fetch(self):
         return self.data