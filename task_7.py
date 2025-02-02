import random
import matplotlib.pyplot as plt

num_throws = int(input ("Введіть кількість кидків: "))
sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(num_throws):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sum_counts[total] += 1

# Перетворюємо підрахунок у ймовірності
for key in sum_counts:
    sum_counts[key] = (sum_counts[key] / num_throws) * 100

# Побудова гістограми
plt.bar(sum_counts.keys(), sum_counts.values(), color='skyblue', edgecolor='black')
plt.xlabel("Сума очок")
plt.ylabel("Ймовірність")
plt.title(f"Метод Монте-Карло для кидання 2 кубиків ({num_throws} симуляцій)")
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()