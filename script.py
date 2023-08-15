import phonenumbers
from phonenumbers import geocoder
import folium
from dotenv import load_dotenv
import os

load_dotenv()

opencage_api_key = os.getenv("OPENCAGE_API_KEY")

user_number = input("Enter your phone number including the country code ")


# get the user number

check_num = phonenumbers.parse(user_number)

num_location = geocoder.description_for_number(check_num, "en")

print(num_location)

from phonenumbers import carrier
carrier_name = phonenumbers.parse(user_number)
print(carrier.name_for_number(carrier_name, "en"))

from opencage.geocoder import OpenCageGeocode

geocode_location = OpenCageGeocode(opencage_api_key)


query = str(num_location)
result = geocode_location.geocode(query)

latitude = result[0]["geometry"]["lat"]
longitude = result[0]["geometry"]["lng"]

print(longitude, latitude)

map_location = folium.Map(location=[latitude, longitude], zoom_start=5)
folium.Marker([latitude, longitude], popup=num_location).add_to(map_location)

map_location.save("mapLocation.html")