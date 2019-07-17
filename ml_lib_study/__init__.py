res = [None] * 20


def print_res():
    for i in range(len(res)):
        if res[i] is not None:
            print('res[{}]:\n'.format(i), res[i], '\n')
