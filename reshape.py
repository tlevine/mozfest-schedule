#!/usr/bin/env python
import json
import pandas

nested = json.load(open('schedule.json'))

def unnest(nested):
    for k,v in nested['schedule'].items():
        for session in v.values():
            session['track'] = k
            yield session

flat = list(unnest(nested))

json.dump(flat, open('flat.json', 'w'))
pandas.DataFrame(flat).to_csv('flat.csv', encoding = 'utf-8')
