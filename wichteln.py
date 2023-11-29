import random


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


anzahl = int(input("Anzahl der Teilnehmer: "))
teilnehmer = []

for i in range(anzahl):
    teilnehmer.append(input(str(i+1) + ". Name: "))

random.shuffle(teilnehmer)

for i in range(len(teilnehmer)):
    if i == len(teilnehmer) - 1:
        open(teilnehmer[i] + ".txt", "w").write(teilnehmer[0])
    else:
        open(teilnehmer[i] + ".txt", "w").write(teilnehmer[i + 1])
