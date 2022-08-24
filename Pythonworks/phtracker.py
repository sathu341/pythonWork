import phonenumbers
from  mynumber import number
import folium


from  phonenumbers import geocoder
ch_nmber=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))
yourlocation=geocoder.description_for_number(ch_nmber,"en");
from phonenumbers import carrier
service_nmber=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))
key='1a8c3714e1894821892a481bb7bdfb16'
from  opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)
query=str(yourlocation)
results=geocoder.geocode(query)
print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourlocation).add_to((myMap))
myMap.save("mylocation.html")

