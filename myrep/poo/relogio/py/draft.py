class Relogio:
    def __init__(self, hora: int, minuto: int, segundo: int):
        self.__hora: int = hora
        self.__min: int = minuto
        self.__seg: int = segundo

    def __str__(self):
        return f"{self.__hora:02d}:{self.__min:02d}:{self.__seg:02d}"
    
    