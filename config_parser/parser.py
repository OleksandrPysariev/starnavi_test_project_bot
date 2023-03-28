import configparser
import os
from abc import ABC, abstractmethod


class ParserBase(ABC):

    @staticmethod
    def get_path_to_file(filename: str):
        return os.path.join(os.getcwd(), filename)

    @abstractmethod
    def parse(self, filename):
        pass


class ConfigParserDriver(ParserBase):
    def parse(self, filename):
        config = configparser.RawConfigParser()
        config.read(self.get_path_to_file(filename))
        return config


class ConfigParser(ConfigParserDriver):
    # You can implement other parsers by inheriting new ConfigParserDriver parent class
    pass
