def reverseStr(a, b):
    a = list(a)
    for i in range(0, len(a), 2 * b):
        left = i
        right = min(i + b - 1, len(a) - 1)
        while left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
    return ''.join(a)
a = "ялюблюпитон"
b = 2
print(reverseStr(a, b))
