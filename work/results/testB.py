# python yapf work/testB.py | tee work/results/testB.py

x = {
    'a': 37,
    'b': 42,
    'c': 927
}
x = {
    'aaaaaaaaaaaaaaa': 37,
    'bbbbbbbbbbbbbbb': 42,
    'cccccccccccc': 927,
    'xxx': 37,
    'xxxxxxxxxxxxxx': 42,
    'xxxxxx': 927
}

y = 'hello ' 'world'
z = 'hello ' + 'world'
a = 'hello {}'.format('world')

big_ol_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
    6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
    6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0
]

big_ol_call(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3,
            4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6,
            7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2,
            3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
            6, 7, 8, 9, 0)

big_ol_call(1, 2,
            function_call(), [4], 5, 6, 7, 8, 9,
            0, 1, 2, 3, 4, 5, 6, 7, {
                8, 9, 0, 1, 2, 3, 4, 5, 6, 7
            }, 8, 9, 0, 1, 2, {
                3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3
            }, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
            6, 7, 8, 9, {0, 1, 2, 3, 4, 5,
                         6}, 7, 8, 9, 0)


class foo(object):
    def f(self):
        return 37 * -+2

    def g(self, x, y=42):
        return y


def f(a):
    if a == 3 and a > 4 or a < 30:
        aaaaaaaaaaaaaaaaa.bbbbbbbbbbbbbbbbb(ccccccccc, ddddddddddddd,
                                            eeeeeeeeeeeee, fffffffffffff)

    thing = x if x else y
    variable = xxxxxxxxx if xxxxxxxxx else (
        yyyyyyyyyyyy
        if yyyyyyyyyyyy else (zzzzzzzzz if zzzzzzzzz
                              else zzzzzzzzz))
    variable = x if x else (y
                            if y else (z
                                       if z else z))
    return [[37 + -+a[42 - x:y**3]]]


class VeryIndented(object):
    def list_comprehensions():
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            test_comp = [
                                x for x in [y for y in iterable
                                            if cond(y)] if cond(x)
                            ]
                            test_comp = [
                                xxxxxxxxxxx
                                for xxxxxxxxxxx in [
                                    yyyyyyyyyy for yyyyyyyyyy in iterable
                                    if cond(yyyyyyyyyy)
                                ] if cond(xxxxxxxxxxx)
                            ]


class AClass(object):
    def list_comprehensions():
        test_comp = [
            x for x in [y for y in iterable
                        if cond(y)] if cond(x)
        ]

        test_comp = [
            xxx for xxx in
            [yyy for yyy in iterable
             if cond(yyy)] if cond(xxx)
        ]

        test_comp = [
            xxxxxx
            for xxxxxx in [
                yyyyyy for yyyyyy in iterable
                if cond(yyyyyy)
            ] if cond(xxxxxx)
        ]

        test_comp = [
            xxxxxxxxx
            for xxxxxxxxx in [
                yyyyyyyy for yyyyyyyy in iterable
                if cond(yyyyyyyy)
            ] if cond(xxxxxxxxx)
        ]

        test_comp = [
            xxxxxxxxxxx
            for xxxxxxxxxxx in [
                yyyyyyyyyy for yyyyyyyyyy in iterable
                if cond(yyyyyyyyyy)
            ] if cond(xxxxxxxxxxx)
        ]
