from abc import ABC, abstractmethod
from functools import wraps
import logging
from hashlib import new

from Exception.invalid_value_exception import invalidValueException
from Tools.scripts.var_access_benchmark import C
from isort import output
from wrapt import decorator
from Exception import invalid_value_exception

exc = invalidValueException()


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.ERROR)
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename='C:\output\wer.txt', filemode='w', level=logging.ERROR)
                    logging.error(e)
                else:
                    raise exception("Invalid mode. Supported modes are 'console' and 'file'")
                raise

        return wrapper

    return decorator


# def logged(exc, file='C:\output\wer.txt'):
#     def wrapper(func):
#         if invalid_value_exception:
#             logging.basicConfig(filename='C:\output\wer.txt', filemode='w',
#                                 format='%(size)s - %(levelname)s - %(message)s')
#             logging.error('This will get logged to a file')
#             raise exc("You have written size op PEN what is less than 0 or equal 0")
#         return wrapper


class Pen(ABC):
    people_who_use = set()

    def __len__(self):
        return len(self.people_who_use)

    def __init__(self, brand, colour, material, size):
        """
        brand(str) it is the brand of Pen
        colour(str) it is the colout of Pem
        material(str) it is the material of Pen
        size(int) it is the size of Pen
        """
        self.brand = brand
        self.colour = colour
        self.material = material
        self.size = size

    @abstractmethod
    def calculate_price(self):
        """
        it will calculate total price
        """
        # if self.size <= 0:
        #     raise ValueError("You have written size op PEN what is less than 0 or equal 0")
        # else:
        pass

    @logged(invalidValueException, mode="file")
    def is_exsist_pen(self):
        if self.size <= 0:
            raise invalidValueException("size of PEN is less than 0")

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def people_who_use(self):
        pass
