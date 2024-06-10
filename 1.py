import folium
from folium.plugins import AntPath

# Создание карты
route_map = folium.Map(location=[43.9, 42.7], zoom_start=8)

# Маршрутные точки
points = [
    {"name": "1. Ессентуки", "location": [44.04861, 42.86056], "time": "0 ч"},
    {"name": "2. Гора Машук", "location": [44.0425, 43.0575], "time": "1 ч"},
    {"name": "3. Озеро Гижгит", "location": [43.4581, 42.6183], "time": "2.5 ч"},
    {"name": "4. Плато Шатджатмаз", "location": [43.688, 42.709], "time": "4 ч"},
    {"name": "5. Чегемское ущелье и водопады", "location": [43.316, 43.204], "time": "6 ч"},
    {"name": "6. Водопад Девичьи Слезы", "location": [43.25, 42.7], "time": "7 ч"},
    {"name": "7. Водопад Терскол", "location": [43.2426, 42.51], "time": "7.5 ч"},
    {"name": "8. Владикавказ", "location": [43.03667, 44.66778], "time": "10 ч"},
    {"name": "9. Памятник Уастырджи", "location": [42.9833, 44.6833], "time": "10.5 ч"},
    {"name": "10. Водохранилище", "location": [43.03, 44.43], "time": "11.5 ч"},
    {"name": "11. Ессентуки", "location": [44.04861, 42.86056], "time": "13.5 ч"}
]

# Добавление маркеров на карту
for point in points:
    folium.Marker(
        location=point["location"],
        popup=f'{point["name"]} ({point["time"]})',
        tooltip=point["name"]
    ).add_to(route_map)

# Добавление линий маршрута
route_locations = [point["location"] for point in points]
AntPath(route_locations, color="blue", weight=2.5, opacity=1).add_to(route_map)

# Сохранение карты в файл
route_map.save("route_map.html")
