class For:
    def __init__(self):
        pass

    #ciclo repetitivo de incrementos o decrementos se ejecuta por verdadero
    def usoFor(self):
        datos=["Ashley",21,True]
        numeross=(2,5.6,4,1)
        docente={"nombre":"Ashley", "edad":21,"fac":"facil"}
        listanotas=[(30,40),(20,40),(50,40)]
        #range([inicio=0],limite,[incremento/decremento]. Genera un rang de valores desde un valor inicial a un valor dinal
        #se ejecuta desde inicio hasta el limite
        for i in range(5):
            print("i={}".format(i))#ciclo de uno en uno
        for i in range(2,10):
            print("i={}".format(i))#ciclo de un valor inicial a un valor final
        for i in range(4,10,2):
            print("i={}".format(i),end=" ")#ciclo con valor inicial y valor final, y con parametros de saltos en aumento
        for i in range(12,3,-3):
            print("i={}".format(i))#ciclo con valor inicial y valor final, y con parametros de saltos de decremento
        
        
objFor=For()
objFor.usoFor()
