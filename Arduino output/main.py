a = int(input('First input: '))

w = x = y = z = 0

if a == 0:
    w = x = y = z = "GREEN"
    print(w, x, y, z)
elif a == 1:
    w = y = "GREEN"
    x = z = "RED"
    print(w, x, y, z)
elif a == 2:
    w = y = "RED"
    x = z = "GREEN"
    print(w, x, y, z)
elif a == 3:
    w = y = "GREEN"
    x = z = "RED"
    print(w, x, y, z)
elif a == 4:
    w = y = "RED"
    x = z = "GREEN"
    print(w, x, y, z)

else:
    print('Error')

