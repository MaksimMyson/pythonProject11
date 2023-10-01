input_str = input("Введіть елементи списку цілих чисел: ")
numbers = list(map(int, input_str.split()))
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"Сума всіх елементів: {total_sum}")
print(f"Середнє арифметичне: {average}")




