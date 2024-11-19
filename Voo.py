class Voo:
    def __init__(self, numero, horario):
        self.numero = numero
        self.horario = horario
        self.assentos = ['-'] * 100
    def getProximoAssento(self):
        for i, assento in enumerate(self.assentos):
            if assento == '-':
                return i + 1
        return None
    def verificarAssento(self, numassento):
        return self.assentos[numassento - 1] == 'X'
    def ocupar(self, numassento):
        if self.verificarAssento(numassento):
            return False
        self.assentos[numassento - 1] = 'X'
        return True
    def getVagas(self):
        return self.assentos.count('-')
    def getVoo(self):
        return self.numero
    def getHoraVoo(self):
        return self.horario
    def getMapaAssentos(self):
        mapa = ''
        for i in range(100):
            if i % 25 == 0:
                mapa += '\n'
            if self.assentos[i] == 'X':
                mapa += 'X'
            else:
                mapa += '-'
        return mapa
voo = Voo('Voo nº 007', 'Saida: 26/02/2023 as 10:00')
print(voo.getVoo()), print(voo.getHoraVoo()), print(voo.getProximoAssento()) 
print(voo.ocupar(2)), print(voo.ocupar(4)), print(voo.ocupar(7)) 
print(voo.ocupar(8)), print(voo.ocupar(13)), print(voo.ocupar(24)) 
print(voo.ocupar(27)), print(voo.ocupar(32)), print(voo.ocupar(33)) 
print(voo.ocupar(38)), print(voo.ocupar(49)), print(voo.ocupar(63)) 
print(voo.ocupar(74)), print(voo.verificarAssento(1)) 
print(voo.getVagas()), print(voo.getMapaAssentos()) 
