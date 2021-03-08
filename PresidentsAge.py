import datetime
from dateutil import parser

all_presidents = []

with open("presidents.txt") as PRES:
    for rec in PRES:
        _, last_name, first_name, birthday, deathday, *_ = rec.split(":")

        if(deathday == 'NONE'):
            continue
        birth_date = parser.parse(birthday)
        death_date = parser.parse(deathday)
        deltatime = death_date - birth_date
        full_name = '{} {}'.format(first_name, last_name)

        all_presidents.append((deltatime, full_name))

for deltatime, name in sorted(all_presidents):
    print(name, "lived", int(deltatime.days/365), 'years')
