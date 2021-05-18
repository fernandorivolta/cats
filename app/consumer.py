import requests

x = requests.get('https://api.thecatapi.com/v1/breeds', headers={'x-api-key': '968f68ea-0fac-43f8-825a-99fed57586ed'})
for i in x.json():
    print(i)
    print(" ")