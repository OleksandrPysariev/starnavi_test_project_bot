import csv
from time import sleep

from settings import ADDRESS, CREDENTIALS_FILENAME
from ..request_maker import req_driver as requests


class HTTPActionWithCreds:
    def __init__(self):
        self.login_data = None
        self.access = None
        self.route = None
        self.number_of_requests = 1
        self.login_route = "api/auth/login"
        self.method = "post"
        self.protocol = "http"

    def build_request_url(self):
        if not self.route:
            raise ValueError("Route is undefined")
        return f"{self.protocol}://{ADDRESS}/{self.route}"

    @staticmethod
    def build_data():
        return dict()

    def make_request(self):
        return getattr(requests, self.method)(
            self.build_request_url(), headers=self.build_header(), data=self.build_data()
        )

    def get_authentication(self):
        r = requests.post(f"{self.protocol}://{ADDRESS}/{self.login_route}", data=self.login_data)
        if r.status_code == 200:
            return r.json().get("access")
        else:
            raise ValueError("Invalid credentials")

    def set_authentication(self, authentication: str):
        self.access = authentication

    def build_header(self):
        return {"Authorization": self.access}

    def set_current_login_data(self, username, password):
        self.login_data = dict(username=username, password=password)

    def execute(self):
        with open(CREDENTIALS_FILENAME) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader, None)
            for row in csv_reader:
                self.set_current_login_data(row[0], row[1])
                try:
                    access = self.get_authentication()
                except ValueError:
                    continue
                self.set_authentication(access)
                sleep(1)
                for i in range(self.number_of_requests):
                    self.make_request()
