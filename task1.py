import pulp


# Завдання 1: Оптимізація виробництва
# Створення моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Функція цілі
model += lemonade + fruit_juice, "Total Products"

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "Water Constraint"
model += lemonade <= 50, "Sugar Constraint"
model += lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання
model.solve()
print(f"Max Lemonade: {lemonade.varValue}, Max Fruit Juice: {fruit_juice.varValue}")

