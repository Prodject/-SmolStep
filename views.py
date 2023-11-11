from flask import Flask, render_template, request
from init import *


def home():
    return render_template("index.html")


def routes():
    return render_template("route.html")


def contact():
    return render_template("contact.html")


def report():
    return render_template("report.html")


def map():
    start_name = request.form.get("input_1111")
    if start_name is None:
        start_name = "Проспект Гагарина, 1, город Смоленск, Россия"
    print(start_name)
    finish_name = request.form.get("input_2222")
    if finish_name is None:
        finish_name = "улица Соболева, 1, город Смоленск, Россия"
    print(finish_name)

    points = build_geocode(start_name, finish_name)
    m = build_path(MY_GRAPH.G, points[0], points[1], "length")
    my_map = m.get_root().render()
    return render_template("map.html", table=my_map)
