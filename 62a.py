#nije moje rjesenje, jako brzo se izvodi
from collections import defaultdict


def euler62():
    i = 1
    cube_map = defaultdict(list)
    while True:
        key = ''.join(sorted(str(i**3)))
        cube_map[key].append(i**3)
        if len(cube_map[key]) >= 5:
            print cube_map[key]
            break
        i += 1

euler62()
