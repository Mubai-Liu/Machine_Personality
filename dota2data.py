import dota2api
import requests
import pprint
import json
r = requests.get("https://api.opendota.com/api/matches/74170846")

pprint.pprint(json.loads(r.text))

 r = requests.get("https://api.opendota.com/api/matches/5258062710")

 pprint.pprint(json.loads(r.text))


api = dota2api.Initialise("54699EC1DAEC662D994DAADE57148354", raw_mode = True)


api.get_heroes()


api.get_match_details(match_id = 5258276949)

api.get_player_summaries(76561198140336085)