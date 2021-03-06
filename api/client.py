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

    def get_api_entry_points(self):
        return self._s.get(self.host + "/v2")

    def create_entity(self, data: dict):
        return self._s.post(self.host + "/v2/entities", json=data)

    # тут мб поломал
    def get_entity(self, uid: str, headers: dict):
        return self._s.get(self.host + f"/v2/entities/{uid}", header=headers)

    def get_entity_attribute(self, uid: str):
        return self._s.get(self.host + f"/v2/entities/{uid}/attrs")

    def update_or_append_entity(self, uid: str, data: dict):
        return self._s.post(self.host + f"/v2/entities/{uid}/attrs", json=data)

    def put_entity(self, uid: str, data: dict):
        return self._s.put(self.host + f"/v2/entities/{uid}/attrs", json=data)

    def patch_entity(self, uid: str, data: dict):
        return self._s.patch(self.host + f"/v2/entities/{uid}/attrs", json=data)

    def delete_entity(self, uid: str):
        return self._s.delete(self.host + f"/v2/entities/{uid}")



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