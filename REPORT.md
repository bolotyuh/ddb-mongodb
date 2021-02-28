## Task 3 - Робота з базовими функціями документо-орієнтованої БД на прикладі MongoDB

### Завдання

1. Створіть декілька товарів з різним набором властивостей

```bash
$ python -m app.import_data_to_mongo
```

2. Напишіть запит, який виводіть усі товари

```json
[
  {
    "_id": ObjectId(
    "603b99fb9ecc2098454d4136"
    ),
    "brand": "OnePlus",
    "os": "Android",
    "name": "Xiaomi Redmi Note 9",
    "title": "Xiaomi Redmi Note 9 4/128GB Midnight Grey",
    "category": "Phone",
    "price": 26959,
    "color": "Magenta",
    "description": "Member statement company little child special wide. Mean ask dog level national against. Go administration population her many subject.",
    "seller": "Rozetka",
    "RAM": "4Gb",
    "display_size": "640x480",
    "camera_resolution": "720*1024",
    "cell_phone_features": "Built-In GPS",
    "phone_carrier": "Sprint",
    "internal_storage_memory": "64Gb"
  },
  {
    "_id": ObjectId(
    "603b99fb9ecc2098454d413d"
    ),
    "category": "Computer",
    "price": 5504,
    "description": "Live compare dark especially. Miss think police perhaps five already. Great tax lawyer including. Very development degree quickly.",
    "seller": "Other",
    "brand": "Acer",
    "RAM": "1Gb",
    "model_year": "2018",
    "refresh_rate": "120Hz",
    "display_size": 25,
    "CPU": "Intel Core i9",
    "disk_size": "1Tb",
    "WLAN": "802.11g/n",
    "graphics_processor": "AMD Radeon HD",
    "video_output": "HDMI",
    "resolution": "1440x900"
  }
]
```

3. Підрахуйте скільки товарів у певної категорії

`>>>QUERY`

```javascript
db.items.aggregate(
    {$project: {category: 1, count: {$add: [1]}}},
    {
        $group: {
            _id: "$category",
            number: {$sum: "$count"}
        }
    })
```

`>>>RESULT`

```json
[
  {
    "_id": "Smart watch",
    "number": 100.0
  },
  {
    "_id": "TV",
    "number": 100.0
  },
  {
    "_id": "Computer",
    "number": 100.0
  },
  {
    "_id": "Phone",
    "number": 100.0
  }
]
```

4. Підрахуйте скільки є різних категорій товарів
   `>>>QUERY`

```javascript
db.items.distinct('category').length
```

`>>>RESULT`

```json
4
```

5. Виведіть список всіх виробників товарів без повторів
   `>>>QUERY`

```javascript
db.items.distinct('brand')
```

`>>>RESULT`

```json
[
  "OnePlus",
  "Hisense",
  "Apple",
  "LG",
  "Xiaomi",
  "Acer",
  "Samsung",
  "HP",
  "Sony",
  "Nokia",
  "Huawei",
  "Meizu",
  "Lenovo"
]
```

6. Напишіть запити, які вибирають товари за різними критеріям і їх сукупності:
    - a) категорія та ціна (в проміжку) - конструкція $and,
    - b) модель чи одна чи інша - конструкція $or,
    - c) виробники з переліку - конструкція $in

`>>>QUERY`

```javascript
// a) категорія та ціна (в проміжку) - конструкція $and,
db.getCollection('items').find({'category': 'Phone', 'price': {'$gte': 1000, '$lte': 40000}})

// b) модель чи одна чи інша - конструкція $or,
db.getCollection('items').find({'$or': [{'brand': 'OnePlus'}, {'brand': 'Iphone'}]})

// c) виробники з переліку - конструкція $in
db.getCollection('items').find({'brand': {'$in': ['OnePlus', 'Nokia', 'Iphone']}})
```

7. Оновить певні товари, змінивши існуючі значення і додайте нові властивості (характеристики) усім товарам за певним
   критерієм
   `>>>QUERY`

```javascript
db.getCollection('items').update(
    {'price': {'$gte': 100000}},
    {
        '$mul': {'price': 0.05},
        '$set': {'promo': ['black friday 2020']}
    })
```

