def rom_to_int(string):
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for p in table:
    	c=True
        while c:
            if len(string)>=len(p[0]):
                if string[0:len(p[0])]==p[0]:
                    returnint+=p[1]
                    string=string[len(p[0]):]
                else: c=False
            else: c=False

    return returnint
rom=raw_input()
print(rom_to_int(rom))
