# python yapf work/testA.py | tee work/results/testA.py
if mytest:
    print True

test_comp = [
    x for x in [y
                for y in iterable if cond(y)]
    if cond(x)
]
test_comp = [
    x.method()
    for x in [y
              for y in iterable if cond(y)]
    if cond(x)
]
test_comp = [
    x for x in
    [y for y in [z for z in i
                 if z]
     if y]
    if x
]
test_comp = [
    xxxxxxxxx
    for xxxxxxxxx in [
        yyyyyyyyyy for yyyyyyyyyy in [
            zzzzzzzzzzzzz
            for zzzzzzzzzzzzz in iterable
            if zzzzzzzzzzzzz
        ] if yyyyyyyyyy
    ] if xxxxxxxxx
]
