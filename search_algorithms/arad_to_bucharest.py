class Vertice:
    def __init__(self, city: str, distance: int) -> None:
        self.city = city
        self.distance = distance
        self.visited = False
        self.neighbors = []

    def add_neighbor(self, neighbor) -> None:
        self.neighbors.append(neighbor)

    def show_neighbor(self) -> None:
        print(f"{self.city} has a path to:")
        for neighbor in self.neighbors:
            print(f"{neighbor} - {neighbor.distance}km")


class Neighbor:
    def __init__(self, city: Vertice, distance: int) -> None:
        self.city = city
        self.distance = distance

    def __str__(self) -> str:
        return f"City {self.city.city}"


class Graph:
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.add_neighbor(Neighbor(zerind, 75))
    arad.add_neighbor(Neighbor(sibiu, 140))
    arad.add_neighbor(Neighbor(timisoara, 118))

    zerind.add_neighbor(Neighbor(arad, 75))
    zerind.add_neighbor(Neighbor(oradea, 71))

    oradea.add_neighbor(Neighbor(zerind, 71))
    oradea.add_neighbor(Neighbor(sibiu, 151))

    sibiu.add_neighbor(Neighbor(oradea, 151))
    sibiu.add_neighbor(Neighbor(arad, 140))
    sibiu.add_neighbor(Neighbor(fagaras, 99))
    sibiu.add_neighbor(Neighbor(rimnicu, 80))

    timisoara.add_neighbor(Neighbor(arad, 118))
    timisoara.add_neighbor(Neighbor(lugoj, 111))

    lugoj.add_neighbor(Neighbor(timisoara, 111))
    lugoj.add_neighbor(Neighbor(mehadia, 70))

    mehadia.add_neighbor(Neighbor(lugoj, 70))
    mehadia.add_neighbor(Neighbor(dobreta, 75))

    dobreta.add_neighbor(Neighbor(mehadia, 75))
    dobreta.add_neighbor(Neighbor(craiova, 120))

    craiova.add_neighbor(Neighbor(dobreta, 120))
    craiova.add_neighbor(Neighbor(pitesti, 138))
    craiova.add_neighbor(Neighbor(rimnicu, 146))

    rimnicu.add_neighbor(Neighbor(craiova, 146))
    rimnicu.add_neighbor(Neighbor(sibiu, 80))
    rimnicu.add_neighbor(Neighbor(pitesti, 97))

    fagaras.add_neighbor(Neighbor(sibiu, 99))
    fagaras.add_neighbor(Neighbor(bucharest, 211))

    pitesti.add_neighbor(Neighbor(rimnicu, 97))
    pitesti.add_neighbor(Neighbor(craiova, 138))
    pitesti.add_neighbor(Neighbor(bucharest, 101))

    bucharest.add_neighbor(Neighbor(fagaras, 211))
    bucharest.add_neighbor(Neighbor(pitesti, 101))
    bucharest.add_neighbor(Neighbor(giurgiu, 90))


if __name__ == '__main__':
    graph: Graph = Graph()
    graph.arad.show_neighbor()
