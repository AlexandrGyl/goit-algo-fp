def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = {}
    total_cost = 0
    total_calories = 0

    for name, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items[name] = details
            total_cost += details['cost']
            total_calories += details['calories']

    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    # Створюємо масив для зберігання максимальної калорійності для кожного бюджету
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for cost in range(1, budget + 1):
        for name, details in items.items():
            if details['cost'] <= cost and name not in selected_items[cost - details['cost']]:
                if dp[cost] < dp[cost - details['cost']] + details['calories']:
                    dp[cost] = dp[cost - details['cost']] + details['calories']
                    selected_items[cost] = selected_items[cost - details['cost']] + [name]

    optimal_items = selected_items[budget]
    total_cost = sum(items[name]['cost'] for name in optimal_items)
    total_calories = dp[budget]

    return optimal_items, total_cost, total_calories

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Заданий бюджет
budget = 100

# Використання жадібного алгоритму
selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items_greedy)
print("Загальна вартість:", total_cost_greedy)
print("Загальна калорійність:", total_calories_greedy)

# Використання алгоритму динамічного програмування
optimal_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Оптимальні страви:", optimal_items_dp)
print("Загальна вартість:", total_cost_dp)
print("Загальна калорійність:", total_calories_dp)
