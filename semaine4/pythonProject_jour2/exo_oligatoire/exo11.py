sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich","pastrami"]
for i in range(len(sandwich_orders)):
    if sandwich_orders[i] == 'pastrami':
        print('La charcuterie est à court de pastrami,')
        del(sandwich_orders[i])
print(sandwich_orders)
