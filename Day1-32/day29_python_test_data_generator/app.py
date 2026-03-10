import streamlit as st
from faker import Faker
import random
import pandas as pd

fake = Faker('en_IN')

valid_states = [
    "Andhra Pradesh", "Karnataka", "Tamil Nadu",
    "Telangana", "Maharashtra", "Kerala",
    "Delhi", "Gujarat", "Rajasthan"
]

# -----------------------
# Data Generators
# -----------------------

def generate_positive(n):
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


def generate_negative(n):
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


def generate_mixed(n):
    pos_count = int(n * 0.7)
    neg_count = n - pos_count
    df_pos = generate_positive(pos_count)
    df_neg = generate_negative(neg_count)
    return pd.concat([df_pos, df_neg], ignore_index=True)


# -----------------------
# Streamlit UI
# -----------------------

st.title("🇮🇳 ETL Test Data Generator (Positive & Negative)")

rows = st.number_input("Enter number of rows", min_value=1, max_value=10000, value=100)

data_type = st.radio(
    "Select Data Type",
    ["Positive", "Negative", "Mixed (70% Positive, 30% Negative)"]
)

if st.button("Generate Data"):

    if data_type == "Positive":
        df = generate_positive(rows)
    elif data_type == "Negative":
        df = generate_negative(rows)
    else:
        df = generate_mixed(rows)

    st.success("Data Generated Successfully!")
    st.dataframe(df)

    # CSV Download
    csv = df.to_excel(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="etl_test_data.csv",
        mime="text/csv"
    )