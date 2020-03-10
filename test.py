
# mensaje8 = "HOL//A MUNDO"
# if mensaje8.find("//") != -1:
#   mensaje8 = mensaje8.replace("//", "''")
# print(mensaje8)
import datetime

date_str = '14-08-19 ' # The date - 29 Dec 2017
# format_str = '%d/%m/%Y' # The format
# datetime_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
# print (datetime_obj.date())
objeto = date_str.split()
print (objeto[0])
objeto2 = objeto[0]
print (objeto2)
valor = objeto2.find("-")
if valor > -1:
    objeto2 = str(objeto2)
    objeto2.replace("-","/")
    objeto2 = objeto2.replace("-","/")
    # print (o)
print (objeto2.find("-"))
print (objeto2)