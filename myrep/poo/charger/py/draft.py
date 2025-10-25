class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getBateria(self):
        return f"{self.__carga}/{self.__capacidade}"
    
    def usar(self, minutos: int):
        self.__carga -= minutos
        if self.__carga < 0:
            self.__carga = 0

    def carregar(self, potencia: int, minutos: int):
        self.__carga += potencia * minutos
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def temCarga(self):
        return self.__carga > 0
    
class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia

    def getPotencia(self):
        return self.__potencia

class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria  | None = None
        self.__carregador: Carregador | None = None

    def status(self, minutos: int):
        if self.__ligado == True:
            status = "ligado"
            if self.__bateria:
                print(f"Notebook: {status} por {minutos} minutos, bateria: {self.__bateria.getBateria()}")
                return
            if self.__carregador:
                print(f"Notebook: {status} por {minutos} minutos, Carregador {self.__carregador.getPotencia()}W")
                return
            if self.__bateria and self.__carregador:
                print(f"Notebook: {status} por {minutos} minutos, Bateria: {self.__bateria.getBateria()}, Carregador {self.__carregador.getPotencia()}W")
                return
            else:
                print(f"Notebook: {status} por {minutos} minutos")
        else:
            status = "desligado"
            if self.__bateria:
                print(f"Notebook: {status}, bateria: {self.__bateria.getBateria()}")
                return
            if self.__carregador:
                print(f"Notebook: {status}, Carregador {self.__carregador.getPotencia()}W")
                return
            if self.__bateria and self.__carregador:
                print(f"Notebook: {status}, Bateria: {self.__bateria.getBateria()}, Carregador {self.__carregador.getPotencia()}W")
                return
            else:
                print(f"Notebook: {status}")
        
    def setLigar(self):
        if self.__bateria and self.__bateria.temCarga():
            self.__ligado = True
            print("msg: notebook ligado")
            return
        if self.__carregador:
            self.__ligado = True
            return
        else:
            print("fail: não foi possível ligar")

    def setDesligar(self):
        if self.__ligado == False:
            print("fail: notebook ja esta desligado")
            return
        self.__ligado = False
        print("msg: notebook desligado")

    def usar(self, minutos: int):
        if self.__ligado == False:
            print("fail: desligado")
            return
        if self.__bateria == None and self.__carregador == None:
            print("fail: sem bateria e sem carregador")
            self.__ligado = False
            return
        print(f"Usado por {minutos} minutos")
        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.getPotencia(), minutos)
            return
        if self.__bateria and not self.__carregador:
            self.__bateria.usar(minutos)
            if not self.__bateria.temCarga():
                print("fail: bateria zerada, notebook desligado")
                self.__ligado = False

    def setBateria(self,bateria: Bateria):
        self.__bateria = bateria
        print("msg: bateria conectada")

    def removeBateria(self):
        if self.__bateria:
            self.__bateria = None
            print("msg: bateria removida")
            return
        else:
            print("fail: sem bateria conectada")

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador

    def removeCarregador(self):
        if self.__carregador:
            self.__carregador = None
            print("msg: carregador removida")
            return
        else:
            print("fail: sem carregador conectado")
    

        
def main():
    notebook = Notebook()
    bateria = None
    carregador = None
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.status()
        elif args[0] == "bateria":
            capacidade = int(args[1])
            bateria = Bateria(capacidade)
            notebook.setBateria(bateria)
        elif args[0] == "removeBateria":
            notebook.removeBateria()
        elif args[0] == "set_charger":
            potencia = int(args[1])
            carregador = Carregador(potencia)
            notebook.setCarregador(carregador)
        elif args[0] == "removeCarregador":
            notebook.removeCarregador()
        elif args[0] == "turn_on":
            notebook.setLigar()
        elif args[0] == "desligar":
            notebook.setDesligar()
        elif args[0] == "use":
            minutos = int(args[1])
            notebook.usar(minutos)
main()