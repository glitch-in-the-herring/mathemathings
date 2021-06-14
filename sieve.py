def sieve(numbers, idx):
    c, pops = numbers[idx], 0
    for i, x in enumerate(numbers[idx + 1:]):
        if x % c == 0:
            numbers.pop(i + idx + 1 - pops)
            pops += 1
            
    if idx + 1 != len(numbers):
        sieve(numbers, idx + 1)
