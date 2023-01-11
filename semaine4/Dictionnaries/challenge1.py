mot=input('Entrer un mot')
mon_dico= dict()

for i in range(len(mot)):
   mon_dico[mot[i]] = i
   print(mon_dico)

