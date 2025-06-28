class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]
    def __iter__(self):
        return self
    def __next__(self):
        while self.stack:
            high = self.stack.pop()
            if isinstance(high, list):
                self.stack.extend(high[::-1])
            else:
                return high
        raise StopIteration
nested_list = [6, [5, [4, 3], 2], 1]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)
