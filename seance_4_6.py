chun = ""
y = input("Jusqu'a quelle table de multiplication?\nRéponse: ")

try:
    y=int(y)
    z = input("Jusqu'a quel multiplication?\nRéponse: ")

    try:
        z=int(z)   
        for x in range(1,y+1):
            print("\nTable de ",x , ":\n")
            for a in range(1,z+1):
#                chun=chun + " " + str(x) + "*" + str(a) + "=" + str(x*a)
                chun=chun + f"{x}*{a}={x*a} "
            print(chun)
            chun = ""

    except:
        print("Cette valeur n'est pas un entier.")

except:
    print("Cette valeur n'est pas un entier.")


#for x in range(1,11):
#    print("\nTable de ",x , ":\n")
#    for a in range(1,11):
#        print(str(x*a))