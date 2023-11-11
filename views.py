from flask import Flask, render_template, request
from init import *


def home():
    return render_template('index.html')


def routes():
    return render_template('route.html')


def contact():
    return render_template('contact.html')


def report():
    pass


def map():
    start_name = """
    36, улица Октябрьской Революции, Ленинский район, городской округ Смоленск, 
    Смоленская область, Центральный федеральный округ, 210000, Россия
    """

    finish_name = """
    Гимназия им. Пржевальского, улица Ленина, Ленинский район, городской округ Смоленск, 
    Смоленская область, Центральный федеральный округ, 210000, Россия
    """

    points = build_geocode(start_name, finish_name)
    m = build_path(MY_GRAPH.G, points[0], points[1], "length")
    my_map = m.get_root().render()
    return render_template('map.html', table=my_map)