class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome
        
    def getIdade(self):
        return self.__idade

    def setNome(self,value: str):
        self.__nome = value

    def setIdade(self, value: int):
        self.__idade = value

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"
    
class Moto:
    def __init__(self, potencia: int = 1):
        self.__potencia = potencia
        self.__tempo = 0
        self.__pessoa = None

    def __str__(self):
        if self.__pessoa != None:
            return f"power:{self.__potencia}, time:{self.__tempo}, person:({self.__pessoa})"
        else:
            return f"power:{self.__potencia}, time:{self.__tempo}, person:(empty)"

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa != None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def remover(self):
        if self.__pessoa == None:
            print("fail: empty motorcycle")
            return None
        aux = self.__pessoa
        self.__pessoa = None
        return aux
    
    def compTempo(self, tempo: int):
        self.__tempo += tempo

    def drive(self, timer: int):
        if self.__tempo == 0:
            print("fail: buy time first")
            return
        if self.__pessoa == None:
            print("fail: empty motorcycle")
            return
        if self.__pessoa.getIdade() > 10:
            print("fail: too old to drive")
            return
        if timer > self.__tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0
            return
        self.__tempo -= timer

    def honk(self):
        return f"P" + ("e" * self.__potencia) + "m"
    
def main():     
    moto = Moto()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
                break
        elif args[0] == "show":
                print(moto)
        elif args[0] == "init":
            potencia = int(args[1])
            moto = Moto(potencia)
        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa(nome, idade)
            moto.inserir(pessoa)
        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa != None:
                print(pessoa)
        elif args[0] == "buy":
            moto.compTempo(int(args[1]))
        elif args[0] == "drive":
            tempo = int(args[1])
            moto.drive(tempo)
        elif args[0] == "honk":
            print(moto.honk())
main()