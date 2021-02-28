from faker import Faker
import random

fake = Faker()

_FEATURES = {
    "seller": ["Rozetka", "Other"],
    "brand": ["Samsung", "LG", "Sony", "Hisense", "Xiaomi"],
    "RAM": ["1Gb", "2Gb", "4Gb"],
    "os": ["IOS TV", "Android", ],
    "connectivity_type": ["bluetooth", "ethernet", "serial", "usb", "wireless"],
    "model_year": ["2020", "2019", "2018"],
    "resolution": ["8k", "4k", "1080p", "720p"],
    "television_features": ["3d", "smart TV"],
    "refresh_rate": ["60Hz", "120Hz", "240Hz"],
    "display_size": [32, 43, 50, 55, 60, 65]
}


def _get_features():
    return {name: random.choice(values) for (name, values) in _FEATURES.items() if type(values) in (list, tuple)}


def get():
    base = {}
    base['category'] = 'TV'
    base['price'] = random.randrange(4000, 120000)
    base['color'] = fake.color_name()
    base['description'] = fake.paragraph(nb_sentences=5)

    features = _get_features()

    return {**base, **features}
