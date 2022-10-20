
# import googlemaps

# gmaps=googlemaps.Client(key='AIzaSyAwWfmMfjjrQdM6K6xa5ctZjbFadQXQibE')

# geocode_result=gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')



import  requests  
# url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?query=restaurants%20in%20Urbana&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Ctypes&key=AIzaSyAwWfmMfjjrQdM6K6xa5ctZjbFadQXQibE"

# url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants%20in%20Champaign&fileds=formatted_address%2Cname%2rating&key=AIzaSyAwWfmMfjjrQdM6K6xa5ctZjbFadQXQibE"

url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJxZkDMBTXDIgRbMTuiFFufRk&fields=name%2Crating%2Cformatted_phone_number%2Copening_hours%2Creviews&key=AIzaSyAwWfmMfjjrQdM6K6xa5ctZjbFadQXQibE"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
