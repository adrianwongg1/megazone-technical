import pandas as pd

MEMBER_INFO_PATH = "memberInfo.csv"
MEMBER_PAID_PATH = "memberPaidInfo.csv"
OUTPUT_PATH = "cleaned_member_paid.csv"

members = pd.read_csv(MEMBER_INFO_PATH)
paid = pd.read_csv(MEMBER_PAID_PATH)

members["full_name"] = (
    members["firstName"].fillna("").str.strip() + " " + members["lastName"].fillna("").str.strip()
).str.strip()

print(members["full_name"].head(10))