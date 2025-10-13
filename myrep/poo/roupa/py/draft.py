class Roupa:
    def __init__(self):
        self.__tamanho: str = ""

    def getSize(self) -> str:
        return self.__tamanho
    
    def setSize(self,valor: str):
        if valor in ["PP","P","M","G","GG","XG"]:
            self.__tamanho = valor
            return
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

def main():
    roupa = Roupa()
    while roupa.getSize() == "":
        line = input()
        print("$" + line)
        args: list[str] = line.split()

        if len(args) == 0:
            continue
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(f"size: ({roupa.getSize()})")
        elif args[0] == "size":
            if len(args) > 1:
                roupa.setSize(args[1])
            else:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
main()