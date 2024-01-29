# heuristics are specifics
# metaheuristics are not specifics


# Problem: Find the minimum cost of the ticket to italy
peoples = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destiny = 'FCO' # roma

flights = {}

with open('flights.txt') as f:
    for row in f.readlines():
        line = row.split(',')

        flights.setdefault((line[0].strip(), line[1].strip()), [])
        flights[(line[0].strip(), line[1].strip())].append(line[2].strip())
        flights[(line[0].strip(), line[1].strip())].append(line[3].strip())
        flights[(line[0].strip(), line[1].strip())].append(int(line[4]))

print(flights[('FCO', 'LIS')])