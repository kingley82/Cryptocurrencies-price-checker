import requests
import json

'''Contacts:
TG - @a352642
VK - https://vk.com/erg374728'''
'''CRYPTOCURRENCY DESIGNATIONS
BTC - Bitcoin
LTC - Litecoin
ETH - Etherium
BNB - Binance coin
LINK - Chainlink
CRO - Crypto.com coin
For more crypto - https://www.coinbase.com/price'''

class Crypto:
	def __init__(self, currency):
		self.currency = currency
		self.api = f'https://api.coinbase.com/v2/prices/{currency}-USD/spot/'
	def check(self):
		response = requests.get(self.api)
		data = response.json()
		try:
			error = data["errors"]
		except:
			return data
		else:
			raise AttributeError(f"No currency named '{self.currency}'")