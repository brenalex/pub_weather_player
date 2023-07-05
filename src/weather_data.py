# Importing libraries
import requests
import config


def init_weather(city):
    ret_data = []
    API_Key = config.api_key
    city_name = city

    # Constructing the API URL path
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric"

    # Making a get request to the API
    response = requests.get(url)

    # Converting JSON response to a dictionary
    res = response.json()

    # Uncomment the next line to see all
    # data that are fetched from the API
    #print(res)
    if res["cod"] != "404":
        data = res["main"]

        # Storing the temp and description data
        live_temperature = data["temp"]
        desc = res["weather"]
        # Storing the weather description
        weather_description = desc[0]["main"]
        ret_data.append(weather_description)
        ret_data.append(live_temperature)
        
    return ret_data

def desc2num(desc):
    if(desc == "Clear"):
        num = 0
    elif(desc == "Clouds"):
        num = 1
    elif(desc == "Rain" or desc == "Drizzle"):
        num = 2
    elif(desc == "Snow"):
        num = 3
    else:
        num = 4
    return num
