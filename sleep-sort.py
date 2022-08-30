from time import sleep
from threading import Timer


def sleepSort(values):
    result = []

    def add_(x):
        result.append(x)

    mx = values[0]
    for v in values:
        if mx < v : mx = v
        Timer(v, add_, [v]).start()
    sleep(mx + 1)
    return result


x = [3, 2, 4, 7, 3, 6, 8, 1]
if sleepSort(x) == sorted(x):
    print('Sorted Array -', sleepSort(x))
else:
    print('Array {} not able to sort.'.format(x))
