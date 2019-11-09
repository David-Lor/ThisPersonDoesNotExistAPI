import requests
from .helpers import *

__all__ = ("get_online_person",)


def get_online_person(params=None, **kwargs) -> bytes:
    """Get a picture of a fictional person from the ThisPersonDoesNotExist webpage.
    :param params: params dictionary used by requests.get
    :param kwargs: kwargs used by requests.get
    :return: the image as bytes
    """
    r = requests.get("https://thispersondoesnotexist.com/image", headers={'User-Agent': 'My User Agent 1.0'}).content
    return r


def save_online_person(file: str = None, params=None, **kwargs) -> int:
    """Get a picture of a fictional person from the ThisPersonDoesNotExist webpage, and save it to a file.
    The filename must be provided as a str with the absolute or relative path where to store it.
    If no filename is provided, a filename will be generated using the MD5 checksum of the picture, with jpeg extension.
    :param file: filename as string, relative or absolute path (optional)
    :param params: params dictionary used by requests.get
    :param kwargs: kwargs used by requests.get
    :return: int returned by file.write
    """
    picture = get_online_person(params, **kwargs)
    return save_picture(picture, file)
