from fuzzywuzzy import fuzz
import pandas
import requests

def match_popit(name):

    df = pandas.DataFrame.from_csv('data/popit-persons.csv')

    for popit_name in df.itertuples():
        if fuzz.token_set_ratio(name.upper(),popit_name[1].upper()) > 95:
            return popit_name

def match_popit_online(name):
    url = 'http://api.popit.sinarproject.org/en/search/persons' + \
          '?q=name:' + name
    
    r = requests.get(url)
    if r.json()['results']:
        return r.json()['results'][0]
    else:
        return None
