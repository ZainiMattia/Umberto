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

