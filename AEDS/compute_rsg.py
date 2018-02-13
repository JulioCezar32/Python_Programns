#tris program is to be used to provide you RSG(Rendimento Semestral Global)
#O calculo é feito com base nas notas das disciplinas e seu determinado peso, variando de 0-5


x = int(input("Report the number of subjects you did \n"))
result = 0
heights = 0
def conceito(nota):
    while nota > 100 or nota < 0:
        print("Nota invalida\n")
        nota = int(input("Digite novamente uma nota válida\n"))
    if nota >= 90:
        return 5
    elif nota >= 80:
        return 4
    elif nota >= 70:
        return 3
    elif nota >= 60:
        return 2
    elif nota >= 40:
        return 1
    else:
        return 0
def credito(carga):
    while carga > 60 or carga < 20:
        print("Carga horária inválida\n")
        carga = int(input("Digite novamente uma carga horária válida\n"))
    return carga
for subject in range(x):
    a = int(input("Insert the number of credits of the subject number {0}\n".format(subject + 1)))
    valor_credito = credito(a)
    b = int(input("Insert the note obteined into subject number {0}\n".format(subject + 1)))
    valor_conceito = conceito(b)

    result = result + a * valor_conceito
    heights = heights + a
RSG = result/heights
print("You RSG in this semestre is {0}\n".format(RSG)) 
