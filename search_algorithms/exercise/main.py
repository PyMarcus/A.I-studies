"""Ir de Porto União à Curitiba, usando a heurística de
linhas retas passada"""
from dataclasses import dataclass


@dataclass
class City:
    def __init__(self, name: str, distance: int) -> None:
        """Nome e distancia, em linha reta(heuristica)"""
        self.name = name
        self.distance = distance
        self.visited = False
        self.neighboring_cities = []

    def add_a_neighbor_city(self, city) -> None:
        self.neighboring_cities.append(city)


@dataclass
class NeighborCity:
    def __init__(self, city: City, distance: int) -> None:
        """Cidade vizinha e sua distancia"""
        self.city = city
        self.distance = distance
        self.distance_a_star = self.city.distance + self.distance


class Graph:
    portoUniao = City("Porto União", 203)
    pauloFrontin = City("Paulo Frontin", 172)
    canoinhas = City("Canoinhas", 141)
    irati = City("Irati", 139)
    palmeira = City("Palmeira", 59)
    campoLargo = City("Campo Largo", 27)
    curitiba = City("Curitiba", 0)
    balsaNova = City("Balsa Nova", 41)
    araucaria = City("Araucária", 23)
    saoJose = City("São José dos Pinhais", 13)
    contenda = City("Contenda", 39)
    mafra = City("Mafra", 94)
    tijucas = City("Tijucas do Sul", 56)
    lapa = City("Lapa", 74)
    saoMateus = City("São Mateus do Sul", 123)
    tresBarras = City("Três Barras", 131)

    portoUniao.add_a_neighbor_city(NeighborCity(pauloFrontin, 46))
    portoUniao.add_a_neighbor_city(NeighborCity(canoinhas, 78))
    portoUniao.add_a_neighbor_city(NeighborCity(saoMateus, 87))

    pauloFrontin.add_a_neighbor_city(NeighborCity(portoUniao, 46))
    pauloFrontin.add_a_neighbor_city(NeighborCity(irati, 75))

    canoinhas.add_a_neighbor_city(NeighborCity(portoUniao, 78))
    canoinhas.add_a_neighbor_city(NeighborCity(tresBarras, 12))
    canoinhas.add_a_neighbor_city(NeighborCity(mafra, 66))

    irati.add_a_neighbor_city(NeighborCity(pauloFrontin, 75))
    irati.add_a_neighbor_city(NeighborCity(palmeira, 75))
    irati.add_a_neighbor_city(NeighborCity(saoMateus, 57))

    palmeira.add_a_neighbor_city(NeighborCity(irati, 75))
    palmeira.add_a_neighbor_city(NeighborCity(saoMateus, 77))
    palmeira.add_a_neighbor_city(NeighborCity(campoLargo, 55))

    campoLargo.add_a_neighbor_city(NeighborCity(palmeira, 55))
    campoLargo.add_a_neighbor_city(NeighborCity(balsaNova, 22))
    campoLargo.add_a_neighbor_city(NeighborCity(curitiba, 29))

    curitiba.add_a_neighbor_city(NeighborCity(campoLargo, 29))
    curitiba.add_a_neighbor_city(NeighborCity(balsaNova, 51))
    curitiba.add_a_neighbor_city(NeighborCity(araucaria, 37))
    curitiba.add_a_neighbor_city(NeighborCity(saoJose, 15))

    balsaNova.add_a_neighbor_city(NeighborCity(curitiba, 51))
    balsaNova.add_a_neighbor_city(NeighborCity(campoLargo, 22))
    balsaNova.add_a_neighbor_city(NeighborCity(contenda, 19))

    araucaria.add_a_neighbor_city(NeighborCity(curitiba, 37))
    araucaria.add_a_neighbor_city(NeighborCity(contenda, 18))

    saoJose.add_a_neighbor_city(NeighborCity(curitiba, 15))
    saoJose.add_a_neighbor_city(NeighborCity(tijucas, 49))

    contenda.add_a_neighbor_city(NeighborCity(balsaNova, 19))
    contenda.add_a_neighbor_city(NeighborCity(araucaria, 18))
    contenda.add_a_neighbor_city(NeighborCity(lapa, 26))

    mafra.add_a_neighbor_city(NeighborCity(tijucas, 99))
    mafra.add_a_neighbor_city(NeighborCity(lapa, 57))
    mafra.add_a_neighbor_city(NeighborCity(canoinhas, 66))

    tijucas.add_a_neighbor_city(NeighborCity(mafra, 99))
    tijucas.add_a_neighbor_city(NeighborCity(saoJose, 49))

    lapa.add_a_neighbor_city(NeighborCity(contenda, 26))
    lapa.add_a_neighbor_city(NeighborCity(saoMateus, 60))
    lapa.add_a_neighbor_city(NeighborCity(mafra, 57))

    saoMateus.add_a_neighbor_city(NeighborCity(palmeira, 77))
    saoMateus.add_a_neighbor_city(NeighborCity(irati, 57))
    saoMateus.add_a_neighbor_city(NeighborCity(lapa, 60))
    saoMateus.add_a_neighbor_city(NeighborCity(tresBarras, 43))
    saoMateus.add_a_neighbor_city(NeighborCity(portoUniao, 87))

    tresBarras.add_a_neighbor_city(NeighborCity(saoMateus, 43))
    tresBarras.add_a_neighbor_city(NeighborCity(canoinhas, 12))


class AStar:
    def __init__(self, destiny: City) -> None:
        self.destiny = destiny

    def search(self, start_point: City) -> None:
        print(f"Passando por {start_point.name}")
        start_point.visited = True
        if start_point.name == self.destiny.name:
            return
        for n in start_point.neighboring_cities:
            if not n.city.visited:
                n.city.visited = True

        ordered = sorted(start_point.neighboring_cities, key=lambda i: i.distance_a_star)
        city = ordered[0].city
        self.search(city)
        return


if __name__ == '__main__':
    graph = Graph()
    a = AStar(graph.curitiba)
    a.search(graph.portoUniao)
