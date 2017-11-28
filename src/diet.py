from __future__ import print_function

fmt = '''{}

        - {}

'''
if __name__ == '__main__':
    items = []

    with(open('diet.txt', 'r')) as ipt:
        for line in ipt:
            d = line.split()
            items.append(fmt.format(*d))

    txt = "%\n".join(items)
    with(open('../data/diet', 'w')) as opt:
        opt.write(txt)
