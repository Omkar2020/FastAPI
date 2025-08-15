def even_numbers():
    for num in range(0,20):
        if num % 2 == 0:yield num
for even in even_numbers():
    print(even)


