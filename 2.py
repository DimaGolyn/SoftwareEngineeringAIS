def fibonacci(n):
    a, b = 1, 1
    with open('fibonacci.txt', 'w') as file:
         for _ in range(n):
             file.write(str(a) + '\n')
             a, b = b, a + b
             yield a
print(list(fibonacci(200))[199])