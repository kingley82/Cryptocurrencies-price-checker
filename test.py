import cryptoprice as cp

Main = cp.Crypto('BTC')
price = Main.check()
print(price["data"]["amount"])
