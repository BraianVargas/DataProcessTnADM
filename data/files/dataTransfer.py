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
                stock = row[2].split(',')
                stock = int(stock[0]) / 10
                if stock >= int(1):
                    prod = tnProduct(
                        row[0], row[1], stock, row[3], row[4], row[5], row[6], row[7])
                    tnlist.append(prod)
            else:
                continue
    csv_file.close()
    return tnlist


    