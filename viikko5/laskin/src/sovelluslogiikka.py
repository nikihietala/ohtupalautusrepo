class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.historia = []

    def _tallenna_historiaan(self):
        self.historia.append(self._arvo)

    def miinus(self, operandi):
        self._tallenna_historiaan()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._tallenna_historiaan()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._tallenna_historiaan()
        self._arvo = 0
    
    def kumoa(self):
        if self.historia:
            self._arvo = self.historia.pop()

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
