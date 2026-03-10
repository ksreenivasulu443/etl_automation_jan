import numpy as np

# Number of rows
n = 1000000

# Generate ID (1 to n)
ids = np.arange(1, n+1)

# Random names (just picking from a pool)
name_pool = np.array(["Alex", "Ravi", "Priya", "John", "Sara", "Meena", "David", "Amit", "Kiran", "Lara"])
names = np.random.choice(name_pool, size=n)

# Age between 20 and 60
ages = np.random.randint(20, 100, size=n)

# Salary between 30k and 120k
salaries = np.random.randint(30000, 120001, size=n)

# Tier selection [A, B, C]
tiers = np.random.choice(["A", "B", "C"], size=n)

# Combine into structured output
data = np.column_stack((ids, names, ages, salaries, tiers))
print("data", data, data.shape)
# Display
# for row in data:
#     print(row)
