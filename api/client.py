import inspect
import logging

import requests

logger = logging.getLogger("example." + __name__)


class RestfulBookerClient:
    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def verify_response(self, response: requests.Response, ok_status=200) -> requests.Response:
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if response.status_code not in ok_status:
            raise ValueError(
                f"Verified response: function {func} failed: "
                f"server responded {response.status_code} "
                f"with data: {response.content}"
            )
        else:
            logger.info(
                f"Verified response: function {func} code {response.status_code}"
            )
        return response

    # def authorize(self, username, password):
    #     res = self.login(username, password)
    #     if res.status_code != 200:
    #         raise Exception("Unable to authorize using given credentials")
    #     session_token = res.json().get("token")
    #     cookie = requests.cookies.create_cookie("token", session_token)
    #     self._s.cookies.set_cookie(cookie)
    #
    # def login(self, username, password):
    #     data = {"username": username, "password": password}
    #     return self._s.post(self.host + "/auth", json=data)

    def create_entity_url(self, data: dict):
        return self._s.post(self.host + "/v2/entities", json=data)

    def get_entity_url(self, uid: str):
        return self._s.get(self.host + f"/v2/entities/{uid}")

    def get_entity_attribute_url(self, uid: str):
        return self._s.get(self.host + f"/v2/entities/{uid}/attrs")

    def update_entity_url(self, uid: str, data: dict):
        return self._s.put(self.host + f"/v2/entities/{uid}", json=data)

    def delete_entity_url(self, uid: str):
        return self._s.put(self.host + f"/v2/entities/{uid}/attrs")
