import bitcoinprice as bcp

Main = bcp.Crypto('BTC')
price = Main.check()
print(price["data"]["amount"])