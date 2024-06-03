def avarage(*numbers) -> float:
    total = 0.0
    for n in numbers:
       total += n
    return total / len(numbers)


print(avarage(100,200,300))