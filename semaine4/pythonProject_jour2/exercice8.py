import psycopg2

gout=input('Entrer des garnitures de pizza')

quitter="q"
i=0

while gout != quitter:
    gout = input('Entrer des garnitures de pizza')
    i = i + 1

print("Nous ajouterons",{gout}, "pizza sur ton plat et ca coutera,",i*12.5,"$")