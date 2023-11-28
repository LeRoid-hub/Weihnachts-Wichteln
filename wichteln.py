import random


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


teilnehmer = ["Jan", "Paul", "Niklas", "Tom", "Timo", "Collin"]
random.shuffle(teilnehmer)

shuffelt = teilnehmer.copy()
swapPositions(teilnehmer, 0, 2)
swapPositions(teilnehmer, 3, 4)
teilnehmer.reverse()


for i in range(len(shuffelt)):
    print(shuffelt[i], "wichtelt für", teilnehmer[i])
    open(shuffelt[i] + ".txt", "w").write("Du wichtelst für: " + teilnehmer[i])
