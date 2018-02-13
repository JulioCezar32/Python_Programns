#tris program is to be used to provide you RSG(Rendimento Semestral Global)
#The calculation is done based in your results in each subject applying the respective weight

x = int(input("Report the number of subjects you did \n"))
result = 0
heights = 0
def concept(note):
    while note > 100 or note < 0:
        print("Invalid note\n")
        note = int(input("Type again your note\n"))
    if note >= 90:
        return 5
    elif note >= 80:
        return 4
    elif note >= 70:
        return 3
    elif note >= 60:
        return 2
    elif note >= 40:
        return 1
    else:
        return 0
def credito(carga):
    while carga > 60 or carga < 20:
        print("Invalid course load \n")
        carga = int(input("Type again a valid course load\n"))
    return carga
for subject in range(x):
    a = int(input("Insert the number of credits of the subject number {0}\n".format(subject + 1)))
    valor_credito = credito(a)
    b = int(input("Insert the note obteined into subject number {0}\n".format(subject + 1)))
    valor_concept = concept(b)

    result = result + a * valor_concept
    heights = heights + a
RSG = result/heights
print("You RSG in this semestre is {0}\n".format(RSG))
