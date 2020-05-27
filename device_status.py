from boltiot import Bolt
api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
device_id  = "BOLTXXXXXX"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response)
