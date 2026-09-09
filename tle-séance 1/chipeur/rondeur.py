from bri import defiler
from filature import enfiler
from file_dattente import file

File = file(6)
print(File)

enfiler(File, 1)
print(File)

enfiler(File, 2)
print(File)

enfiler(File, 3)
print(File)

enfiler(File, 4)
print(File)

enfiler(File, 5)
print(File)

enfiler(File, 6)
print(File)

print(defiler(File))
print(File)

enfiler(File, 66)
print(File)

print(defiler(File))
print(File)

# retour ./oui.sh
