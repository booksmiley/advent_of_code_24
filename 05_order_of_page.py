updates = [
    [75,47,61,53,29],
    [97,61,53,29,13],
    [75,29,13],
    [75,97,47,61,53],
    [61,13,29],
    [97,13,75,29,47],
]

order = """
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13
"""
order = [tuple(map(int, x.split('|'))) for x in order.strip().split('\n')]


order = []
updates = []
with open('./input_05.txt', 'r') as f:
    for line in f:
        if '|' in line:
            a, b = map(int, line.strip().split('|'))
            order.append((a, b))
        elif line.strip():
            updates.append([int(x) for x in line.strip().split(',') if x])


def safety_check(update, order):
    update_map = {x: i for i, x in enumerate(update)}
    for check in order:
        a, b = check
        if update_map.get(a, -1) > update_map.get(b, len(update)):
            return False
    return True


def fix_order(update, order):
    for j in range(len(update), 0, -1):
        for i in range(j-1):
            if (update[i], update[i+1]) in order:
                continue
            elif (update[i+1], update[i]) in order:
                update[i], update[i+1] = update[i+1], update[i]
            else:
                continue
    return update[len(update)//2]

count = 0
m_p = 0
for update in updates:
    if not safety_check(update, order):
        # m_p += update[len(update)//2]
        m_p += fix_order(update, order)
        count += 1

print(m_p)
print(count)