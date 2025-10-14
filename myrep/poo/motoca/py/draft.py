class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return self.nome
class Moto:
    def __init__(self):
        self.pessoa: Pessoa | None = None

    def inserir(self, pessoa: Pessoa):
        if self.pessoa != None:
            print("ja tem gente na moto")
            return
        self.pessoa = pessoa
        return False

    def remover(self) -> Pessoa | None:
        aux = self.pessoa
        self.pessoa = None
        return aux
        
def main()        
        moto = Moto()
        
        while True:
            line = input()
            print("$" + line)
            args = line.split(" ")

            if args[0] == "end":
                break
            elif args[0] == "show":
                print(moto)