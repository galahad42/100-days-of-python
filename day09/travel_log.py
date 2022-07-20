travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country" : "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities_list):
    global travel_log
    travel_log +=   [
    {   
        "country": country,
        "visits" : visits,
        "cities" : cities_list
    }
                    ]


add_country = input("Please input the country: ")
add_visits  = int(input("Please input number of visits to the country: "))
add_cities  = input("Please input the cities visited separated by a single space: ")
add_cities = add_cities.split(" ")

add_new_country(add_country, add_visits, add_cities)
print(travel_log)
