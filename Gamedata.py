
matches = pd.DataFrame()
match_id = [5264233901,5263347490]
for i in match_id:
    print(i)
    matches = matches.append(get_match(i))
api = dota2api.Initialise("54699EC1DAEC662D994DAADE57148354", raw_mode = True)
pd.DataFrame(api.get_match_details(match_id)['players'])

def get_match(match_id):
    return pd.DataFrame(api.get_match_details(match_id))


# 76561198140336085 - 76561197960265728
pd.DataFrame(api.get_match_history(76561198140336085))




url = "https://api.opendota.com/api/matches/" + str(match_id)
requests.get(url)

json.loads(requests.get(url).text)


!pip install -U dota2
import dota2
dota.request_match_details(match_id)