import numpy as np

array_1, array_2 = np.loadtxt('./input_01.txt', unpack=True)

array_1.sort()
array_2.sort()

minimal_distance = sum(abs(array_2 - array_1))

print(minimal_distance)

freq_dict = {}
for num in array_2:
    if num not in freq_dict:
        freq_dict[num] = 1
    else:
        freq_dict[num] += 1

score = 0
for num in array_1:
    score += freq_dict.get(num, 0) * num

print(score)