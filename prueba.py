import csv
import json
import requests
import datetime

url = 'http://localhost:3000/provedores'
datos = {}
datos['provedores'] = []


with open('libro.csv', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        if row['situacionActual']=='Presunto':
            situacionActual = 1
            nombreContribuyente = row['nombreContribuyente']
            rfc = row['\ufeffrfc']
            pSatPresunto = row['pSatPresunto']
            pSatPresunto = datetime.datetime.strptime(pSatPresunto, '%d/%m/%Y')
            pDofPresunto = row['pDofPresunto']
            pDofPresunto = datetime.datetime.strptime(pDofPresunto, '%d/%m/%Y')
            pSatDesvirtuado = row['pSatDesvirtuado']
            pDofDesvirtuado = row['pDofDesvirtuado']
            pSatDefinitivo = row['pSatDefinitivo']
            pDofDefinitivo = row['pDofDefinitivo']
            pSatFavorable = row['pSatFavorable']
            pDofFavorable = row['pDofFavorable']

            if nombreContribuyente.find("'") != -1:
                nombreContribuyente = nombreContribuyente.replace("'","''")
            if nombreContribuyente.find("//") == -1:
                if rfc != 'XXXXXXXXXXXX':
                    datos['provedores'].append({
                        'rfc': rfc,
                        'nombreContribuyente': nombreContribuyente,
                        'situacionActual': situacionActual,
                        'pSatPresunto': pSatPresunto.date(),
                        'pDofPresunto': pDofPresunto.date(),
                        'pSatDesvirtuado': pSatDesvirtuado,
                        'pDofDesvirtuado': pDofDesvirtuado,
                        'pSatDefinitivo': pSatDefinitivo,
                        'pDofDefinitivo': pDofDefinitivo,
                        'pSatFavorable': pSatFavorable,
                        'pDofFavorable': pDofFavorable
                        })
        elif (row['situacionActual']=='Desvirtuado'):
            situacionActual = 2
            nombreContribuyente = row['nombreContribuyente']
            rfc = row['\ufeffrfc']
            pSatPresunto = row['pSatPresunto']
            pSatPresunto = datetime.datetime.strptime(pSatPresunto, '%d/%m/%Y')
            pDofPresunto = row['pDofPresunto']
            pDofPresunto = datetime.datetime.strptime(pDofPresunto, '%d/%m/%Y')
            pSatDesvirtuado = row['pSatDesvirtuado']
            pSatDesvirtuado = datetime.datetime.strptime(pSatDesvirtuado, '%d/%m/%Y')
            pDofDesvirtuado = row['pDofDesvirtuado']
            if pDofDesvirtuado == '':
                pDofDesvirtuado = '00/00/0000';
            else:
                pDofDesvirtuado = datetime.datetime.strptime(pDofDesvirtuado, '%d/%m/%Y')
            pSatDefinitivo = row['pSatDefinitivo']
            pDofDefinitivo = row['pDofDefinitivo']
            pSatFavorable = row['pSatFavorable']
            pDofFavorable = row['pDofFavorable']
            if nombreContribuyente.find("'") != -1:
                nombreContribuyente = nombreContribuyente.replace("'","''")
            if nombreContribuyente.find("//") == -1:
                if rfc != 'XXXXXXXXXXXX':
                    datos['provedores'].append({
                        'rfc': rfc,
                        'nombreContribuyente': nombreContribuyente,
                        'situacionActual': situacionActual,
                        'pSatPresunto': pSatPresunto.date(),
                        'pDofPresunto': pDofPresunto.date(),
                        'pSatDesvirtuado': pSatDesvirtuado.date(),
                        'pDofDesvirtuado': pDofDesvirtuado.date(),
                        'pSatDefinitivo': pSatDefinitivo,
                        'pDofDefinitivo': pDofDefinitivo,
                        'pSatFavorable': pSatFavorable,
                        'pDofFavorable': pDofFavorable
                        })
        elif (row['situacionActual']=='Definitivo'):
            situacionActual = 3
            nombreContribuyente = row['nombreContribuyente']
            rfc = row['\ufeffrfc']
            pSatPresunto = row['pSatPresunto']
            pSatPresunto = datetime.datetime.strptime(pSatPresunto, '%d/%m/%Y')
            pDofPresunto = row['pDofPresunto']
            pDofPresunto = datetime.datetime.strptime(pDofPresunto, '%d/%m/%Y')
            pSatDesvirtuado = row['pSatDesvirtuado']
            pDofDesvirtuado = row['pDofDesvirtuado']
            pSatDefinitivo = row['pSatDefinitivo']
            pSatDefinitivo = datetime.datetime.strptime(pSatDefinitivo, '%d/%m/%Y')
            pDofDefinitivo = row['pDofDefinitivo']
            if pDofDefinitivo == '':
                pDofDefinitivo = '00/00/0000';
            else:
                pDofDefinitivo = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
            pSatFavorable = row['pSatFavorable']
            pDofFavorable = row['pDofFavorable']
            if nombreContribuyente.find("'") != -1:
                nombreContribuyente = nombreContribuyente.replace("'","''")
            if nombreContribuyente.find("//") == -1:
                if rfc != 'XXXXXXXXXXXX':
                    datos['provedores'].append({
                        'rfc': rfc,
                        'nombreContribuyente': nombreContribuyente,
                        'situacionActual': situacionActual,
                        'pSatPresunto': pSatPresunto.date(),
                        'pDofPresunto': pDofPresunto.date(),
                        'pSatDesvirtuado': pSatDesvirtuado,
                        'pDofDesvirtuado': pDofDesvirtuado,
                        'pSatDefinitivo': pSatDefinitivo.date(),
                        'pDofDefinitivo': pDofDefinitivo.date(),
                        'pSatFavorable': pSatFavorable,
                        'pDofFavorable': pDofFavorable
                        })
        elif (row['situacionActual']=='Sentencia favorable'):
            situacionActual = 4
            nombreContribuyente = row['nombreContribuyente']
            rfc = row['\ufeffrfc']
            pSatPresunto = row['pSatPresunto']
            pSatPresunto = datetime.datetime.strptime(pSatPresunto, '%d/%m/%Y')
            pDofPresunto = row['pDofPresunto']
            pDofPresunto = datetime.datetime.strptime(pDofPresunto, '%d/%m/%Y')
            pSatDesvirtuado = row['pSatDesvirtuado']
            pSatDesvirtuado = datetime.datetime.strptime(pSatDesvirtuado, '%d/%m/%Y')
            pDofDesvirtuado = row['pDofDesvirtuado']
            pDofDesvirtuado = datetime.datetime.strptime(pDofDesvirtuado, '%d/%m/%Y')
            pSatDefinitivo = row['pSatDefinitivo']
            pSatDefinitivo = datetime.datetime.strptime(pSatDefinitivo, '%d/%m/%Y')
            pDofDefinitivo = row['pDofDefinitivo']
            pDofDefinitivo = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
            pSatFavorable = row['pSatFavorable']
            pSatFavorable = datetime.datetime.strptime(pSatFavorable, '%d/%m/%Y')
            pDofFavorable = row['pDofFavorable']
            pDofFavorable = datetime.datetime.strptime(pDofDefinitivo, '%d/%m/%Y')
            if nombreContribuyente.find("'") != -1:
                nombreContribuyente = nombreContribuyente.replace("'","''")
            if nombreContribuyente.find("//") == -1:
                if rfc != 'XXXXXXXXXXXX':
                    datos['provedores'].append({
                        'rfc': rfc,
                        'nombreContribuyente': nombreContribuyente,
                        'situacionActual': situacionActual,
                        'pSatPresunto': pSatPresunto.date(),
                        'pDofPresunto': pDofPresunto.date(),
                        'pSatDesvirtuado': pSatDesvirtuado.date(),
                        'pDofDesvirtuado': pDofDesvirtuado.date(),
                        'pSatDefinitivo': pSatDefinitivo,
                        'pDofDefinitivo': pDofDefinitivo,
                        'pSatFavorable': pSatFavorable.date(),
                        'pDofFavorable': pDofFavorable.date()
                        })
    with open('data.json', 'w', encoding="utf-8" ) as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
    x = requests.post(url, json=datos)
    print(x.text)
    # print(datos)