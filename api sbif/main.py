import urllib.request
import json
from datetime import datetime
import calendar


testfile = urllib.request.URLopener()
contents = "http://api.sbif.cl/api-sbifv3/recursos_api/uf/periodo/2018/2018?apikey=76ee98402f2d3db479b278e8c266c7dad0867edb&formato=json&callback=despliegue"
testfile.retrieve(contents, "file.json")

data = json.load(open('file.json'))
#pprint(data)
meses = []
subio = {}
bajo= {}
mant= {}
uf=0.0 #valor uf inicio mes
mes =1
mayor_Uf = 0
menor_Uf = 0
mes_Menor= "No hubo meses con baja de UF"
mes_Mayor= "No hubo meses con alza de UF"
bandera = True
for x in data['UFs']:
    #print(x['Valor'])

    valor = x['Valor']
    valor = valor.replace(".","")
    valor = valor.replace(",",".")
    valor = float(valor)
    fecha = (datetime.strptime(x['Fecha'], '%Y-%m-%d'))
    if bandera:
        menor_Uf = valor
        bandera = False
    if valor > mayor_Uf:
        mayor_Uf = valor
        mes_Mayor = fecha
    if valor < menor_Uf:
        menor_Uf = valor
        mes_Menor = fecha
    if fecha.month == mes:
        #print(fecha.day)

        if(fecha.day == 1):
            uf = valor
        if(fecha.day == calendar.monthrange(2018,fecha.month)[1]):
            mes_abre = calendar.month_name[fecha.month]
            aux = valor - uf
            if aux <0:
                bajo[mes_abre]= -1 * aux
            if aux ==0:
                mant[mes_abre] = aux
            if aux > 0:
                subio[mes_abre] = aux
    else:
        if fecha.day ==1:
            uf = valor
            mes += 1

print(data['UFs'])
subio = sorted(subio.items(), key=lambda kv: kv[1])
print(subio)
for x in subio:
    print(x[0])
bajo = sorted(bajo.items(), key=lambda kv: kv[1], reverse=True)
print(bajo)
mant = sorted(mant.items(), key=lambda kv: kv[0])
print(mant)
print(mes_Mayor)
print(mes_Menor)