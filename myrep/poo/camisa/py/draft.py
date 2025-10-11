class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getSize(self) -> str:
        return self.__tamanho
        
    def setSize(self, valor: str):
        if valor == "PP" or valor == "P" or valor == "M" or valor == "G" or valor == "GG" or valor == "XG":
            self.__tamanho = valor
            return
        else:
            print("fail: o valor digitado nao corresponde a um tamanho de camisa")

def main():
    camisa = Camisa()
    while camisa.getSize() == "":
        print("digite o seu tamanho de camisa")
        tamanho = str(input(": "))
        camisa.setSize(tamanho)
    print("parabens, voce comprou uma camisa de tamanho ", camisa.getSize())
main()