8. Знайдіть товари у яких є (присутнє поле) певні властивості
   
`>>>QUERY`

```javascript
db.getCollection('items').find({'promo': {'$exists': true}})
```

`>>>RESULT`

```json
{
  "_id": ObjectId(
  "603b99fb9ecc2098454d4151"
  ),
  "category": "Computer",
  "price": 5549.0,
  "description": "Find prepare hair across hour notice east. Attack attack political course trip. Place politics late.",
  "seller": "Other",
  "brand": "LG",
  "RAM": "2Gb",
  "model_year": "2020",
  "refresh_rate": "120Hz",
  "display_size": 14,
  "CPU": "Intel Core i5",
  "disk_size": "1Tb",
  "WLAN": "802.11a/b/g/n",
  "graphics_processor": "Intel UHD Graphics",
  "video_output": "HDMI",
  "resolution": "1440x900",
  "promo": [
    "black friday 2020"
  ]
}
```

9. Для знайдених товарів збільшіть їх вартість на певну суму

`>>>QUERY`

```javascript
db.getCollection('items').update({'price': {'$lte': 5000}}, {'$inc': {'price': 750}})
```

Товари ви додаєте в замовлення - orders, яке містити вартість, ім'я замовника, і адресу доставки.

1. Створіть кілька замовлень з різними наборами товарів, але так щоб один з товарів був у декількох замовленнях

```bash
$ python 
```

2. Виведіть всі замовлення

`>>>QUERY`

```javascript
db.getCollection('orders').find({})
```

`>>>RESULT`

```json
{
  "_id": ObjectId(
  "603bacce876e0d4992f86a08"
  ),
  "order_number": 77794204,
  "total_sum": 448391,
  "payment": {
    "card_owner": "Juan Allen",
    "cardId": "KYBP21917335480832"
  },
  "order_items_id": [
    {
      "ref": "items",
      "id": ObjectId(
      "603bab264653b65cd91673ee"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603baca1ca03a20d727226be"
      )
    }
  ],
  "customer": {
    "username": "qmiller",
    "name": "Juan Allen",
    "sex": "M",
    "address": "0542 Castillo Extensions\nNew Emily, IL 88972",
    "mail": "carol14@hotmail.com"
  }
}
```

3. Виведіть замовлення з вартістю більше певного значення
   
`>>>QUERY`

```javascript
db.getCollection('orders').find({'total_sum': {'$gte': 5000}})
```

`>>>RESULT`

```json
{
  "_id": ObjectId(
  "603bacce876e0d4992f86a0b"
  ),
  "order_number": 98611112,
  "total_sum": 747771,
  "payment": {
    "card_owner": "Jeffery Simmons",
    "cardId": "BANX21745003552066"
  },
  "order_items_id": [
    {
      "ref": "items",
      "id": ObjectId(
      "603bacce876e0d4992f868f4"
      )
    }
  ],
  "customer": {
    "username": "jeffrey81",
    "name": "Jeffery Simmons",
    "sex": "M",
    "address": "989 Jane Street\nLake Carolinehaven, NV 52980",
    "mail": "marissapreston@hotmail.com"
  }
}
```

4. Знайдіть замовлення зроблені одним замовником
   
`>>>QUERY`

```javascript
db.getCollection('orders').find({'customer.username': 'jeffrey81'})
```

`>>>RESULT`

```json
{
  "_id": ObjectId(
  "603bacce876e0d4992f86a0b"
  ),
  "order_number": 98611112,
  "total_sum": 747771,
  "payment": {
    "card_owner": "Jeffery Simmons",
    "cardId": "BANX21745003552066"
  },
  "order_items_id": [
    {
      "ref": "items",
      "id": ObjectId(
      "603bacce876e0d4992f868f4"
      )
    }
  ],
  "customer": {
    "username": "jeffrey81",
    "name": "Jeffery Simmons",
    "sex": "M",
    "address": "989 Jane Street\nLake Carolinehaven, NV 52980",
    "mail": "marissapreston@hotmail.com"
  }
}
```

5. Знайдіть всі замовлення з певним товаром (товарами) (шукати можна по ObjectId)
   
`>>>QUERY`

