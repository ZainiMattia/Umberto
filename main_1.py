#Creazione variabili 
x=17 
y= "Mattia"
print(x)
print(y)

#Riassegnazione variabili
x=1957       # x è una varibile int
x="Vitiano"  # x è diventata un str
print(x)    

#Cambiamento tipo variabili 
x=str(3)   #x è una variabile str e sarà "3"
y=int(3)   #y è una variabile int e sarà 3
z=float(3) #z è una variabile float e sarà 3.0

#Stampa tipo variabili 
x=5
y="Barbapapà"
print(type(x))
print(type(y))

#"" e '' sono la stessa cosa
x = "John"
x = 'John'

#La stessa lettera maiuscola non sovrascriverà quella minuscola+
a=30
A="Super Sayan"

#Come posso nominare una variabile per renderla "legale":-Una variabile deve iniziare con una lettera o un _; -Può contenere solo caratter alfa-numerici e _ (A-z, 0-9, _); Le varibaili scritte con la stessa parola cambiano in base ai caratteri (Age,age,AGE)sono variabili diverse
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Assegnazione variabili su una linea 
x, y, z= "Lei", "Lui", "Tarantola"
print(x)
print(y)
print(z)

#Come estrarre dei valori e trasformarli in variabili -->(mi stamperà i contenuti della "LISTA")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

main_1.py