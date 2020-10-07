import pytest
from api import entity


class TestApiEntryPoints:

    # pytest -v -m positive_test для запуска всех позитивных тестов
    @pytest.mark.positive_test
    def test_get_api_entry_points(self, client):
        """Отправляет GET запрос и проверяет корректность полученного ответа"""
        response = client.verify_response(client.get_api_entry_points(), [200])
        response_body = response.json()
        assert response_body["entities_url"] == "/v2/entities"
        assert response_body["types_url"] == "/v2/types"
        assert response_body["subscriptions_url"] == "/v2/subscriptions"
        assert response_body["registrations_url"] == "/v2/registrations"
