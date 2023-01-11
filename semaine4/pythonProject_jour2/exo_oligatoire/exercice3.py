basket = ["Banana", "Apples", "Oranges","Pommes", "Blueberries"];

basket.remove("Banana")
#basket.remove("Banana")
print(basket)
basket.insert(0,"Pommes")
print(basket)
basket.append("Kiwi")
print(basket)
x="Pommes"
k=0
for i in basket:
    if i==x:
        k=k+1
print("Il y a ",k,"pommes dans le panier")
basket.clear()
print(basket)



