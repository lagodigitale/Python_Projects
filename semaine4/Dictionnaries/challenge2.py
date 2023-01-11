items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20
}

wallet = 100

f=[]
for values in items_purchase.items():
  f=items_purchase.values()

for i in f:
  if int(wallet) > i:
    print("Vous pouvez acheter cet article")
  else:
    print("Vous ne pouvez pas acheter cet article")
