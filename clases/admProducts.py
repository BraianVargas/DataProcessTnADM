from unicodedata import category

from sqlalchemy import ColumnDefault


class admProduct:
    __code = None
    __name = None
    __stock = None
    __L1, L2, L3 = None
    __category = None


    def __init__(self, code, name, stock, l1, l2, l3, category):
        self.__code = code 
        self.__name = name
        self.__stock = stock
        self.__L1 = l1
        self.__L2 = l2
        self.__L3 = l3
        self.__category = category

    def getCode(self):
        return int(self.__code)

    def getStock(self):
        return int(self.__stock)