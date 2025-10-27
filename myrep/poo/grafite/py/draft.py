class Grafite:
    def __init__(self, calibre: float, hardness: str, size: int):
        self.__calibre = calibre
        self.__hardness = hardness
        self.__size = size

    def getCalibre(self):
        return self.__calibre
    
    def getHardness(self):
        return self.__hardness
    
    def getSize(self):
        return self.__size

    def setSize(self, size:int):
        self.__size = size

    def usePerSheet(self):
        gastos = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return gastos.get(self.__hardness, 0)
    
    def __str__(self):
        return f"{self.__calibre:.1f}:{self.__hardness}:{self.__size}"
    
class Pencil:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__lead = None
        
    def hasGrafite(self) -> bool:
        return self.__lead != None
    
    def inserir(self, grafite: Grafite):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if grafite.getCalibre() != self.__calibre:
            print("fail: calibre incompativel")
            return
        self.__lead = grafite

    def remover(self):
        if self.hasGrafite():
            self.__lead = None
            return
        print("fail: nao existe grafite")

    def write(self):
        if self.hasGrafite() == False:
            print("fail: nao existe grafite")
            return
        if self.__lead.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        gasto = self.__lead.usePerSheet()
        newSize = self.__lead.getSize() - gasto
        if newSize < 10:
            self.__lead.setSize(10)
            print("fail: folha incompleta")
            return
        self.__lead.setSize(newSize)

    def __str__(self):
        if self.hasGrafite():
            return f"calibre: {self.__calibre:.1f}, grafite: [{self.__lead}]"
        return f"calibre: {self.__calibre:.1f}, grafite: null"
    
def main():
    lapiseira = None
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Pencil(calibre)
        elif args[0] == "insert":
            esp = float(args[1])
            dur= str(args[2])
            tam = int(args[3])
            grafite = Grafite(esp, dur, tam)
            lapiseira.inserir(grafite)
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.write()
main()