```javascript
db.getCollection('orders').find({'order_items_id.id': ObjectId("603bacd7d8ad58ccfdb01286")})
```

`>>>RESULT`

```json
/* 1 */
{
  "_id": ObjectId(
  "603bacd7d8ad58ccfdb0129c"
  ),
  "order_number": 52796393,
  "date": ISODate(
  "2019-03-20T03:25:45.000Z"
  ),
  "total_sum": 45221,
  "payment": {
    "card_owner": "Blake Acosta",
    "cardId": "SFJE00834007212519"
  },
  "order_items_id": [
    {
      "ref": "items",
      "id": ObjectId(
      "603bab179546df9191a7027a"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603baca1ca03a20d72722817"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacd7d8ad58ccfdb0117a"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bab9ff07a0d0e67e37471"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacd7d8ad58ccfdb01172"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bab9ff07a0d0e67e374db"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacce876e0d4992f868ef"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacd7d8ad58ccfdb01286"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bab9ff07a0d0e67e37525"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603baca1ca03a20d7272270a"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacce876e0d4992f869cf"
      )
    }
  ],
  "customer": {
    "username": "ulewis",
    "name": "Blake Acosta",
    "sex": "M",
    "address": "Unit 6390 Box 7097\nDPO AP 14475",
    "mail": "ngraves@gmail.com"
  }
}

/* 2 */
{
  "_id": ObjectId(
  "603bacd7d8ad58ccfdb012b9"
  ),
  "order_number": 25101348,
  "date": ISODate(
  "1979-11-07T09:52:17.000Z"
  ),
  "total_sum": 280321,
  "payment": {
    "card_owner": "Crystal Diaz",
    "cardId": "PGBB86050840771722"
  },
  "order_items_id": [
    {
      "ref": "items",
      "id": ObjectId(
      "603bab9ff07a0d0e67e3749a"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacd7d8ad58ccfdb0114c"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bab9ff07a0d0e67e37431"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacd7d8ad58ccfdb01286"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bab0486b039da4ce0d7b3"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacd7d8ad58ccfdb01155"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bab264653b65cd91673b4"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603baca1ca03a20d727226ea"
      )
    },
    {
      "ref": "items",
      "id": ObjectId(
      "603bacce876e0d4992f869ba"
      )
    }
  ],
  "customer": {
    "username": "carlyburton",
    "name": "Crystal Diaz",
    "sex": "F",
    "address": "2542 King Ville Apt. 950\nSouth Jeffrey, KS 66684",
    "mail": "dana45@yahoo.com"
  }
}
```

6. Додайте в усі замовлення з певним товаром ще один товар і збільште існуючу вартість замовлення на деяке значення Х
   
`>>>QUERY`

```javascript
db.getCollection('orders').update(
    {'order_items_id.id': ObjectId("603bacd7d8ad58ccfdb01286")},
    {
        '$inc': {'total_sum': 454},
        '$push': {
            'order_items_id': {
                "ref": "items",
                "id": ObjectId("603bab264653b65cd91673ee")
            }
        }
    })
```

7. Виведіть кількість товарів в певному замовленні

`>>>QUERY`
```javascript
db.orders.aggregate({'$match':{"order_number": 25101348} }, {$project: { count: { $size:"$order_items_id" }}})
```

`>>>RESULT`

```json
{
    "_id" : ObjectId("603bacd7d8ad58ccfdb012b9"),
    "count" : 9
}
```
8. Виведіть тільки інформацію про кастомера і номери кредитної карт, для замовлень вартість яких перевищує певну суму

`>>>QUERY`
```javascript
db.getCollection('orders').find({'total_sum': {'$gte': 2343}}, {'customer': 1, 'payment.cardId': 1})
```

`>>>RESULT`

```json
[{
    "_id" : ObjectId("603bacce876e0d4992f86a07"),
    "payment" : {
        "cardId" : "ORXH17855822034793"
    },
    "customer" : {
        "username" : "leon83",
        "name" : "Amy Fleming",
        "sex" : "F",
        "address" : "7021 Anthony Road Suite 210\nNew Debrastad, OR 04018",
        "mail" : "kgregory@hotmail.com"
    }
},
{
    "_id" : ObjectId("603bacce876e0d4992f86a08"),
    "payment" : {
        "cardId" : "KYBP21917335480832"
    },
    "customer" : {
        "username" : "qmiller",
        "name" : "Juan Allen",
        "sex" : "M",
        "address" : "0542 Castillo Extensions\nNew Emily, IL 88972",
        "mail" : "carol14@hotmail.com"
    }
}]
```

