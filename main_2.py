#le liste servono per stampare più cose in una singola variabile --> la lista è cambiabile, e ogni elemento al suo interno è "numerato"
thislist = ["apple", "banana", "cherry"]
print(thislist)

#le liste possono avere all'interno dei duplicati e li considereranno 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# utilizzo comando len() --> ti dice quanti elementi ci sono al suo interno
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#le liste posso contenere tutto i "type"
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#una lista può contenere più "type"
list1 = ["abc", 34, True, 40, "male"]

#le liste hanno un "type: list"
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#per creare una lista posso fare anche così
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#stampare solo un elemento della lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#stampare un elemento con i numeri negativi
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#stampare da un elemento ad un altro scelto arbitrariamente 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#fino a 4--> escluso 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#dal 2 in poi
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#controllare se un elemento è nella lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#cambiare gli elementi nella lista
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#cambiare un "range" di elementi nella lista
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#cambiare un elemento con più
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#cambiare più elementi con uno 
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#aggiungere elementi nella lista in determinate posizione 
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#aggiungere un elemento alla fine 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#allungare la lista 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#rimoszione elementi nella lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#rimuovere elementi nella lista (con i numeri associati)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#se non metto il numero dentro pop() mi eleminerà l'ultimo elemento 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#"del" altro comando per eliminare
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#"del" elimina l'intera compagnia 
thislist = ["apple", "banana", "cherry"]
del thislist

#"clear" elimina gli elementi della lista, ma quest'ultima rimane 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#"for" così mi stampa gli elementi nella lista riacchiusi in una variabile arbitraia 
thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)

#"range" e "len" utili per ciclare le liste
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  #comando "while" 
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#forma compatta di for 
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#avendo 2 liste posso stampare gli elementi con quella lettera in quella nuova 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#mettere gli elementi in un'altra lista con il "for"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# ! esclude un elemento
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#uso "range" per arrivare ad un certo numero della lista
newlist = [x for x in range(10)]
print(newlist)

#mettendo la condizione "if"
newlist = [x for x in range(10) if x < 5]
print(newlist)

#mettere gli elementi maiuscoli 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#scambiare una variabile con tutti gli elementi della lista 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

#eliminare un elemento e sostituirlo nella stessa posizione con un altro 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#"sort"  stamperà alfabeticamente la lista (str)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#"sort" stamperà in ordine crescente la lista (nuemri)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#stampare inversamente la lista (reverse = true)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

