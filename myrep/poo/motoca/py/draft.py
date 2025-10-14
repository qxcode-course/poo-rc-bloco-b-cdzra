class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    def setNome(self,value: str):
        self.__nome = value
    def __str__(self):
        return self.__nome
    
class Moto:
    def __init__(self):
        self.pessoa: Pessoa | None = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.pessoa != None:
            print("ja tem gente na moto")
            return False
        self.pessoa = pessoa
        return True

    def remover(self) -> Pessoa | None:
        if self.pessoa == None:
            print("moto vazia")
            return None
        aux = self.pessoa
        self.pessoa = None
        return aux
        
    def __str__(self):
        return f"moto: {self.pessoa}"
    
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
main()