from pymongo import MongoClient
from pymongo.collection import Collection
from faker import Faker
import datamaker
import random
from tqdm import tqdm


def main():
    client = MongoClient('localhost', 27020, username='admin', password='qwerty')

    db = client['main']
    items = db['items']

    COUNT_SAMPLES = 100
    BATCH_SIZE = 20

    fake = Faker()

    # Insert Items
    for _ in tqdm(range(max(COUNT_SAMPLES // BATCH_SIZE, 1))):
        _data = []

        for _ in range(BATCH_SIZE):
            _data.append(datamaker.get_phones())
            _data.append(datamaker.get_tv())
            _data.append(datamaker.get_smart_watches())
            _data.append(datamaker.get_computers())

        items.insert_many(_data)

    def _get_order_items(n, items_collection: Collection):
        return [_d['_id'] for _d in items_collection.aggregate([{"$sample": {"size": n}}])]


    # Insert Orders
    for _ in tqdm(range(50)):
        customer = fake.simple_profile()
        del customer['birthdate']
        order_items = [{"ref": "items", "id": _id} for _id in _get_order_items(random.randrange(1, 12), items)]

        _data = {
            "order_number": random.randint(0, 99999999),
            "date": fake.date_time(),
            "total_sum": random.randrange(1, 999999, 10),
            "payment": {
                "card_owner": customer["name"],
                "cardId": fake.bban(),
            },
            "customer": customer,
            "order_items_id": order_items
        }

        db['orders'].insert_one(_data)


if __name__ == '__main__':
    main()
