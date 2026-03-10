from faker import Faker
import random
import pandas as pd

fake = Faker('en_IN')

valid_states = [
    "Andhra Pradesh", "Karnataka", "Tamil Nadu",
    "Telangana", "Maharashtra", "Kerala",
    "Delhi", "Gujarat", "Rajasthan"
]

# ✅ Positive Data
def generate_positive(n=10):
    data = []
    for i in range(1, n + 1):
        record = {
            "sno": f"ABC{i:03}",
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "state": random.choice(valid_states),
            "salary": random.randint(25000, 150000)
        }
        data.append(record)
    return pd.DataFrame(data)


# ❌ Negative Data
def generate_negative(n=5):
    data = []

    for i in range(1, n + 1):

        record = {
            "sno": f"ABC{i:03}",
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "state": random.choice(valid_states),
            "salary": random.randint(25000, 150000)
        }

        error_type = random.choice([
            "duplicate_sno",
            "invalid_sno",
            "null_name",
            "negative_salary",
            "invalid_state",
            "salary_string"
        ])

        # Inject errors
        if error_type == "duplicate_sno":
            record["sno"] = "ABC001"

        elif error_type == "invalid_sno":
            record["sno"] = "XYZ123"

        elif error_type == "null_name":
            record["name"] = None

        elif error_type == "negative_salary":
            record["salary"] = -10000

        elif error_type == "invalid_state":
            record["state"] = "Moon"

        elif error_type == "salary_string":
            record["salary"] = "One Lakh"

        data.append(record)

    return pd.DataFrame(data)


# 🔄 Mixed Data
def generate_mixed(pos_n=10, neg_n=5):
    df_pos = generate_positive(pos_n)
    df_neg = generate_negative(neg_n)
    return pd.concat([df_pos, df_neg], ignore_index=True)


# -----------------------
# Usage
# -----------------------

print("✅ Positive Data")
print(generate_positive(5))

print("\n❌ Negative Data")
print(generate_negative(5))

print("\n🔄 Mixed Data")
print(generate_mixed(5, 3))