magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    for i in magician_names:
        print(i)

show_magicians(magician_names)


def make_great():
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    for i in range(len(magician_names)):
        m='The great' + magician_names[i]
        
        print(m)
make_great()