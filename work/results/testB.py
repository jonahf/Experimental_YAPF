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


class foo(object):
    def f(self):
        return 37 * -+2

    def g(self, x, y=42):
        return y


def f(a):
    aaaaaaaaaaaaaaaaa.bbbbbbbbbbbbbbbbb(ccccccccc, ddddddddddddd,
                                        eeeeeeeeeeeee, fffffffffffff)


def conditional_zoo(a):
    # thing = x if x else y
    thing = x if x else y

    # variable = x if x else (y if y else (z if z else z))
    variable = x if x else (y
                            if y else (z if z else z))

    # variable = xxxxxxxxx if xxxxxxxxx else (yyyyyyyyyyyy if yyyyyyyyyyyy else (zzzzzzzzz if zzzzzzzzz else zzzzzzzzz))
    variable = xxxxxxxxx if xxxxxxxxx else (
        yyyyyyyyyyyy
        if yyyyyyyyyyyy else (zzzzzzzzz if zzzzzzzzz
                              else zzzzzzzzz))


def island_of_many_commas():
    big_ol_list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
        6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
        6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    ]

    # was: complicated_call([a(b).c],[a(b).c],b([c]).a(),f in a(b).c,aaaaaaaaaa)
    complicated_call([a(b).c], [a(b).c],
                     b([c]).a(), f in a(b).c,
                     aaaaaaaaaa)

    train_wreck_call(
        1, 2,
        function_call(), [4], 5, 6, 7, 8, 9, 0, 1, 2,
        3, 4, 5, 6, 7, {8, 9, 0, 1, 2, 3, 4, 5, 6,
                        7}, 8, 9, 0, 1, 2,
        {3, 4, 5, 6, 7, 8, 9, 0, 1, 2,
         3}, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7,
        8, 9, {0, 1, 2, 3, 4, 5, 6}, 7, 8, 9, 0)


class VeryIndented(object):
    def list_comprehensions():
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            # now that we're indented a lot, let's see what happens

                            test_comp = [
                                x for x in [y
                                            for y in iterable if cond(y)]
                                if cond(x)
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
        # was: test_comp = [x for x in [y for y in iterable if cond(y)] if cond(x)]
        test_comp = [
            x for x in [y
                        for y in iterable if cond(y)]
            if cond(x)
        ]

        # was: test_comp = [xxx for xxx in [yyy for yyy in iterable if cond(yyy)] if cond(xxx)]
        test_comp = [
            xxx for xxx
            in [yyy
                for yyy in iterable if cond(yyy)]
            if cond(xxx)
        ]

        # was: test_comp = [xxxxxx for xxxxxx in [yyyyyy for yyyyyy in iterable if cond(yyyyyy)] if cond(xxxxxx)]
        test_comp = [
            xxxxxx
            for xxxxxx in [
                yyyyyy for yyyyyy in iterable
                if cond(yyyyyy)
            ] if cond(xxxxxx)
        ]

        # was: test_comp = [xxxxxxxxx for xxxxxxxxx in [yyyyyyyy for yyyyyyyy in iterable if cond(yyyyyyyy)] if cond(xxxxxxxxx)]
        test_comp = [
            xxxxxxxxx
            for xxxxxxxxx in [
                yyyyyyyy for yyyyyyyy in iterable
                if cond(yyyyyyyy)
            ] if cond(xxxxxxxxx)
        ]

        # was: test_comp = [xxxxxxxxxxx for xxxxxxxxxxx in [yyyyyyyyyy for yyyyyyyyyy in iterable if cond(yyyyyyyyyy)] if cond(xxxxxxxxxxx)]
        test_comp = [
            xxxxxxxxxxx
            for xxxxxxxxxxx in [
                yyyyyyyyyy for yyyyyyyyyy in iterable
                if cond(yyyyyyyyyy)
            ] if cond(xxxxxxxxxxx)
        ]
