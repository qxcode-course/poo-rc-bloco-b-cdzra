class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

class Notebook:
    def __init__(self, minutos : int = 0 ):
        self.__ligado: bool = False
        self.__bateria: Bateria  | None = None
        self.__carregador: Carregador | None = None
        self.minutos = minutos

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

    def usar(self, minutos: int):
        if self.__ligado == False:
            print("fail: notebook desligado")
            return
        else:
            self.minutos = minutos
            return
        
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
        elif args[0] == "use":
            print(f"Usado por {notebook.usar(args[1])} minutos")
main()