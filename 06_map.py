import copy


obstacle = '#'
map = []

idx = 0
with open('./input_06.txt', 'r') as f:
    for line in f:
        line = [s for s in line.strip()]
        if '^' in line:
            g_c = [idx, line.index('^')]
        map.append(line)
        idx += 1


# m_s = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """
#
# map = [
#     [s for s in line.strip()] for line in m_s.strip().split('\n')
# ]
# for idx, line in enumerate(map):
#     if '^' in line:
#         g_c = [idx, line.index('^')]


def single_move(guard, x, y, map):
    h, w = len(map), len(map[0])
    if guard == '^':
        if y - 1 >= 0 and map[y - 1][x] == obstacle:
            return turn(guard), x, y
        return guard, x, y - 1
    if guard == 'v':
        if y + 1 < h and map[y + 1][x] == obstacle:
            return turn(guard), x, y
        return guard, x, y + 1
    if guard == '<':
        if x - 1 >= 0 and map[y][x - 1] == obstacle:
            return turn(guard), x, y
        return guard, x - 1, y
    if guard == '>':
        if x + 1 < w and map[y][x + 1] == obstacle:
            return turn(guard), x, y
        return guard, x + 1, y


def turn(guard):
    turn_dict = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return turn_dict[guard]


# def move(guard, x, y, map):
#     hist = set()
#     h, w = len(map), len(map[0])
#
#     while True:
#         hist.add((x, y))
#         guard, x, y = single_move(guard=guard, x=x, y=y, map=map)
#         if y >= h or y < 0 or x >= w or x < 0:
#             return len(hist)


def probe(guard, x, y, map, hist, forbid_coord):
    h, w = len(map), len(map[0])

    if guard == '^' and y - 1 >= 0 and map[y - 1][x] == obstacle:
        return False
    if guard == 'v' and y + 1 < h and map[y + 1][x] == obstacle:
        return False
    if guard == '<' and x - 1 >= 0 and map[y][x - 1] == obstacle:
        return False
    if guard == '>' and x + 1 < w and map[y][x + 1] == obstacle:
        return False

    hist_copy = copy.deepcopy(hist)
    _, jab_x, jab_y = single_move(guard=guard, x=x, y=y, map=map)
    if (jab_x, jab_y) == forbid_coord:

        return False
    guard = turn(guard)
    while True:
        if (x, y) not in hist_copy:
            hist_copy[(x, y)] = set()

        hist_copy[(x, y)].add(guard)

        guard, x, y = single_move(guard=guard, x=x, y=y, map=map)

        if y >= h or y < 0 or x >= w or x < 0:
            return False
        if hist_copy and guard in hist_copy.get((x, y), set()):
            return True


def loop(guard, x, y, map):
    hist = {}
    h, w = len(map), len(map[0])

    forbid_coord = (x, y)

    loop_count = 0
    while True:
        if (x, y) not in hist:
            hist[(x, y)] = set()
        hist[(x, y)].add(guard)

        if guard == '^' and y - 1 >= 0 and map[y - 1][x] == obstacle:
            guard = turn(guard)
            continue
        if guard == 'v' and y + 1 < h and map[y + 1][x] == obstacle:
            guard = turn(guard)
            continue
        if guard == '<' and x - 1 >= 0 and map[y][x - 1] == obstacle:
            guard = turn(guard)
            continue
        if guard == '>' and x + 1 < w and map[y][x + 1] == obstacle:
            guard = turn(guard)
            continue

        probe(guard, x, y, map, hist, forbid_coord)

        if probe(guard, x, y, map, hist, forbid_coord):
            print(x, y, guard, loop_count)
            loop_count += 1
        guard, x, y = single_move(guard=guard, x=x, y=y, map=map)
        if y >= h or y < 0 or x >= w or x < 0:
            return loop_count


res = loop(guard='^', x=g_c[1], y=g_c[0], map=map)
print(res)