9. Видаліть товар з замовлень, зроблених за певний період дат

`>>>QUERY`
```javascript
db.getCollection('orders').remove({'date':{'$gte': new ISODate("2017-04-14T23:59:59Z"), '$lte': new ISODate("2020-04-14T23:59:59Z")}})
```

`>>>RESULT`
Removed 4 record(s) in 5ms
```json
```

10. Перейменуйте у всіх замовлення ім'я (прізвище) замовника

`>>>QUERY`
```javascript
db.getCollection('orders').updateMany({}, {'$set':{'customer.name': 'Bob'}})
```

`>>>RESULT`

```json
{
    "acknowledged" : true,
    "matchedCount" : 96.0,
    "modifiedCount" : 95.0
}
```

11. (+2 бали)* Знайдіть замовлення зроблені одним замовником, і виведіть тільки інформацію про кастомера та товари у замовлені підставивши замість ObjectId("***") назви товарів та їх вартість (аналог join-а між таблицями orders та items).
`>>>QUERY`
```javascript
db.getCollection('orders').aggregate([
   {'$match': {'customer.username': 'qmiller'}},
   {
      "$lookup": {
         "from": "items",
         "localField": "order_items_id.id",
         "foreignField": "_id",
         "as": "items"
      }
   },
   {'$project': {'customer': 1, 'items': 1}}
])
```

`>>>RESULT`

```json
{
    "_id" : ObjectId("603bacce876e0d4992f86a08"),
    "customer" : {
        "username" : "qmiller",
        "name" : "Bob",
        "sex" : "M",
        "address" : "0542 Castillo Extensions\nNew Emily, IL 88972",
        "mail" : "carol14@hotmail.com"
    },
    "items" : [ 
        {
            "_id" : ObjectId("603bab264653b65cd91673ee"),
            "category" : "TV",
            "price" : 118451,
            "color" : "MediumOrchid",
            "description" : "West bag coach write success participant area visit. Continue future floor contain day record cultural. Space plan security event.",
            "seller" : "Other",
            "brand" : "Xiaomi",
            "RAM" : "4Gb",
            "os" : "IOS TV",
            "connectivity_type" : "ethernet",
            "model_year" : "2019",
            "resolution" : "8k",
            "television_features" : "smart TV",
            "refresh_rate" : "120Hz",
            "display_size" : 60
        }, 
        {
            "_id" : ObjectId("603baca1ca03a20d727226be"),
            "brand" : "Sony",
            "os" : "IOS",
            "name" : "iPhone 12",
            "title" : "New Apple iPhone 12(128GB, Graphite) [Locked] + Carrier Subscription",
            "category" : "Phone",
            "price" : 53032,
            "color" : "DarkTurquoise",
            "description" : "Walk thousand act fact total particular. Fly city middle sister. Government indicate remain newspaper.",
            "seller" : "Other",
            "RAM" : "1Gb",
            "display_size" : "720*1024",
            "camera_resolution" : "720*1024",
            "cell_phone_features" : "4k video recording",
            "phone_carrier" : "Sprint",
            "internal_storage_memory" : "8Gb"
        }
    ]
}
```

1. Створіть Сapped collection яка б містила 5 останніх відгуків на наш інтернет-магазин. Структуру запису визначіть самостійно.
Перевірте що при досягненні обмеження старі відгуки будуть затиратись

`>>>QUERY`
```javascript
db.createCollection("feedbacks", { capped: true,size:50000, max:5 })

db.getCollection('feedbacks').insertOne({
    'created_at':new ISODate(),
    'user': {
        'username':'er123r1223',
        'email':'er32020@gmail.com' 
      },
      'text':'sdfjl jsdlfkj sdifjsdfkj sldfkjsdfl lksdjflkj ldsjflksdjfl'
    })
```