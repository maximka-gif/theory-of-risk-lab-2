import math

def input_data(model_name):
    print(f"Введіть дані для {model_name} моделі:")

    profit = []
    probability = []

    for demand_type in ["високого", "середнього", "низького"]:
        p = float(input(f"Введіть прибуток для {demand_type} попиту: "))
        pr = float(input(f"Введіть ймовірність для {demand_type} попиту: "))
        profit.append(p)
        probability.append(pr)

    return profit, probability

def expected_profit(profits, probabilities):
    return sum([p * pr for p, pr in zip(profits, probabilities)])

def calculate_risk(profits, probabilities, exp_profit):
    variance = sum([pr * (p - exp_profit) ** 2 for p, pr in zip(profits, probabilities)])
    std_dev = math.sqrt(variance)
    return variance, std_dev

profit_old, probability_old = input_data("старої")
profit_new, probability_new = input_data("нової")

expected_profit_old = expected_profit(profit_old, probability_old)
expected_profit_new = expected_profit(profit_new, probability_new)

variance_old, std_dev_old = calculate_risk(profit_old, probability_old, expected_profit_old)
variance_new, std_dev_new = calculate_risk(profit_new, probability_new, expected_profit_new)

print(f"\nОчікуваний прибуток для старої моделі: {expected_profit_old:.2f}")
print(f"Очікуваний прибуток для нової моделі: {expected_profit_new:.2f}")
print(f"\nДисперсія для старої моделі: {variance_old:.2f}, Стандартне відхилення (ризик): {std_dev_old:.2f}")
print(f"Дисперсія для нової моделі: {variance_new:.2f}, Стандартне відхилення (ризик): {std_dev_new:.2f}")

risk_adjusted_old = expected_profit_old - std_dev_old
risk_adjusted_new = expected_profit_new - std_dev_new

print(f"\nОчікуваний прибуток з урахуванням ризику для старої моделі: {risk_adjusted_old:.2f}")
print(f"Очікуваний прибуток з урахуванням ризику для нової моделі: {risk_adjusted_new:.2f}")

# Прийняття рішення
if risk_adjusted_new > risk_adjusted_old:
    print("Рекомендується впровадити нову модель.")
else:
    print("Рекомендується залишити стару модель.")
