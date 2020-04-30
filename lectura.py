import csv
import json
import requests
import datetime

url = 'http://localhost:3000/provedores'
datos = {}
datos['provedores'] = []

def validarCampo (campo):
    if campo.find("-") > -1:
       campo = campo.replace("-","/")
    if campo == '':
        campo = '0000-00-00'
    else:
        if len(campo) <= 9:
            campo = datetime.datetime.strptime(campo, '%d/%m/%y')
            campo = campo.date()
        elif len(campo) == 10:
            campo = datetime.datetime.strptime(campo, '%d/%m/%Y')
            campo = campo.date()
        elif len(campo) > 10:
            print (campo)
            campo = campo.split()
            campo = campo[0]
            if len(campo) <= 9:
                campo = datetime.datetime.strptime(campo, '%d/%m/%y')
                campo = campo.date()
            elif len(campo) == 10:
                campo = datetime.datetime.strptime(campo, '%d/%m/%Y')
                campo = campo.date()
        # print(campo.date())
    return str(campo)

with open('lista4.csv', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        # # row = [entry.decode("utf8") for entry in row]
        # nombreContribuyente = row['nombreContribuyente']
        # rfc = row['\ufeffrfc']
        # pSatPresunto = validarCampo(row['pSatPresunto'])
        # # pSatPresunto = datetime.datetime.strptime(pSatPresunto, '%d/%m/%Y')
        # pDofPresunto = validarCampo(row['pDofPresunto'])
        # # pDofPresunto = datetime.datetime.strptime(pDofPresunto, '%d/%m/%Y')
        # pSatDesvirtuado = validarCampo(row['pSatDesvirtuado'])
        # # pSatDesvirtuado = datetime.datetime.strptime(pSatDesvirtuado, '%d/%m/%Y')
        # pDofDesvirtuado = validarCampo(row['pDofDesvirtuado'])
        # # pDofDesvirtuado = datetime.datetime.strptime(pDofDesvirtuado, '%d/%m/%Y')
        # pSatDefinitivo = validarCampo(row['pSatDefinitivo'])
        # # pSatDefinitivo = datetime.datetime.strptime(pSatDefinitivo, '%d/%m/%Y')
        # pDofDefinitivo = validarCampo(row['pDofDefinitivo'])
        # # pDofDefinitivo = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
        # pSatFavorable = validarCampo(row['pSatFavorable'])
        # # pSatFavorable = datetime.datetime.strptime(pSatFavorable, '%d/%m/%Y')
        # pDofFavorable = validarCampo(row['pDofFavorable'])
        # # pDofFavorable = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
        # situacionActual = 0;
        # if row['situacionActual']=='Sentencia favorable':
        #     situacionActual = 4
        # elif (row['situacionActual']=='Definitivo'):
        #     situacionActual = 3
        # elif (row['situacionActual']=='Desvirtuado'):
        #     situacionActual = 2
        # elif (row['situacionActual']=='Presunto'):
        #     situacionActual = 1
        # if nombreContribuyente.find("'") != -1:
        #     nombreContribuyente = nombreContribuyente.replace("'","''")
        # if nombreContribuyente.find("//") == -1:
        #     if rfc != 'XXXXXXXXXXXX':
        #         datos['provedores'].append({
        #             'rfc': rfc,
        #             'nombreContribuyente': nombreContribuyente,
        #             'situacionActual': situacionActual,
        #             'pSatPresunto': pSatPresunto,
        #             'pDofPresunto': pDofPresunto,
        #             'pSatDesvirtuado': pSatDesvirtuado,
        #             'pDofDesvirtuado': pDofDesvirtuado,
        #             'pSatDefinitivo': pSatDefinitivo,
        #             'pDofDefinitivo': pDofDefinitivo,
        #             'pSatFavorable': pSatFavorable,
        #             'pDofFavorable': pDofFavorable
        #             })
    # print (data)
    # with open('data.json', 'w', encoding="utf-8" ) as file:
    #     json.dump(datos, file, indent=4, ensure_ascii=False)
    # x = requests.post(url, json=datos)
    # print(x.text)
    # print(datos)