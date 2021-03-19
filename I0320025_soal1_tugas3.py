#list 10 nama teman
ListTeman=["Anisa","Efa","Echa","Uddin","Fadhila","Cristin","Erysa","Erika","Alip","Nadya"]

#Menampilkan list nama teman indeks 4,6,7
print("Nama teman indeks 4,6,7:", ListTeman[4],",",ListTeman[6],",",ListTeman[7])

#Mengubah nama teman indeks 3,5,9
ListTeman[3]="Fajri"
ListTeman[5]="Vincent"
ListTeman[9]="Retno"

#Menambah nama teman
ListTeman.extend(["Divana","Uli"])

#Menampilkan nama teman dengan perulangan
for data in ListTeman :
    print(data)

#Menampilkan panjang list
print(len(ListTeman))