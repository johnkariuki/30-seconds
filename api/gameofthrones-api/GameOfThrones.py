#!/usr/bin/env python2

import urllib2
import json
base_url = "http://www.anapioficeandfire.com/api/characters?page={}&pageSize=50"

max_page = 43

names = []
game_thrones = {"Game Of Thrones": names}

for i in range(1, max_page + 1):
    url = base_url.format(i)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    response = opener.open(url)

    actors = json.loads(response.read())

    for actor in actors:
        name = actor["name"]
        if actor["playedBy"] and name != "":
            if name not in names:
                names.append(actor["name"])
                print actor["name"]

if len(names):
    print "Done downloading names!!"

    file_name = "game_thrones_actors.json"
    print "Writing to ", file_name
    with open(file_name, 'wt') as fw:
        fw.write(json.dumps(game_thrones, sort_keys=True, indent=4))


else:
    print "No Names found"


print "Done Writing!!!"
