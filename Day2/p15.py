size = 5  
for i in range(1, size + 1):
    print(" " * (size - i) + "* " * i)
for i in range(size - 1, 0, -1):
    print(" " * (size - i) + "* " * i)
