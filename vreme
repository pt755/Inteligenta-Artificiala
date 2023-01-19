import requests
API_KEY = "1c2917dc89ebf80f20bf94cc650ab705"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Introdu numele orasului: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    vreme=data['weather'][0]['description']
    temperature = round(data["main"]["temp"],2)
    humidity = (data["main"]["humidity"])
    with open('Weather text.txt', 'a') as f:
        print("Vremea: ", vreme, file=f)
        print("Temperatura: ", temperature, "Â°C", file=f)
        print("Umiditate: ", humidity, "%", file=f)
else:
    print("Am intampinat o eroare")
    
