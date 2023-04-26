import time

def fibonacci (n):
    if n in num:
        return num[n]
    elif n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        num[n] = fibonacci(n-1) + fibonacci(n-2)
        return num[n]

num = {}

f_start = time.time()
span = 101
for i in range(0,span):
    #start = time.time()
    result = fibonacci(i)
    #end = time.time()
    #duration = end - start
    print(i, result)
f_end = time.time()
f_duration =f_end - f_start
print('Вычисление всех', span-1,'чисел заняло', f_duration,'секунды')
