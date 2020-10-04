from random import randint

from api import random


class TestEntity:

    def test_create_new_entity(self, client):
        data = random.random_entity()
        res = client.vr(client.create_entity(data), [201, 204])
        response_body = res.json()
        assert response_body.get("bookingid")
        assert response_body.get("booking") == data

    # def test_create_new_entity(self, client):
    #     data = random.random_entity()
    #     res = client.vr(client.create_entity(data), [200, 201])
    #     created = res.json()
    #     assert created.get("bookingid")
    #     assert created.get("booking") == data
    #
    # def test_new_entity_exists(self, client):
    #     data = random.random_entity()
    #     res = client.vr(client.create_entity(data), [200, 201])
    #     created = res.json()
    #     bookingid = created.get("bookingid")
    #     res = client.vr(client.get_entity(bookingid))
    #     exists = res.json()
    #     assert exists == data
    #
    # def test_update_entity(self, client):
    #     data = random.random_entity()
    #     res = client.vr(client.create_entity(data), [200, 201])
    #     created = res.json()
    #     bookingid = created.get("bookingid")
    #     data2 = random.random_entity()
    #     res = client.vr(client.update_entity(bookingid, data2))
    #     updated = res.json()
    #     assert updated == data2
    #
    # def test_not_existing_entity(self, client):
    #     res = client.get_entity(randint(10000, 99999))
    #     assert res.status_code == 404
