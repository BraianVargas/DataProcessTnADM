from clases.tnProducts import tnProduct
from ...clases.admProducts import admProduct
import csv


listOfCategory = [
    'RELOJ SMARTWHATCH','FUENTE','IMPRESORA LASER',
    'IMPRESORA TINTA','GABINETE','NOTEBOOK',
    'TABLET','TECLADO','MOUSE','PARLANTE PORTATIL','PARLANTE',
    'AURICULAR','RAM','PLACA DE VIDEO',
    'MONITOR','MOTHERBOARD'
]

def readADM(filename, adm):
    file = open(filename, 'r')

    with file as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            if row[7] in listOfCategory:
                stock = row[2].split(',')
                stock = int(stock[0]) / 10
                if stock >= int(1):
                    prod = admProduct(row[0], row[1], stock, row[3], row[4], row[5], row[6], row[7])
                    adm.append(prod)
            else:
                continue
    csv_file.close()
    return adm

def readTN(filename, tnlist):
    file = open(filename, 'r')

    with file as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)
        for row in csv_reader:
            if row[2] in listOfCategory:
                prod = tnProduct(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15],
                    row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23],
                    row[24], row[25], row[26], row[27], row[28]
                    )
                tnlist.append(prod)
            else:
                continue
    csv_file.close()
    return tnlist


def compareAndGetProducts(admList, tnList):
    i = 0
    finalList = []

    while i != len(admList):
        j = 0
        while j != len(tnList):
            if admList[i].getCode() == tnList[j].getBarcode():
                tnList[j].setStock(admList[i].getStock())
                tnList[j].setPrice(admList[i].getPrice()) #aqui multipliar precio lista 3 por el porcentaje
                finalList.append(tnList[j])
            j+=1
        i+=1
    
    return finalList