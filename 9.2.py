
#List that has 2 dictionaries
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, visits_time, cities_list):
  #new_country = {"country": country_name, "visits": visits_time, "cities": cities_list}    or
  new_country = {}
  new_country["country"] = country_name
  new_country["visits"] = visits_time
  new_country["cities"] = cities_list

  travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)
print(travel_log[2]["cities"])
print(travel_log[2]["cities"][1])
