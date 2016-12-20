import numpy as np
a1 = np.array([1, 2, 3, 4])
a1.flatten()
length = 4
for i in range(2**length):
    result = np.append(np.zeros(length - len(bin(i)[2:])), list(bin(i)[2:]), axis=0)
    result2 = result.astype(np.float)
    # print(type(result), type(a1))
    # for i in result2:
    #     print(type(i))
    print(np.multiply(a1, result2))

for i in a1:
    print(type(i))

# print(type(a1))
# print()