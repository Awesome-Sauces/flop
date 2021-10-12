# Keywords
from typing import Set


Keywords = ['InstanceFlop', 'SettingsInst']
InstanceFlop = ['True', 'False']
SettingsInst = ['Matrice=True', 'PIlen=']

with open('project.flop') as f:
    lines = f.readlines()
for a in range(len(lines)):
    for b in range(len(Keywords)):
        if Keywords[b] in lines[a]:
            if Keywords[b] == Keywords[0]:
                if 'True' in lines[a]:
                    print("InstanceFlop Created!")
                elif InstanceFlop[1] in lines[a]:
                    quit()
                else:
                    raise SyntaxError(lines[a] + " <--- Fault in line " + str(a + 1))
            elif Keywords[b] == Keywords[1]:
                for c in range(len(SettingsInst)):
                    if SettingsInst[c] in lines[a]:
                        print("Succes!")
