from random import randint
import pytest
from api import entity


class TestEntity:

    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2(self, client, headers):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(
            client.get_entity(data['id'], {"parameter": "value", "Fiware-Service": "test_id_happy_path",
                                           "Fiware-ServicePath": "/test", "Content-Type": "application/json"}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.parametrize(("headers",),
                             [
                                 "application/json",
                                 "application/xml",
                                 "application/x-www-form-urlencoded",
                                 "multipart/form-data",
                                 "text/plain",
                                 "text/html",
                                 "dsfsdfsdf",
                                 "<sdsd>",
                                 "(eeqweqwe)"
                             ])
    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2_with_Content_Type_header(self, client, headers):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(
            client.get_entity(data['id'], {"parameter": "value", "Fiware-Service": "test_id_happy_path",
                                           "Fiware-ServicePath": "/test", "Content-Type": headers}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2_with_Content_Type_header_and_empty_value(self, client):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(
            client.get_entity(data['id'], {"parameter": "value", "Fiware-Service": "test_id_happy_path",
                                           "Fiware-ServicePath": "/test", "Content-Type": ""}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.parametrize(("headers",),
                             [
                                 "service",
                                 "service_12",
                                 "service_sr",
                                 "SERVICE",
                                 "max length allowed"
                             ])
    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2_with_several_services(self, client, headers):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(
            client.get_entity(data['id'], {"parameter": "value", "Fiware-Service": headers,
                                           "Fiware-ServicePath": "/test", "Content-Type": "application/json"}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2_without_service(self, client):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(client.get_entity(data['id'], {"parameter": "value", "Fiware-ServicePath": "/test",
                                                              "Content-Type": "application/json"}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.parametrize(("headers",),
                             [
                                 "service.sr",
                                 "Service-sr",
                                 "Service(sr)",
                                 "Service=sr",
                                 "Service<sr>",
                                 "Service,sr",
                                 "service#sr",
                                 "service%sr",
                                 "service&sr"
                             ])
    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2_with_wrong_several_services(self, client, headers):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(
            client.get_entity(data['id'], {"parameter": "value", "Fiware-Service": headers,
                                           "Fiware-ServicePath": "/test"}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    def test_to_get_an_attribute_by_entity_ID_using_NGSI_v2_with_bad_length_several_services(self, client, headers):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос с разными типами content_type, на который должен получить status_code 200->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Проверка корректности создания /v2/entities/{entityId}
        client.verify_response(
            client.get_entity(data['id'], {"parameter": "value", "Fiware-Service": "greater than max length allowed",
                                           "Fiware-ServicePath": "/test"}), [200])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])