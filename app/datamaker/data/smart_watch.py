from faker import Faker
import random

fake = Faker()

_FEATURES = {
    "seller": ["Rozetka", "Other"],
    "brand": ["Apple", "Huawei", "Nokia", "Meizu", "OnePlus", "Samsung", "Sony", "Xiaomi"],
    "RAM": ["1Gb", "2Gb"],
    "OS": ["IOS", "Android", "BlackBerry"],
    "wireless_technology": ["Bluetooth", "Ethernet", "Serial", "USB", "Wireless"],
    "other_features": ["Alarm Clock", "Camera", "GPS", "Mail", "Music player"],
    "fitness_features": ["Activity tracker", "blood pressure monitor", "calorie tracker", "pedometer"]
}


def _get_features():
    return {name: random.choice(values) for (name, values) in _FEATURES.items() if type(values) in (list, tuple)}


def get():
    base = {}
    base['category'] = 'Smart watch'
    base['price'] = random.randrange(800, 65000)
    base['color'] = fake.color_name()
    base['description'] = fake.paragraph(nb_sentences=5)

    features = _get_features()

    return {**base, **features}
