def print_pairs(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            print(list[i], list[j])

def get_sum_all_subarrays(list):
    sum = 0
    n = len(list)
    for i in range(n):
        sum += list[i] * (i + 1) * (n - i)
    return sum

def check_if_num_exists(list, num):
    return num in list