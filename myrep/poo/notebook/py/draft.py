class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False

    def getLigado(self):
        if self.__ligado == False:
            print("Status: Desligado")
            return
        if self.__ligado == True:
            print("Status: Ligado")
            return
        
    def setLigar(self):
        if self.__ligado == True:
            print("fail: notebook ja esta ligado")
            return
        self.__ligado = True

    def setDesligar(self):
        if self.__ligado == False:
            print("fail: notebook ja esta desligado")
            return
        self.__ligado = False

def main():
    notebook = Notebook()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.getLigado()
        elif args[0] == "ligar":
            notebook.setLigar()
        elif args[0] == "desligar":
            notebook.setDesligar()
main()