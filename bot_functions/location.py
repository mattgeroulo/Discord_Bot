from dotenv import load_dotenv
import googlemaps
import os
from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen


def get_location(name):

    if "me" in name.lower():

        reponse = urlopen("http://ipinfo.io/json")
        data = json.load(reponse)

        lst = []

        for i in data['loc'].split(','):
            i = float(i)
            lst.append(i)
        return tuple(lst)

    else:
      # call the client to get list of all locations of latitude and longitude
        location = Nominatim(user_agent="GetLocation")
        # call geocode to for name
        get_loc = location.geocode("{}".format(name))

        if get_loc == None:
            return "invalid"
        # return location of place
        return (get_loc.latitude, get_loc.longitude)


def milesToMeter(miles):
    try:
        return miles*1_609.344
    except:
        return 0


def find_places_nearby(location, search_string, preference):

    load_dotenv()

    map_client = googlemaps.Client(os.getenv("token"))
    print(location)
    loc = get_location(location)
    if loc == "invalid":
        return "invalid location"

    distance = milesToMeter(25)
    blist = []

   # finding places ranked by preference (popularity by default)
    if preference.lower() == "popularity":
        response = map_client.places_nearby(
            location=loc,
            keyword=search_string,
            name=search_string,
            radius=distance
        )
    elif preference.lower() == "distance":
        response = map_client.places_nearby(
            location=loc,
            keyword=search_string,
            name=search_string,
            rank_by='distance'
        )
    else:
        return "invalid preference"

    # make final list to store the results in nice format
    # dictionary with key as name, list as phone number and rating as value
    final_list = {}

    blist.extend(response.get('results'))

    if len(blist) == 0:
        return "No results found / Invalid search type"
    for i in range(5):

        final_list[blist[i]["name"]] = blist[i]["rating"]
        response = map_client.place(
            place_id=blist[i]["place_id"],
            fields=['international_phone_number']
        )
        phone_num = response.get('result')

        if len(phone_num) == 0:
            final_list[blist[i]["name"]] = ('None', blist[i]["rating"])
        else:
            final_list[blist[i]["name"]] = (
                phone_num['international_phone_number'], blist[i]["rating"])
    result_string = search_string + " "

    if preference == "popularity" and location != "me":
        result_string += "in"
    else:
        result_string += "near"

    if location == "me":
        result_string = result_string + " " + "you" + " " + "are: \n"
    else:
        result_string = result_string + " " + location + " " + "are \n"
    i = 1
    for place in final_list.keys():

        result_string += str(i) + ". " + place + ", " + "Phone: " + \
            final_list[place][0] + ", " "Rating: " + \
            str(final_list[place][1]) + ".\n"

        i += 1
    return result_string
