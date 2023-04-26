def recursive_compute_sum(list):
    if len(list) == 0:
        return 0
    else:
        first = list[0]
        rest = list[1:]
        sum_list = first + recursive_compute_sum(rest)
        return sum_list



test = [10, 13, 39, 14, 41, 9, 3]
num = recursive_compute_sum(test)
print('Сумма равна', num)

