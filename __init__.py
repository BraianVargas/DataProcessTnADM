from .clases.admProducts import admProduct
from .clases.tnProducts import tnProduct
from _csv import *
from .data.files.dataTransfer import *




admList = []
tnList = []


if __name__ == '__main__':
    
    print("************************** Iniciando proceso **************************")
    
    admList = readADM('admProduct.csv', admList)
    tnList = readTN('tnProducts.csv', tnList)

    """
    EN ESTA PARTE VOY A PROCESAR LAS DOS LISTAS Y DE AHI 
    COMPARAR LOS PRODUCTOS POR CODIGO DE ARTICULO
    """

    compareAndGetProducts(admList, tnList)
    