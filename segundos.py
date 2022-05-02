entradaSegundos = input("Por favor, entre com o número que deseja converter: ")
totalSegundos = int(entradaSegundos)

dias = (totalSegundos // 86400)
segundos = (totalSegundos % 86400)
horas = (segundos // 3600)
segundosRestantes = (segundos % 3600)
minutos = (segundosRestantes // 60)
segundosRestantesFinal = (segundosRestantes % 60)

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosRestantesFinal, "segundos.")