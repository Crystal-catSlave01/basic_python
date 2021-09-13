def input():
    set_h, set_m = map(int, input().split())
    h, m = set_h, set_m
    min = 60
    alram = 45

    if set_m - alram < 0:
        m = min + (set_m - alram)
        h -= 1

        if h < 0:
            h = 23
        print(h,m)

    else:
        print(h,m-alram)

input()