test = """
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
"""

test_eqs = []
for line in test.strip().split('\n'):
    eq = [int(line.split(': ')[0])]
    eq += list(map(int, line.split(': ')[1].split(' ')))
    test_eqs.append(eq)


eqs = []
with open('./input_07.txt', 'r') as f:
    for line in f:
        line = line.strip()
        eq = [int(line.split(': ')[0])]
        eq += list(map(int, line.split(': ')[1].split(' ')))
        eqs.append(eq)


def check_eq(eq):
    res = eq[0]

    i = 2
    operation_res = {eq[1]}
    while i < len(eq):
        add = set([num + eq[i] for num in operation_res])
        mul = set([num * eq[i] for num in operation_res])
        concat = set(
            [int(str(num) + str(eq[i])) for num in operation_res]
        )
        operation_res = add.union(mul).union(concat)
        i += 1

    if res in operation_res:
        return True
    return False


ans = 0
for eq in eqs:
    if check_eq(eq):
        ans += eq[0]

print(ans)