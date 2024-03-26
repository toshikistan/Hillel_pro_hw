# 2. Створити frange ітератор. Який буде працювати з float or Decimal.

# class frange:
#     pass

# for i in frange(1, 100, 3.5):
#     print(i)

# має вивести

# 1
# 4.5
# 8.0
# ...


# Перед здачею перевірти тести чи проходять:

# assert(list(frange(5)) == [0, 1, 2, 3, 4])
# assert(list(frange(2, 5)) == [2, 3, 4])
# assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
# assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
# assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
# assert(list(frange(1, 5)) == [1, 2, 3, 4])
# assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
# assert(list(frange(0, 0)) == [])
# assert(list(frange(100, 0)) == [])

# print('SUCCESS!')

class frange:
    def __init__(self, first_num, last_num=None, step=1) -> None:
        if last_num is None:
            last_num = first_num
            first_num = 0
        self.first_num = first_num
        self.last_num = last_num
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.first_num >= self.last_num:
            raise StopIteration
        if self.step < 0 and self.first_num <= self.last_num:
            raise StopIteration
        result = self.first_num
        self.first_num += self.step
        return result


# for i in frange(1, 100, 3.5):
#     print(i)

assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])

print('SUCCESS!')
