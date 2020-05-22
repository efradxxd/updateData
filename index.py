import csv
import json
import requests
import datetime
import os

# os.remove("data.json")

url = 'http://ec2-52-53-179-97.us-west-1.compute.amazonaws.com:3000/actualizarProvedores'
datos = {}
datos['provedores'] = []

def validarCampo (campo):
    if campo.find("-") > -1:
       campo = campo.replace("-","/")
    if campo == '':
        campo = '0000-00-00'
    else:
        if len(campo) <= 9:
            try:
                campo = datetime.datetime.strptime(campo, '%d/%m/%y')
                campo = campo.date()
            except:
                campo = '0000-00-00'
        elif len(campo) == 10:
            campo = datetime.datetime.strptime(campo, '%d/%m/%Y')
            campo = campo.date()
        elif len(campo) > 10:
            # print (campo)
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

with open('lista.csv', encoding='ISO-8859-1') as csvfile:
    reader = csv.DictReader(csvfile)
    rfcAnterior = '';
    for row in reader:
        # row = [entry.decode("utf8") for entry in row]v
        nombreContribuyente = row['Nombre del Contribuyente']
        rfc = row['RFC']
        pSatPresunto = validarCampo(row['Publicación página SAT presuntos'])
        # pSatPresunto = datetime.datetime.strptime(pSatPresunto, '%d/%m/%Y')
        pDofPresunto = validarCampo(row['Publicación DOF presuntos'])
        # pDofPresunto = datetime.datetime.strptime(pDofPresunto, '%d/%m/%Y')
        pSatDesvirtuado = validarCampo(row['Publicación página SAT desvirtuados'])
        # pSatDesvirtuado = datetime.datetime.strptime(pSatDesvirtuado, '%d/%m/%Y')
        pDofDesvirtuado = validarCampo(row['Publicación DOF desvirtuados'])
        # pDofDesvirtuado = datetime.datetime.strptime(pDofDesvirtuado, '%d/%m/%Y')
        pSatDefinitivo = validarCampo(row['Publicación página SAT definitivos'])
        # pSatDefinitivo = datetime.datetime.strptime(pSatDefinitivo, '%d/%m/%Y')
        pDofDefinitivo = validarCampo(row['Publicación DOF definitivos'])
        # pDofDefinitivo = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
        pSatFavorable = validarCampo(row['Publicación página SAT sentencia favorable'])
        # pSatFavorable = datetime.datetime.strptime(pSatFavorable, '%d/%m/%Y')
        pDofFavorable = validarCampo(row['Publicación DOF sentencia favorable'])
        # pDofFavorable = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
        situacion = 0;
        if row['Situación del contribuyente']=='Sentencia Favorable':
            situacion = 4
        elif (row['Situación del contribuyente']=='Definitivo'):
            situacion = 3
        elif (row['Situación del contribuyente']=='Desvirtuado'):
            situacion = 2
        elif (row['Situación del contribuyente']=='Presunto'):
            situacion = 1
        if nombreContribuyente.find("'") != -1:
            nombreContribuyente = nombreContribuyente.replace("'","''")
        if nombreContribuyente.find("//") == -1:
            if rfc != 'XXXXXXXXXXXX':
                if rfc != rfcAnterior:
                    # datos['provedores'].pop()
                    # print(rfc)
                    datos['provedores'].append({
                        'rfc': rfc,
                        'nombreContribuyente': nombreContribuyente,
                        'situacion': situacion,
                        'pSatPresunto': pSatPresunto,
                        'pDofPresunto': pDofPresunto,
                        'pSatDesvirtuado': pSatDesvirtuado,
                        'pDofDesvirtuado': pDofDesvirtuado,
                        'pSatDefinitivo': pSatDefinitivo,
                        'pDofDefinitivo': pDofDefinitivo,
                        'pSatFavorable': pSatFavorable,
                        'pDofFavorable': pDofFavorable
                        })
                    rfcAnterior = rfc;                   
# print (data)
with open('data.json', 'w', encoding="utf-8" ) as file:
    json.dump(datos, file, indent=4, ensure_ascii=False)
x = requests.post(url, json=datos)
print(x.text)
# print(datos)