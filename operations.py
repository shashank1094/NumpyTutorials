import numpy as np

a = np.arange(0, 25, 5)
b = np.arange(5)

print(a - b)
print(a + 1)
print(a > 10)

a1 = np.array([[[4, 92],
                [68, 6],
                [48, 17]],

               [[64, 61],
                [33, 81],
                [89, 30]]])
print(a1, a1.argmax(axis=0))
print("SORT", np.argsort(a1, axis=0))
print(np.mean(a1))

