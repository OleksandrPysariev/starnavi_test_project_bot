import os

from ..request_maker import req_driver as requests
from csv import DictWriter

from requests import Response

from bot.src.faker import fake
from settings import ADDRESS, CREDENTIALS_FILENAME


class SingUpAction:
    def __init__(self):
        self.signup_data = None

    def set_signup_data(self, data: dict):
        self.signup_data = data

    @staticmethod
    def store_data(storage_data: dict):
        file_exists = os.path.isfile(CREDENTIALS_FILENAME)
        with open(CREDENTIALS_FILENAME, "a", newline="") as fd:
            dict_writer_object = DictWriter(fd, fieldnames=storage_data.keys())
            if not file_exists:
                dict_writer_object.writeheader()
            dict_writer_object.writerow(storage_data)
            fd.close()

    @staticmethod
    def build_data() -> (str, str):
        password = fake.password

        request_data = {
            "username": fake.username,
            "password": password,
            "password2": password,
            "email": fake.email,
            "first_name": fake.first_name,
            "last_name": fake.second_name
        }

        signup_data = {
            "username": request_data["username"],
            "password": request_data["password"]
        }

        return request_data, signup_data

    def make_register_request(self) -> Response:
        request_data, signup_data = self.build_data()
        self.set_signup_data(signup_data)
        return requests.post(f"http://{ADDRESS}/api/auth/register", data=request_data)

    def make_signup_request(self) -> Response:
        return requests.post(f"http://{ADDRESS}/api/auth/login", data=self.signup_data)

    def execute(self, number_of_users: int):

        for i in range(number_of_users):
            success = False
            while not success:
                r = self.make_register_request()
                if r.status_code == 201:
                    success = True
            self.store_data(self.signup_data)
