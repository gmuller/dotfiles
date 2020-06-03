#!/usr/bin/env python

import tmdbsimple as tmdb
import csv
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file-name", dest="filename", help="Where to write the output file", default="output.csv")
parser.add_argument("-i", "--movie-id", dest="movie_id", help="Movie ID to link to")
parser.add_argument("-m", "--movie-name", dest="movie_name", help="Movie name to link to")
args = parser.parse_args()


filename = args.filename
tmdb.API_KEY = os.environ['TMDB_KEY']
seen_list_id = os.environ['TMDB_SEEN_ID']
a = tmdb.Lists(seen_list_id)

movie_id = args.movie_id

if args.movie_name != None:
    search = tmdb.Search()
    response = search.movie(query=args.movie_name);
    for s in search.results:
        print(s['id'], s['title'], s['release_date'], s['popularity'])
    movie_id = input("\nWhich Movie ID did you mean?\n")

movie = tmdb.Movies(movie_id)

for c in movie.credits()['cast']:
    print(c['id'], c['name'])

excluded_collaborator = input("\nExclude a Collaborator?\n")

response = movie.info()
list_response = a.info()
seen = set()
[seen.add(movie['id']) for movie in a.items]

cache = {}
for c in movie.credits()['cast']:
    person = tmdb.People(c['id'])
    response = person.info
    for p in person.movie_credits()['cast']:
        if p['vote_count'] < 40: continue
        if p['id'] in seen: continue
        if p['id'] in cache:
            cache[p['id']]['collaborators'].add(c['name'])
        else:
            p['collaborators'] = {c['name']}
            cache[p['id']] = p;

with open(filename, 'w') as csv_file:
    fields = ['id', 'title', 'collaborators', 'vote_average', 'vote_count', 'release_date', 'overview']
    writer = csv.DictWriter(csv_file, fieldnames=fields, extrasaction='ignore')
    writer.writeheader()
    for movie in sorted(list(cache.values()), key=lambda x: x['vote_average'], reverse=True):
        writer.writerow(movie)
        #print(str(movie['id']) + ", " + movie['title'] + ", " + str(movie['collaborators']) + ", " + str(movie['vote_average']))

print("complete")
