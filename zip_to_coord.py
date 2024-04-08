# from geopy.geocoders import Nominatim

def ZipToCoord (zipcode):
    geolocator = Nominatim(user_agent="zipcode_to_lat_long")
    location = geolocator.geocode(zipcode)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
