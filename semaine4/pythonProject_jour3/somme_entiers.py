
def personne(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
personne(Rahima=20,Ouria=0)

mafonction = lambda s:s.upper()
print(mafonction("Moussa"))

def robe(*args):
    for i in args:
        print(i+2)
robe(4,7,9)

fonction_robe = lambda r:r+2
#print(fonction_robe(2))
d=[0,8,9]
s=map(fonction_robe,d)
print(list(s))

solution = tuple(map(lambda x: x + 2, d))
print(solution)