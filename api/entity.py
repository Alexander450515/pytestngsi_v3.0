from faker import Faker

faker = Faker()


def entity():
    return {
        "type": "car",
        "id": "d1211",
        "temperature": {
            "value": 21.7
        },
        "humidity": {
            "value": 60
        },
        "location": {
            "value": "41.3763726, 2.1864475",
            "type": "geo:point",
            "metadata": {
                "crs": {
                    "value": "WGS84"
                }
            }
        }
    }


def empty_entity():
    return {
        "type": "",
        "id": "",
        "temperature": {
            "value": ""
        },
        "humidity": {
            "value": ""
        },
        "location": {
            "value": "41.3763726, 2.1864475",
            "type": "geo:point",
            "metadata": {
                "crs": {
                    "value": "WGS84"
                }
            }
        }
    }


def wrong_entity():
    return {
        "type": faker.word(),
        "id": faker.pystr(),
        "temperature": {
            "value": faker.pyint()
        },
        "humidity": {
            "value": faker.pyint()
        },
        "location": {
            "value": "41.3763726, 2.1864475",
            "type": "geo:point",
            "metadata": {
                "crs": {
                    "value": "WGS84"
                }
            }
        }
    }


def entity_replace():
    return {
        "temperature": {
            "value": 25.5
        },
        "seatNumber": {
            "value": 6
        }
    }


def empty_entity_replace():
    return {
        "temperature": {
            "value": ""
        },
        "seatNumber": {
            "value": ""
        }
    }


def wrong_entity_replace():
    return {
        "temperature": {
            "value": faker.pyint()
        },
        "seatNumber": {
            "value": faker.pyint()
        }
    }

# {
#         "firstname": faker.first_name(),
#         "lastname": faker.last_name(),
#         "totalprice": faker.pyint(),
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": faker.iso8601()[:10],
#             "checkout": faker.iso8601()[:10]
#         },
#         "additionalneeds": faker.word(),
#     }
