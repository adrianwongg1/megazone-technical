import pandas as pd

MEMBER_INFO_PATH = "memberInfo.csv"
MEMBER_PAID_PATH = "memberPaidInfo.csv"
OUTPUT_PATH = "cleaned_member_paid.csv"

members = pd.read_csv(MEMBER_INFO_PATH)
paid = pd.read_csv(MEMBER_PAID_PATH)

members["full_name"] = (
    members["firstName"].fillna("").str.strip() + " " + members["lastName"].fillna("").str.strip()
).str.strip()

merged = paid.merge(
    members[["memberId", "full_name"]],
    on="memberId",
    how="inner",
)

merged = merged[merged["full_name"].str.len() > 0].copy()

paid_names = merged["fullName"].fillna("").str.strip()
info_names = merged["full_name"].fillna("").str.strip()
no_paid_name = paid_names == ""
names_agree = paid_names == info_names

merged = merged[no_paid_name | names_agree].drop(columns=["fullName"])

cleaned = merged[["memberId", "full_name", "paidAmount"]].copy()
cleaned = cleaned.sort_values("memberId").reset_index(drop=True)

