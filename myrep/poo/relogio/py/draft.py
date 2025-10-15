class Relogio:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora: int = 0
        self.__min: int = 0
        self.__seg: int = 0
        self.setHora(hora)
        self.setMin(minuto)
        self.setSeg(segundo)

    def __str__(self):
        return f"{self.__hora:02d}:{self.__min:02d}:{self.__seg:02d}"

    def getHora(self) -> int:
        return self.__hora

    def getMin(self) -> int:
        return self.__min

    def getSec(self) -> int:
        return self.__seg

    def setHora(self,value: int):
        if value > 23 or value < 0:
            print("fail: hora invalida")
            return
        self.__hora = value

    def setMin(self,value: int):
        if value > 59 or value < 0:
            print("fail: minuto invalido")
            return
        self.__min = value

    def setSeg(self,value: int):
        if value > 59 or value < 0:
            print("fail: segundo invalido")
            return
        self.__seg = value

    def initHora(self,value: int):
        if value > 23 or value < 0:
            print("fail: hora invalida")
            self.__hora = 0
            return
        self.__hora = value

    def initMin(self,value: int):
        if value > 59 or value < 0:
            print("fail: minuto invalido")
            self.__min = 0
            return
        self.__min = value

    def initSeg(self,value: int):
        if value > 59 or value < 0:
            print("fail: segundo invalido")
            self.__seg = 0
            return 
        self.__seg = value

    def nextSeg(self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
        if self.__min > 59:
            self.__min = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0

def main():
    relogio = Relogio(0, 0, 0)
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            relogio.setHora(int(args[1]))
            relogio.setMin(int(args[2]))
            relogio.setSeg(int(args[3]))
        elif args[0] == "init":
            relogio.initHora(int(args[1]))
            relogio.initMin(int(args[2]))
            relogio.initSeg(int(args[3]))
        elif args[0] == "next":
            relogio.nextSeg()

main()