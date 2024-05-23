import requests
import json
import sys
import re

def main():
    country_from_user = input('Country: ')
    comp = league_getter(country_from_user)
    best_team = team_getter(comp)
    print(best_team)
    print(result_compare(best_team))

def team_getter(league):

    uri = f'https://api.football-data.org/v4/competitions/{league}/standings'
    headers = { 'X-Auth-Token': 'af048cff09194199b5317c0a43458178' }

    response = requests.get(uri, headers=headers)
    o = response.json()
    a = o['standings']
    b = a[0]
    c = b['table']
    d = c[0]
    e = d['team']
    f = e['shortName']
    return (f'It is {f}!')

def league_getter(s):
    countries = {
        'germany': 'BL1',
        'netherlands': 'DED',
        'brasil': 'BSA',
        'spain': 'PD',
        'france': 'FL1',
        'portugal': 'PPL',
        'italy': 'SA',
        'england': 'PL',
    }
    country = s.strip().lower()
    if country in countries:
        league = countries[country]
        return league
    else:
        sys.exit('Competition is not available, sorry!')


def result_compare(answer):
    matches = re.search(r'It is (.+)!', answer, re.IGNORECASE)
    team = matches.group(1)
    match team:
        case 'Man City'|'PSG'|'Bayern'|'AC Milan'|'AFC Ajax'|'Palmeiras'|'FC Porto'|'Real Madrid':
            return ('Again!')
        case _:
            return ('After some time! Finally!')

if __name__ == "__main__":
    main()