# heuristics are specifics
# metaheuristics are not specifics
import sys
import typing

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
        flights[(line[0].strip(), line[1].strip())].append((line[2].strip(), line[3].strip(), int(line[4])))


def get_price(schedule: typing.List[int]) -> None:
    flight_id: int = -1
    price: int = 0
    for index in range(len(schedule) // 2):
        country_name = peoples[index][0]
        origin = peoples[index][1]
        flight_id += 1
        flight_to = flights[(origin, destiny)][schedule[flight_id]]
        price += flight_to[2]
        flight_id += 1
        flight_from = flights[(destiny, origin)][schedule[flight_id]]
        price += flight_from[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (country_name, origin, flight_to[0], flight_to[1], flight_to[2],
                                                    flight_from[0], flight_from[1], flight_from[2]))
    print(f"Total Price: ${price}")


if __name__ == '__main__':
    # formato de solucao. Num pessoas * 2, pois sao ida e volta
    # a cada posicao indica a cidade, [ida,volta]
    schedule_simulation = [1, 0, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
    get_price(schedule_simulation)
