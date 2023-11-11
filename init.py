import folium as fm
import networkx as nx
import osmnx as ox
from geopy.distance import geodesic
import numpy as np

from tqdm import tqdm

from shapely.geometry import Point


place = "г Смоленск, Смоленская область, Россия"  # город для которого нужен граф
G = ox.graph_from_place(place, network_type="walk")


class Graph:
    def __init__(self, G):
        self.G = G


# теги для отбора геометрий
tags = {'tourism': ['attraction', 'viewpoint'],
        'leisure': ['park', 'garden'],
        'historic': ['memorial', 'yes'],
        'amenity': ['theatre', 'fountain'],
        'memorial': ['statue', 'stele', 'stone', 'war_memorial', 'bust']}


# функция ищет ближайшую точку от цетра объекта gdf(GeoDataFrame)
def fin_nearest_nodes(gdf):
    nns = {}
    imp = {}

    for i in range(gdf.shape[0]):
        obj = gdf.iloc[i, :]
        nn = ox.nearest_nodes(G, obj['geometry'].x, obj['geometry'].y)
        nns[nn] = 0.009
        imp[nn] = 1
        if not obj.historic is np.nan:
            nns[nn] /= 2
            imp[nn] += 3
        if not obj["subject:wikidata"] is np.nan or not obj["subject:wikipedia"] is np.nan:  # subject:wikipedia
            nns[nn] /= 2
            imp[nn] += 3
        if not obj["name"] is np.nan:
            nns[nn] -= 0.00125
            imp[nn] += 2

    return nns, imp


gdf = ox.geometries_from_place(place, tags=tags)  # находит из геометрии нашего графа

index_nodes = []  # список для нод
index_relations = []  # список для ребер

for i in range(gdf.shape[0]):  # прохожусь по всем объектам в gdf, если это нода то добавляю к index_nodes
    if 'node' in gdf.index[i]:
        index_nodes.append(i)
    else:
        index_relations.append(
            i)  # иначе к index_relations. В этом списке могут быть индексы объектов с типом way (тоже самое что relation)

gdf['importance'] = 1
for i in range(gdf.shape[0]):
    obj = gdf.iloc[i, :]
    if not obj['historic'] is np.nan:
        gdf.iloc[i, -1] += 3
    if not obj["subject:wikidata"] is np.nan or not obj["subject:wikipedia"] is np.nan:  # subject:wikipedia
        gdf.iloc[i, -1] += 3
    if not obj["name"] is np.nan:
        gdf.iloc[i, -1] += 2

nodes_gdf = gdf.iloc[index_nodes, :]  # дальше беру срез объектов отобранных циклом
relations_gdf = gdf.iloc[index_relations, :]  # дальше беру срез объектов отобранных циклом

# считаю центры всех достопримечательностей что нашел(на карте будут синими точками)
centroids = gdf.centroid
X = centroids.x
Y = centroids.y

mask_nodes, importance = fin_nearest_nodes(
    nodes_gdf)  # нахожу ближайшие ноды для точечных достопримечательностей (пример: статуя, памятник)


# the length unit is now `meter`
eqArea_lakeSup = relations_gdf.to_crs(epsg=6933)

# compute areas in sq meters
areas = eqArea_lakeSup.area


def set_group(area):
    return round(area ** 0.5)


# and add it as a new column to geodataframe
eqArea_lakeSup["area_m"] = np.sqrt(areas.values)
relations_gdf["area_radius"] = eqArea_lakeSup["area_m"].apply(lambda x: set_group(x))

# print some result
eqArea_lakeSup[["name","area_m"]].head()


def set_basic_attr(graph, attr, val=1):  # функция которая задаёт базовый вес

    assert val != None, "Value is NoneType object"

    for u, v, data in graph.edges(data=True):
        data[attr] = data['length'] * val


def set_edge_attr(graph, attr, mask=[]):  # функция которая задаёт вес для нод

    assert len(mask) != 0

    for i in tqdm(range(nodes_gdf.shape[0])):
        center_point = nodes_gdf.iloc[i, :]['geometry']
        radius = 3
        # Создайте геометрическую форму для окружности
        circle = Point(center_point).buffer(radius)

        # Отфильтруйте рёбра, которые пересекают окружность
        edges_to_update = []
        for u, v, data in graph.edges(data=True):
            edge_geometry = data.get('geometry', None)
            if edge_geometry is not None:
                if edge_geometry.intersects(circle):
                    edges_to_update.append((u, v, data))

        for u, v, data in edges_to_update:  # проходимся по всем рёбрам и если там есть нода из mask то меняем вес
            if u in mask and v in mask:
                data[attr] = data['length'] * min([mask[v], mask[u]])
            elif u in mask:
                data[attr] = data['length'] * mask[u]
            elif v in mask:
                data[attr] = data['length'] * mask[v]


def set_polygon_edge_attr(graph, attr, gdf=[], global_gdf=[]):  # функция которая задаёт вес для геометрий

    assert len(gdf) != 0, "Filter object has 0 length"
    assert len(global_gdf) != 0, "Filter object has 0 length"

    relation_centers = gdf.centroid
    for i in tqdm(range(gdf.shape[0])):
        center_point = relation_centers[0]
        radius = gdf.iloc[i, :]['area_radius']
        # Создайте геометрическую форму для окружности
        circle = Point(center_point).buffer(radius)

        # Отфильтруйте рёбра, которые пересекают окружность
        edges_to_update = []
        for u, v, data in graph.edges(data=True):
            edge_geometry = data.get('geometry', None)
            if edge_geometry is not None:
                if edge_geometry.intersects(circle):
                    edges_to_update.append((u, v, data))

        # Уменьшите атрибуты рёбер для отфильтрованных рёбер
        for u, v, data in edges_to_update:
            obj = global_gdf.iloc[i, :]
            w = 0.009
            if not obj.historic is np.nan:
                w /= 2
            if not obj["subject:wikidata"] is np.nan or not obj["subject:wikipedia"] is np.nan:  # subject:wikipedia
                w /= 2
            if not obj["name"] is np.nan:
                w -= 0.002
            if data[attr] == 1:
                data[attr] = data['length'] * w
            else:
                data[attr] = min([data[attr], data['length'] * w])


set_basic_attr(G, 'weight', 1)
set_edge_attr(G, 'weight', mask_nodes)
set_polygon_edge_attr(G, 'weight', relations_gdf, gdf)


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
