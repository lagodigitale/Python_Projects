fruits=str(input("Entrer vos fruits preferes"))

favoris=fruits.split()
name=str(input("Entrer un nom de fruits"))
for i in range(0,len(favoris)):
    if name== favoris[i]:
        print("Favoris");

for i in range(0,len(favoris)):
    if name!= favoris[i]:
        print("Non Favoris");
