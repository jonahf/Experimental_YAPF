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
                            if y else (z
                                       if z else z))

    # variable = xxxxxxxxx if xxxxxxxxx else (yyyyyyyyyyyy if yyyyyyyyyyyy else (zzzzzzzzz if zzzzzzzzz else zzzzzzzzz))
    variable = xxxxxxxxx if xxxxxxxxx else (yyyyyyyyyyyy
                                            if yyyyyyyyyyyy else
                                            (zzzzzzzzz
                                             if zzzzzzzzz else
                                             zzzzzzzzz))


def island_of_many_commas():
    big_ol_list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8,
        9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7,
        8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    ]

    # was: complicated_call([a(b).c],[a(b).c],b([c]).a(),f in a(b).c,aaaaaaaaaa)
    complicated_call([a(b).c],
                     [a(b).c],
                     b([c]).a(), f in a(b).c, aaaaaaaaaa)

    train_wreck_call(
        1, 2,
        function_call(), [4], 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5,
        6, 7, {8, 9, 0, 1, 2, 3, 4, 5, 6, 7}, 8, 9, 0, 1, 2, {
            3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3
        }, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        {0, 1, 2, 3, 4, 5, 6}, 7, 8, 9, 0)


def incomprehensionable():
    # a zoo of comprehensions to play with.
    d = {n: n**2
         for n in range(5)}
    d = {n: True
         for n in range(5)}

    total_length = sum(
        len(x)
        for x, y in zip(strings, validity)
        if y)

    californian_name_lengths = sum(
        len(name)
        for name, zip_code in zip(names, zip_codes)
        if zip_code in california_zip_codes)

    some_dict = {
        k: v
        for k, v in [('a', 1), ('b',
                                2)]
        if v % 2 == 0
    }

    set_of_vowels = {upper(i)
                     for i in sentence
                     if i in vowels}

    birthdays = (day for day in list_of_days
                 if day.has_birthday())
    birthdays = [day for day in list_of_days
                 if day.has_birthday()]

    zvals = [
        zvals[i]
        for i, (a, b) in enumerate(pairs(zvals))
        if b - a >= threshold
    ]

    not_terribly_pythonic = [
        i * 2
        for i in [j + 1
                  for j in range(20)
                  if (j % 3) == 0]
        if i * i > 19
    ]

    for row in [[i * j
                 for i in range(1, 8)]
                for j in range(1, 4)]:
        print row

    return ("\n".join(
        str(i) + ":\t" + "*" * a.count(i)
        for i in range(min(a), max(a) + 1)))


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
                                            for y in iterable
                                            if cond(y)]
                                if cond(x)
                            ]

                            test_comp = [
                                xxxxxxxxxxx
                                for xxxxxxxxxxx in [
                                    yyyyyyyyyy for yyyyyyyyyy in iterable
                                    if cond(yyyyyyyyyy)
                                ]
                                if cond(xxxxxxxxxxx)
                            ]


class AClass(object):
    def list_comprehensions():
        # was: test_comp = [x for x in [y for y in iterable if cond(y)] if cond(x)]
        test_comp = [
            x for x in [y
                        for y in iterable
                        if cond(y)]
            if cond(x)
        ]

        # was: test_comp = [xxx for xxx in [yyy for yyy in iterable if cond(yyy)] if cond(xxx)]
        test_comp = [
            xxx for xxx in [yyy
                            for yyy in iterable
                            if cond(yyy)]
            if cond(xxx)
        ]

        # was: test_comp = [xxxxxx for xxxxxx in [yyyyyy for yyyyyy in iterable if cond(yyyyyy)] if cond(xxxxxx)]
        test_comp = [
            xxxxxx for xxxxxx in
            [yyyyyy for yyyyyy in iterable
             if cond(yyyyyy)]
            if cond(xxxxxx)
        ]

        # was: test_comp = [xxxxxxxxx for xxxxxxxxx in [yyyyyyyy for yyyyyyyy in iterable if cond(yyyyyyyy)] if cond(xxxxxxxxx)]
        test_comp = [
            xxxxxxxxx
            for xxxxxxxxx in
            [yyyyyyyy for yyyyyyyy in iterable
             if cond(yyyyyyyy)]
            if cond(xxxxxxxxx)
        ]

        # was: test_comp = [xxxxxxxxxxx for xxxxxxxxxxx in [yyyyyyyyyy for yyyyyyyyyy in iterable if cond(yyyyyyyyyy)] if cond(xxxxxxxxxxx)]
        test_comp = [
            xxxxxxxxxxx
            for xxxxxxxxxxx in [
                yyyyyyyyyy for yyyyyyyyyy in iterable
                if cond(yyyyyyyyyy)
            ]
            if cond(xxxxxxxxxxx)
        ]
