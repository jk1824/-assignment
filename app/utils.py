from geopy.distance import geodesic

def is_within_distance(lat1, lon1, lat2, lon2, max_km):
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    return geodesic(point1, point2).km <= max_km
