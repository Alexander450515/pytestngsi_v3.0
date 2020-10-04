from faker import Faker

faker = Faker()


def random_entity():
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
