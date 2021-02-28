from faker import Faker
import random

fake = Faker()

_PHONES = [
    {
        "brand": "Apple",
        "os": "IOS",
        "name": "iPhone 12 Pro Max",
        "title": "New Apple iPhone 12 Pro Max (128GB, Graphite) [Locked] + Carrier Subscription",
    },
    {
        "brand": "Apple",
        "os": "IOS",
        "name": "iPhone 12 Pro",
        "title": "New Apple iPhone 12 Pro (128GB, Graphite) [Locked] + Carrier Subscription",
    },
    {
        "brand": "Apple",
        "os": "IOS",
        "name": "iPhone 12",
        "title": "New Apple iPhone 12(128GB, Graphite) [Locked] + Carrier Subscription",
    },
    {
        "brand": "Xiaomi",
        "os": "Android",
        "name": "Xiaomi Redmi Note 9",
        "title": "Xiaomi Redmi Note 9 4/128GB Midnight Grey",
    },
    {
        "brand": "Xiaomi",
        "os": "Android",
        "name": "Xiaomi Mi 11",
        "title": "Xiaomi Mi 11 8/256GB Midnight Gray",
    },
    {
        "brand": "Nokia",
        "os": "Android",
        "name": "Nokia 5.3",
        "title": "Nokia 5.3 4/64GB DualSim Charcoal",
    },
    {
        "brand": "Nokia",
        "os": "Android",
        "name": "Nokia 150",
        "title": "Nokia 150 TA-1235 DualSim Black",
    },
    {
        "brand": "OnePlus",
        "os": "Android",
        "name": "OnePlus 6T",
        "title": "OnePlus 6T 8/256GB Midnight Black",
    },
    {
        "brand": "Huawei",
        "os": "Android",
        "name": "Huawei P",
        "title": "Huawei P Smart 2021 NFC 128 GB Black",
    },
]

_FEATURES = {
    "seller": ["Rozetka", "Other"],
    "brand": ["Apple", "Huawei", "Nokia", "Meizu", "OnePlus", "Samsung", "Sony", "Xiaomi"],
    "RAM": ["1Gb", "2Gb", "4Gb"],
    "os": ["IOS", "Android", "BlackBerry"],
    "display_size": ['640x480', '720*1024'],
    "camera_resolution": ['640x480', '720*1024'],
    "cell_phone_features": ["4k video recording", "bluetooth", "camera", "dual camera", "LTE", "Built-In GPS"],
    "phone_carrier": ["Sprint", "Kyivstar", "AT&T"],
    "internal_storage_memory": ["4Gb", "8Gb", "16Gb", "32Gb", "64Gb"]
}


def _get_features():
    return {name: random.choice(values) for (name, values) in _FEATURES.items() if type(values) in (list, tuple)}


def get():
    base = random.choice(_PHONES)
    base['category'] = 'Phone'
    base['price'] = random.randrange(800, 65000)
    base['color'] = fake.color_name()
    base['description'] = fake.paragraph(nb_sentences=5)

    features = _get_features()

    return {**base, **features}
