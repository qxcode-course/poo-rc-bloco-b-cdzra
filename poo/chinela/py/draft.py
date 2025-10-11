class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getSize(self) -> int:
        return self.__tamanho
    def setSize(self, valor: int):
        if valor > 19 or valor < 51:
            self.__tamanho = valor
            return
        else:
            print("fail: o valor digitado nao corresponde a um par de chinela")

def main():
    chinela = Chinela()
    while chinela.getSize() == 0:
        tamanho = int(input(": "))
        chinela.setSize(tamanho)
    print("parabens, voce comprou uma chinela de tamanho ", chinela.getSize())
main()