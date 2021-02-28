from faker import Faker
import random

fake = Faker()

_FEATURES = {
    "seller": ["Rozetka", "Other"],
    "brand": ["Samsung", "LG", "Xiaomi", "Lenovo", "Apple", "Acer", "HP"],
    "RAM": ["1Gb", "2Gb", "4Gb"],
    "model_year": ["2020", "2019", "2018"],
    "refresh_rate": ["60Hz", "120Hz", "240Hz"],
    "display_size": [14, 17, 21, 24, 25],
    "CPU": ["Intel Core i5", "Intel Core i8", "Intel Core i7", "Intel Core i9", "AMD A8"],
    "disk_size": ["512Gb", "1Tb"],
    "WLAN": ["802.11a/b/g/n", "802.11ac", "802.11g/n"],
    "graphics_processor": ["AMD Radeon HD", "AMD Radeon Pro", "AMD Radeon R9", "Intel UHD Graphics",
                           "NVIDIA GeForce"],
    "video_output": ["Display Port", "DVI", "HDMI", "VGA", "Mini - DVI"],
    "resolution": ["2880x1800", "1440x900", "1200x800"]
}


def _get_features():
    return {name: random.choice(values) for (name, values) in _FEATURES.items() if type(values) in (list, tuple)}


def get():
    base = {}
    base['category'] = 'Computer'
    base['price'] = random.randrange(4000, 120000)
    base['description'] = fake.paragraph(nb_sentences=5)

    features = _get_features()

    return {**base, **features}
