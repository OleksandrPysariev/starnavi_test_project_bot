import random
import string

from faker import Faker


class FakeWrapper(Faker):
    def __init__(self):
        super().__init__()

    @property
    def _profile(self):
        return self.simple_profile()

    @property
    def username(self):
        return self._profile["username"]

    @property
    def password(self):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(10))

    @property
    def email(self):
        return self._profile["mail"]

    @property
    def first_name(self):
        return self._profile["name"].split(" ")[0]

    @property
    def second_name(self):
        return self._profile["name"].split(" ")[1]

    @property
    def title(self):
        return self.paragraph(nb_sentences=1)

    @property
    def body(self):
        return self.paragraph(nb_sentences=10)


fake = FakeWrapper()
