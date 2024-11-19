class Horario:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto
    def incrementa_hora(self):
        if self.hora == 23:
            self.hora = 0
        else:
            self.hora += 1
    def decrementa_hora(self):
        if self.hora == 0:
            self.hora = 23
        else:
            self.hora -= 1
    def decrementa_minuto(self):
        if self.minuto == 0:
            if self.hora == 0:
                self.hora = 23
            else:
                self.hora -= 1
            self.minuto = 59
        else:
            self.minuto -= 1
    def incrementa_minuto(self):
        if self.minuto == 59:
            self.incrementa_hora()
            self.minuto = 0
        else:
            self.minuto += 1
    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"
    def periodo_dia(self):
        if self.hora < 12:
            return "AM"
        else:
            return "PM"
horario = Horario(11, 00)
Hora = ('Hora atual')
print(Hora), print (horario) 
Hora = ('Incrementado 1:00 hora da atual')
print(Hora)
horario.incrementa_hora(), print(horario) 
Hora = ('Decrementado 1:00 hora')
print(Hora)
horario.decrementa_hora(), print(horario) 
Hora = ('Decrementado 1:00 minuto da atual')
print(Hora)
horario.decrementa_minuto(), print(horario) 
Hora = ('Incrementado 1:00 minuto ')
print(Hora)
horario.incrementa_minuto(), print(horario)
Periodo = ('Periodo')
print(Periodo)
print(horario.periodo_dia())