salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

months = 10
total_deficit = 0
for month in range(months):
    current_expenses = spend * (1 + increase) ** month
    deficit = current_expenses - salary
    if deficit > 0:
        total_deficit = round(total_deficit + deficit)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_deficit)
