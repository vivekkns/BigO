def find_log(num):
    if num > 1:
        return 1 + find_log(num/2)
    else:
        return 0


def find_sqrt(num):
    i = 1
    while i*i <= num:
        i += 1
    return i-1

if __name__ == '__main__':

    print('lg(64)', find_log(64))
    print('sqrt(99)', find_sqrt(100))
