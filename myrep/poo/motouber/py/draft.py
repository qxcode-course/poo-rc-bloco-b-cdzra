class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome
    
    def getDinheiro(self):
        return self.__dinheiro
    
    def pagar(self, value: int):
        if value > self.__dinheiro:
            self.__dinheiro = 0
            return
        self.__dinheiro -= value

    def receber(self, value: int):
        self.__dinheiro += value

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"
    
    def setDinheiro(self, dinheiro:int) -> None:
        self.__dinheiro = dinheiro

class Moto:
    def __init__(self):
        self.__custo = 0
        self.__passageiro = None
        self.__motorista = None

    def setDriver(self, nome: str, dinheiro: int):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome: str, dinheiro: int):
        if self.__motorista == None:
            print("fail: no driver in the moto")
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, km: int):
        if self.__passageiro == None:
            print("fail: no passenger in the moto")
            return
        self.__custo += km

    def left(self):
        if self.__passageiro != None:
            aux = self.__passageiro
            self.__passageiro.pagar(self.__custo)
            if self.__passageiro.getDinheiro() <= 0:
                self.__passageiro.setDinheiro(0)
                print("fail: Passenger does not have enough money")
            self.__motorista.receber(self.__custo)
            self.__custo = 0
            self.__passageiro = None
            return aux
        
    def __str__(self):
            return f"Cost: {self.__custo}, Driver: {self.__motorista}, Passenger: {self.__passageiro}"
    
def main():
    moto = Moto()
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            moto.setDriver(args[1], int(args[2]))
        elif args[0] == "setPass":
            moto.setPass(args[1], int(args[2]))
        elif args[0] == "drive":
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            pessoa = moto.left()
            print(f"{pessoa} left")
main()
