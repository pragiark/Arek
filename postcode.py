a = "79-900"
b = "80-155"


#start = a[0:2]
#start += a[3:7]
#start = int(start)
#start += 1
start = int(a.replace("-",""))
stop = int(b.replace("-",""))
#koniec = None
#end = b[0:2]
#end += b[3:7]
#end = int(end)
lista = []
for i in range(start, stop):
    i = str(i)
    lista.append(i[0:2] + "-" + i[2:5])
print(lista)

