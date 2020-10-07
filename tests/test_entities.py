from random import randint
import pytest
from api import entity


class TestEntity:

    # pytest -v -m positive_test для запуска всех позитивных тестов
    @pytest.mark.positive_test
    def test_create_new_entity(self, client):
        """Отправляет POST запрос на создание->
        Отправляет GET запрос и проверяет корректность создания->
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

    @pytest.mark.positive_test
    def test_replace_all_entity_attributes(self, client):
        """Отправляет POST запрос на создание->
        Отправляет PUT запрос на замену атрибутов->
        Отправляет GET запрос и проверяет корректность создания->
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

    @pytest.mark.positive_test
    def test_update_or_append_entity_attributes(self, client):
        """Отправляет POST запрос на создание->
        Отправляет POST запрос на обновление и замену атрибутов->
        Отправляет GET запрос и проверяет корректность создания->
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

    @pytest.mark.positive_test
    def test_update_existing_entity_attributes(self, client):
        """Отправляет POST запрос на создание->
        Отправляет PATCH запрос на обновление атрибутов->
        Отправляет GET запрос и проверяет корректность создания->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена
        data_for_update = entity.entity_update()
        client.verify_response(client.patch_entity(data['id'], data_for_update), [204])
        # # Проверка корректности создания /v2/entities/{entityId}/attrs
        response = client.verify_response(client.get_entity_attribute(data['id']), [200])
        response_body = response.json()
        for key in data_for_update:
            if key in ('id', 'type'):
                continue
            assert response_body[key]['value'] == data_for_update[key]['value']
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    # pytest -v -m negative_test для запуска всех негативных тестов
    @pytest.mark.negative_test
    def test_create_empty_entity(self, client):
        """Отправляет POST запрос с пустыми значениями->
        Должен вернуть ошибку 400"""
        data = entity.empty_entity()
        client.verify_response(client.create_entity(data), [400])

    @pytest.mark.negative_test
    def test_create_entity_with_wrong_value_types(self, client):
        """Отправляет POST запрос с неверным типом данных->
        Должен вернуть ошибку 400"""
        data = entity.wrong_value_types_of_entity()
        client.verify_response(client.create_entity(data), [400])

    @pytest.mark.negative_test
    def test_create_entity_with_wrong_json_structure(self, client):
        """Отправляет POST запрос с неправильной структурой файла json->
        Должен вернуть ошибку 400"""
        data = entity.wrong_value_types_of_entity()
        client.verify_response(client.create_entity(data), [400])

    @pytest.mark.positive_test
    def test_replace_all_entity_attributes_by_empty_attributes(self, client):
        """Отправляет PUT запрос с пустыми значениями->
        Должен вернуть status_code 204 и заменить значения на пустые->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена атрибутов
        data_for_replace = entity.empty_entity_for_replace()
        client.verify_response(client.put_entity(data['id'], data_for_replace), [204])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.skip
    @pytest.mark.positive_test
    def test_replace_all_entity_attributes_by_wrong_value_types_of_entity(self, client):
        """Отправляет PUT запрос с пустыми значениями->
        Должен вернуть status_code 204 и создать объект с некорректным значением->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена атрибутов
        data_for_replace = entity.wrong_value_types_of_entity_for_replace()
        client.verify_response(client.put_entity(data['id'], data_for_replace), [204])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.negative_test
    def test_replace_all_entity_with_wrong_json_structure(self, client):
        """Отправляет PUT запрос с неправильной структрурой файла json->
        Должен вернуть status_code 400->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена атрибутов
        data_for_replace = entity.wrong_json_structure_for_replace()
        client.verify_response(client.put_entity(data['id'], data_for_replace), [400])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.negative_test
    def test_update_or_append_entity_attributes_with_empty_entity(self, client):
        """Отправляет POST запрос с пустыми значениями->
        Должен вернуть status_code 204 и заменить значение объекта на пустое->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Добавление и замена
        data_for_append = entity.empty_entity_for_append()
        client.verify_response(client.update_or_append_entity(data['id'], data_for_append), [204])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.negative_test
    def test_update_or_append_entity_with_wrong_value_types(self, client):
        """Отправляет POST запрос с неверным типом данных->
        Должен вернуть status_code 204 и заменить значение объекта на значение с неверным типом данных->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Добавление и замена
        data_for_append = entity.wrong_value_types_of_entity_for_append()
        client.verify_response(client.update_or_append_entity(data['id'], data_for_append), [204])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.negative_test
    def test_update_or_append_entity_with_wrong_json_structure(self, client):
        """Отправляет POST запрос с неправильной структурой файла json->
        Должен вернуть status_code 400->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Добавление и замена
        data_for_append = entity.wrong_json_structure_for_append()
        client.verify_response(client.update_or_append_entity(data['id'], data_for_append), [400])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.negative_test
    def test_update_existing_entity_attributes_with_empty_entity(self, client):
        """Отправляет PATCH запрос с пустыми значениями->
        Должен вернуть status_code 204 и заменить значение объекта на пустое->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена
        data_for_update = entity.empty_entity_for_update()
        client.verify_response(client.patch_entity(data['id'], data_for_update), [204])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])

    @pytest.mark.negative_test
    def test_update_existing_entity_with_wrong_value_types(self, client):
        """Отправляет PATCH запрос с неверным типом данных->
        Должен вернуть status_code 204 и заменить значение объекта на значение с неверным типом данных->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена
        data_for_update = entity.empty_entity_for_update()
        client.verify_response(client.patch_entity(data['id'], data_for_update), [204])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])


    @pytest.mark.negative_test
    def test_create_entity_with_wrong_json_structure(self, client):
        """Отправляет PATCH запрос с неправильной структурой файла json->
        Должен вернуть status_code 400->
        Отправляет DELETE запрос на удаление"""
        # Создание
        data = entity.entity()
        client.verify_response(client.create_entity(data), [201, 204])
        # Замена
        data_for_update = entity.wrong_json_structure_for_update()
        client.verify_response(client.patch_entity(data['id'], data_for_update), [400])
        # Удаление
        client.verify_response(client.delete_entity(data['id']), [204])
