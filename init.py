import folium as fm
import networkx as nx
import osmnx as ox
from geopy.distance import geodesic
from tqdm import tqdm


place = "г Смоленск, Смоленская область, Россия"  # город для которого нужен граф
G = ox.graph_from_place(place, network_type="walk")


class Graph:
    def __init__(self, G):
        self.G = G


MY_GRAPH = Graph(G)


def build_geocode(name1=None, name2=None):  # функция для перевода адрессов в геокод (lat, lon)
    assert name1 is not None, "1st name is None"
    assert name2 is not None, "2nd name is None"

    place1 = ox.geocode(
        name1
    )  # метод перевода из коробки для карт OSM(Open Street Map)
    place2 = ox.geocode(
        name2
    )  # метод перевода из коробки для карт OSM(Open Street Map)

    return place1, place2


def build_path(graph=None, point1=(), point2=(), mode="time"):  # функция для отрисовки карты
    assert graph is not None, "Your graph is NoneType object"
    assert len(point1) == 2, "1st point hasn`t 2 coordinates"
    assert len(point2) == 2, "2nd point hasn`t 2 coordinates"

    start_node = ox.nearest_nodes(
        graph, point1[1], point1[0]
    )  # для полученных координат находится ближайшая нода
    finish_node = ox.nearest_nodes(
        graph, point2[1], point2[0]
    )  # для полученных координат находится ближайшая нода

    route = nx.shortest_path(
        graph, start_node, finish_node, weight=mode
    )  # строится короткий путь по Алгоритму Дейкстры по атрибуту mode(параметр функции)

    shortest_route_map = ox.plot_route_folium(graph, route)  # отрисовка карты

    fm.TileLayer("openstreetmap").add_to(shortest_route_map)  # добавление стиля

    # маркеры начала и конца пути
    start_marker = fm.Marker(
        location=point1, popup="Начало маршрута", icon=fm.Icon(color="green")
    )

    finish_marker = fm.Marker(
        location=point2, popup="Конец маршрута", icon=fm.Icon(color="red")
    )

    # добавление их на карту
    start_marker.add_to(shortest_route_map)
    finish_marker.add_to(shortest_route_map)

    # цикл на добавление синих маркеров с центрами достопримечательностей(чтобы понять как идёт путь)
    # for i in range(gdf.shape[0]):
    #     if i == 100:
    #         break
    #     marker = fm.Marker(
    #         location=(Y[i], X[i]), popup=gdf.name[i], icon=fm.Icon(color="blue")
    #     )
    #     marker.add_to(shortest_route_map)

    return shortest_route_map
