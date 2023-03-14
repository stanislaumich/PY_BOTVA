'''
разобрать и посчитать такой формат из экселя
walmau 6altau;107;DominosZ;151;walmau 6altau;99;Макыс;77;Макыс;124;**SUPERHelen**;130;**SUPERHelen**;144;ЛюЛюНдРа=;140;DambLDoR;97;**SUPERHelen**;151;
бешка-бебешка_;105;Бродвей;139;T@nk;97;T@nk;63;T@nk;102;бешка-бебешка_;98;StasLz42;125;**SUPERHelen**;131;**SUPERHelen**;63;DambLDoR;129;
*Милка;100;Kerberos;136;Тудор;93;DambLDoR;61;Тудор;100;ЛюЛюНдРа=;95;Kerberos;116;Kerberos;111;Kerberos;53;Kerberos;78;

'''

def main():
    d = {}
    with open("arena200223.csv", "r") as file:
        content = file.read()
        content = content.replace("\n", "")
        #print(content)
        #with open("res.txt", "a") as file:
        #file.write(content)
        ar = content.split(";")
        s = 0
        rs = ""
        lst = []
        for r in ar:
            #print(r)
            rs = rs + r + ";"
            s = s + 1
            if s == 2:
                s = 0
                t = rs.split(";")
                rs = ""
                if t[0] != "":
                    bob = (t[0], t[1])
                    lst.append(bob)

        for r in lst:
            print(r)
            #print(d.setdefault(r[0], 0))
            d[r[0]] = d.setdefault(r[0], 0) + int(r[1])
            print(d[r[0]])

    with open("arena200223-RES.csv", "w") as file:
        for key, value in d.items():
            s = (key+";"+str(value))
            print(s)






if __name__ == "__main__":
    main()