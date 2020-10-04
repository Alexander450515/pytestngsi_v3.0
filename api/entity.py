from faker import Faker

faker = Faker()


def entity():
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
            "value": faker.pyint()
        },
        "seatNumber": {
            "value": faker.pyint()
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
