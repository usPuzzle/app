"""nums=[7,8,9,5]
it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))"""

class TopTen:
    def __init__(self):
        self.pera = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.pera <= 10:
            val = self.pera
            self.pera += 1
            return val 
        else:
            raise StopIteration

values = TopTen()
print(next(values))
for i in values:
    print(i)
