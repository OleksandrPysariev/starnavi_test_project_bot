import os

from settings import CREDENTIALS_FILENAME


def purge():
    file_exists = os.path.isfile(os.path.join(os.getcwd(), CREDENTIALS_FILENAME))
    if file_exists:
        os.remove(os.path.join(os.getcwd(), CREDENTIALS_FILENAME))
