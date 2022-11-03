class Frange:
    def __init__(self, left, right=None, step=1):
        self._left = left
        self._right = right
        self._step = step
        if self._right is None:
            self._right = self._left
            self._left = 0

    def __next__(self):
        if any(
            [
                (self._step == 0),
                (self._left == self._right),
                (self._left < self._right and self._step <= 0),
                (self._left > self._right and self._step >= 0),
            ]
        ):
            raise StopIteration("stop")
        if self._right is None:
            self._right = self._left
            self._right = 0
        while any(
            [
                (self._left < self._right and self._step > 0),
                (self._left > self._right and self._step < 0),
            ]
        ):
            answer = self._left
            self._left += self._step
            return answer

    def __iter__(self):
        return self


assert list(Frange(5)) == [0, 1, 2, 3, 4]
assert list(Frange(2, 5)) == [2, 3, 4]
assert list(Frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(Frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(Frange(1, 5)) == [1, 2, 3, 4]
assert list(Frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(Frange(0, 0)) == []
assert list(Frange(100, 0)) == []

for i in Frange(1, 100, 3.5):
    print(i)

print("SUCCESS!")
