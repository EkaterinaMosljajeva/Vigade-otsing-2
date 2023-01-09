#1
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while vastus!=o_vastus:
#    print("Viga! Sisesta Õige vastus on ...", )
#    vastus=int(input("Sisesta vastus ..."))
#    k+=1
#print("Õige vastus! Katsed oli ...",k )
#print()
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while True:
#    if vastus!=o_vastus:
#        print("Viga! Sisesta Õige vastus on ...", )
#        vastus=int(input("Sisesta vastus ..."))
#        k+=1
#    else:
#        break
#print("Õige vastus! Katsed oli ...",k )

#2
#x=0
#while x<30:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#print()
#x=0
#while True:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#    if x==30:
#        break
#print()
#for x in range(30):
#    if x%2==1:
#        print(x, end="")

print("*** KÜSIMUSTE MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1: 
    try:
        a = (abs(int(input("Sisesta täisarv => ")))) #Lisatud sulud
        break
    except ValueError:
         print("See pole täisarv.")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi teha.")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
    print()
    c=b=a #Üleliigsed märgid on eemaldatud
    paaris=0 #Üleliigsed märgid on eemaldatud
    paaritu=0 #Üleliigsed märgid on eemaldatud
    while b > 0: #;->:
        if b%2==0:
            paaris+=1
        else:
            paaritu+=1
        b=b//10
    print("Paaris arvude kogus:", paaris) #Lisatud sulud
    print("Paaritu on:", paaritu) #Lisatud sulud
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake ümber* sisestatud arv")
    print()
    b=0
    while a > 0: #Lisatud koolon
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #=+ -> +=
    print("*Pööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Uurime Syracuse hüpoteesi") #Koristatud sulg
    print()
    if c % 2 == 0:
        print(c," - paarisarv. Jagame 2-ga.")
    else:
        print(c," - paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")
    while c != 1:
            if c % 2 == 0: #Lisatud on võrdne märk
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(round(c), end=" ")
    print()
    print("Hüpotees on õige") #''->"