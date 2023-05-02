# NSE_open_interest

#This is open source web app developed in python by Manish Lamba(Linkedin: https://www.linkedin.com/in/manish--lamba/, Gmail: Manishlamba002@gmail.com) to show open intereset and change in open interest for selected securities

You can use this repo to show live open interest/ change in live open interest for indices: 'NIFTY', 'BANKNIFTY', 'FINNIFTY' and currency: 'USDINR' and commodities: 'CRUDEOIL', 'NATURALGAS'. You can alseo change the url and also include other stock(like 'RELIANCE','SBIN') and indices.

Find below the Useful url's that you can include to fetch OI data:
1. Indices= https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY  #Replace 'NIFTY" with other indices to fetch data for that index, e.g. 'BANKNIFTY', 'FINNIFTY', 'MIDCPNIFTY'
2. USDINR= https://www.nseindia.com/api/option-chain-currency?symbol=USDINR #Replace 'USDINR' with other cuurrency to fetch data for that currency, e.g. 'GBPINR', 'EURINR', 'JPYINR'
3. CrudeOil= Post_Api: https://www.mcxindia.com/backpage.aspx/GetOptionChain, Payload: {'Commodity':'CRUDEOIL','Expiry':'15FEB2023'}  #change payload Expiry with current Expiry date
4. NaturalGas= https://www.mcxindia.com/backpage.aspx/GetOptionChain, Payload: {'Commodity':'NATURALGAS','Expiry':'21FEB2023'} #Change payload Expiry with current Expiry date
5. Equities= https://www.nseindia.com/api/option-chain-equities?symbol=ADANIENT #Replace 'ADANIENT' with other stock name to fetch data for that stock, e.g. 'RELIANCE', 'HDFC' or can also choose from FNO Symbol list
6. FNO Symbol list= https://archives.nseindia.com/content/fo/fo_mktlots.csv
7. Clearing holidays= https://www.nseindia.com/api/holiday-master?type=clearing
8. Trading holidays= https://www.nseindia.com/api/holiday-master?type=trading
9. nse events= https://www.nseindia.com/api/event-calendar
10. nse blockdeal= https://nseindia.com/api/block-deal
11. market status= https://nseindia.com/api/marketStatus
12. nse fiidii daily cash data= https://www.nseindia.com/api/fiidiiTradeReact


#Feel free to drop any suggestions
#This is the first version of the web app I have developed, and also hosted at www.Bullopear.com, You can also visit this website to view live OI
