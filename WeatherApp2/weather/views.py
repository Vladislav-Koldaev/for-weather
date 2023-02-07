from django.shortcuts import render
import requests

def index(request):
    appid='4d1a908aa1d527f34f695cdff47b27fc'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid="+appid

    city='London'
    res = requests.get(url.format(city))

    print(res.text)

    return render(request, 'weather/index.html')



