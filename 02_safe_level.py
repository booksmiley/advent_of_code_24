import numpy as np

count = 0


def is_safe(nums):
    gradiant = np.diff(nums)
    if (np.all(gradiant > 0) or np.all(gradiant < 0)) and max(abs(gradiant)) <= 3:
            return True
    return False


def fix(nums):
    for i in range(len(nums)):
        temp = nums.copy()
        temp.pop(i)
        if is_safe(temp):
            return True
    return False


with open('./input_02.txt', 'r') as f:
    for line in f:
        nums = [int(s) for s in line.strip().split(' ')]
        if is_safe(nums):
            count += 1
        else:
            if fix(nums):
                count += 1

print(count)
