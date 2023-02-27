file = open('alumnos.txt', 'w')

nombres = file.readline()
print(nombres)
file.close()

for items in nombres:
    print(items, end="")
    
