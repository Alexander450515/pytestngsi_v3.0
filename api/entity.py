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


def entity_replace():
    return {
        "temperature": {
            "value": 25.5
        },
        "seatNumber": {
            "value": 6
        }
    }


def entity_append():
    return {
        "temperature": {
            "value": 25.5
        },
        "seatNumber": {
            "value": 6
        }
    }


def entity_update():
    return {
        "temperature": {
            "value": 29.5
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
            "value": "",
            "type": "",
            "metadata": {
                "crs": {
                    "value": ""
                }
            }
        }
    }


def wrong_value_types_of_entity():
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
            "value": faker.pyint(),
            "type": faker.pyint(),
            "metadata": {
                "crs": {
                    "value": faker.pyint()
                }
            }
        }
    }


def wrong_json_structure_of_entity():
    return {
        "type": "car",
        # "id": "d1211",
        "temperature": {
            # "value": 21.7
            "type": 21.7
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


def empty_entity_for_replace():
    return {
        "temperature": {
            "value": ""
        },
        "seatNumber": {
            "value": ""
        }
    }


def wrong_value_types_of_entity_for_replace():
    return {
        "temperature": {
            "value": "NUMBER SHOULD BE HERE"
        },
        "seatNumber": {
            "value": "NUMBER SHOULD BE HERE"
        }
    }


def wrong_json_structure_for_replace():
    return {
        "temperature": {
            "value": "NUMBER SHOULD BE HERE"
        },
        "seatNumber": {
            "value": "NUMBER SHOULD BE HERE"
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
