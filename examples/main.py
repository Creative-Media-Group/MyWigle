from mywigle import MyWigleClient

client = MyWigleClient(user="USER", key="KEY")
print(client.network_geocode(addresscode="London"))
