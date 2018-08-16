"""
Created on Sun Feb 18 04:01:17 2018 ----------- @author: mxhfield

"""

def inflight_entertainment(flight, movies):
    dif = {}
    for k in movies:
        dif[flight - k] = k
        
    for v in movies:
        if dif.get(v) and dif.get(v) != v:
            return True, str(v) +'m first movie + '+ str(dif[v]) + \
                            'm second movie = '+ str(flight)+'m flight'
    return False, v+' + '+ dif[v]+' = '+ flight


movies = [97,85, 90, 93, 74, 66, 57, 120, 111, 103, 81, 98]
flight = 194

#print(inflight_entertainment(flight, movies))

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_seen = set()

    for first_movie in movie_lengths:
        matching_second_movie = flight_length - first_movie
        if matching_second_movie in movie_seen:
            return True
        movie_seen.add(first_movie)

    # We never found a match, so return False
    return False
