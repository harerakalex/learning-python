
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

import requests_with_caching

def get_movies_from_tastedive(movie_name):
    baseurl="https://tastedive.com/api/similar"
    d = {}
    d['q'] = movie_name
    d["type"]= "movies"
    d["limit"] = "5"
    
    result = requests_with_caching.get(baseurl, params=d)
    return result.json()

def extract_movie_titles(movies):
    return [movie['Name'] for movie in movies['Similar']['Results']]

def get_related_titles(movies):
    t_movies = []
    res = []
    for movie in movies:
        t_movies.append(extract_movie_titles(get_movies_from_tastedive(movie)))
    for list in t_movies:
        for m in list:
            if m not in res:
                res.append(m)
    return res

def get_movie_data(movie_name):
    baseurl="http://www.omdbapi.com/"
    d = {}
    d['t'] = movie_name
    d["r"]= "json"
    
    result = requests_with_caching.get(baseurl, params=d)
    return result.json()

def get_movie_rating(movies):
    strRanting=""
    for rantingList in movies["Ratings"]:
        if rantingList["Source"]== "Rotten Tomatoes":
            strRanting = rantingList["Value"]
    if strRanting != "":
        ranting = int(strRanting[:2])
    else: ranting = 0
    return ranting

def get_sorted_recommendations(listMovieTitle):
    listMovie= get_related_titles(listMovieTitle)
    listMovie= sorted(listMovie, key = lambda movieName: (get_movie_rating(get_movie_data(movieName)), movieName), reverse=True)
    
    return listMovie