from random import randint
import pytest
from api import entity


class TestEntity:

    # @pytest.mark.parametrize(("data",), [('entity.entity()',)])
    def test_create_new_entity(self, client):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        response = client.verify_response(client.get_entity(data['id']), [200])
        response_body = response.json()
        for key in data:
            if key in ('id', 'type'):
                assert response_body[key] == data[key]
            else:
                assert response_body[key]['value'] == data[key]['value']
        # Проверка корректности создания /v2/entities/{entityId}/attrs
        response = client.verify_response(client.get_entity_attribute(data['id']), [200])
        response_body = response.json()
        for key in data:
            if key in ('id', 'type'):
                continue
            assert response_body[key]['value'] == data[key]['value']
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    def test_replace_all_entity_attributes(self, client):
        """Отправляет POST запрос на создание->
        Отправляет PUT запрос на замену атрибутов->
        Отправляет GET запрос->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена атрибутов
        data_for_replace = entity.entity_replace()
        client.verify_response(client.put_entity(data['id'], data_for_replace), [204])
        # Проверка корректности создания /v2/entities/{entityId}/attrs
        response = client.verify_response(client.get_entity_attribute(data['id']), [200])
        response_body = response.json()
        for key in data_for_replace:
            if key in ('id', 'type'):
                continue
            assert response_body[key]['value'] == data_for_replace[key]['value']
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    def test_update_or_append_entity_attributes(self, client):
        """Отправляет POST запрос на создание->
        Отправляет PUT запрос на замену атрибутов->
        Отправляет GET запрос->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Добавление и замена
        data_for_append = entity.entity_append()
        client.verify_response(client.update_or_append_entity(data['id'], data_for_append), [204])

        # Проверка корректности создания /v2/entities/{entityId}/attrs
        response = client.verify_response(client.get_entity_attribute(data['id']), [200])
        response_body = response.json()
        for key in data_for_append:
            if key in ('id', 'type'):
                continue
            assert response_body[key]['value'] == data_for_append[key]['value']
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    #
    # def test_create_empty_entity(self, client):
    #     """Должен вернуть ошибку 404"""
    #     data = entity.empty_entity()
    #     client.verify_response(client.create_entity(data), [404])  #

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
