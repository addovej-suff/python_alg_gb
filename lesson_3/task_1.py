# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


num_dict = {i: 0 for i in range(2, 10)}

for i in num_dict:
    for num in range(2, 100):
        if num % i == 0:
            num_dict[i] += 1


for i, val in num_dict.items():
    print(f'{i} = {val}')

# Or easier:
# print(*num_dict.items(), sep='\n')
