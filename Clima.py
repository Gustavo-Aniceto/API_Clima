import requests

weather_url = "https://wttr.in/São+Paulo"
try:
    response = requests.get(weather_url)
    data = response.text

    if response.status_code == 200:
        print(data)
    else:
        print("Não foi possível")

except Exception as e:
    print(f"Erro API: {e}")
