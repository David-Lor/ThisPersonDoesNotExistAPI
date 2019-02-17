from itertools import repeat
from typing import Dict, Optional
from .online_getter import *
from .helpers import *

__all__ = ("Person",)


class Person(object):
    def __init__(self, fetch_online: bool = False):
        self.picture: bytes = None
        self.checksum: Dict[str, Optional[str]] = dict(zip(algorithms_available, repeat(None)))

        if fetch_online:
            self.set_from_online()
            self.get_checksum()

    def set_from_online(self, params: dict = None, **kwargs) -> bytes:
        self.picture = get_online_person(params, **kwargs)
        return self.picture

    def get_checksum(self, method: str = "md5") -> str:
        checksum = self.checksum.get(method.lower(), get_checksum_from_picture(self.picture, method))
        if method not in self.checksum.keys():
            self.checksum[method] = checksum
        return checksum

    def save(self, file: str = None) -> int:
        """Save the picture of this person to a file.
        The picture must be provided as it content as bytes.
        The filename must be provided as a str with the absolute or relative path where to store it.
        If no filename is provided, a filename will be generated using the MD5 checksum of the picture.
        :param file: filename as string, relative or absolute path (optional)
        :return: int returned by file.write
        """
        return save_picture(self.picture, file)
