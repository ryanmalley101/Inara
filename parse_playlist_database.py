import csv
import json
import re

def parse_playlists(text_path):
    objects = []

    with open(text_path, 'r') as text_file:
        lines = text_file.readlines()

        for line in lines:
            items = line.split("|")
            print(items)
            group = items[1]
            song = items[3].replace("ï½œ", "|").replace('\n', "").replace("â€™", "'").replace("Â ", " ").replace("ï¼š", ":").replace("ï¼‚", r'"')

            song_in_playlist = False
            for plist in objects:
                if plist["name"] == group:
                    plist["songs"].append(song)
                    song_in_playlist = True

            if not song_in_playlist:
                objects.append({"name": group, "songs": [song]})

    return objects


if __name__ == '__main__':
    playlists_file = "playlists.txt"
    playlists = parse_playlists(playlists_file)

    with open("playlists.json", 'w') as json_file:
        json.dump(playlists, json_file, indent=4)
    print('CSV to JSON conversion complete.')
