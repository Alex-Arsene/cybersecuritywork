# # print("hello world")
# # numar_int = 3
# # print(numar_int)

# # numar_float = 4.5
# # print(numar_float)

# # str ="helloworld"
# # print(str)
# ### creeaza o LISTA goala
# nums=[]
# ### adaugam date in LISTA
# nums.append(21)
# nums.append(4.5)
# nums.append('string')
# print(nums)
# ### DICTIONAR cu nume si varsta
# persoane= {
#     'alex':21,
#     'irina':22
# }
# print(persoane)
# ### un TUPLE ce contine fructe
# fructe=('mar', 'portocala')
# print(fructe)
# ### un SET ce contine fructe
# fructe={"mar", "portocala"}
# print(fructe)
# ### primeste date de la utilizator
# name = input("Introduce numele tau: ") 
# print("Salut", name)
# ### primim un numar de la utilizator
# ### tipul de returnare a funcției input () este string 
# ### deci trebuie să convertim intrarea în număr întreg
# n1=int(input("Da i valoare lui n1: "))
# n2=int(input("Da i valoare lui n2: "))
# ### facem înmulțirea celor 2 numere
# n3 = n1 * n2
# print(f"produsul este: {n3}")
# ### selecționare unui număr mai mare ca 12 dar mai mic decat 35
# if(n3>12):
#     print("n3 este mai mare:")
# elif(n3>35):
#     print("n3 este mai mare decat 35")
# else:
#     print("n3 este in afara intervalului cautat")

# ### functie pentru adunarea a două numere
# n4=int(input("da i valoare lui n4: "))
# n5=int(input("da i valoare lui n5: "))
# def sum(n4,n5):
#     suma=n4+n5
#     print(f"Suma este: {suma}")
# sum(n4,n5)
# def main():
#     num1=int(input("primul numar: "))
#     num2=int(input("al doilea numar: "))
#     rezultat=sum(num1,num2)
#     print(rezultat)
# if __name__=="__main__":
#     main()
# for num in range(5):    
#    print(num)
from pwn import *
r = remote('127.0.0.1', 1234) #conectarea la un ip si port
r.send('Salut\n') 