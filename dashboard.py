import json
import re
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Issue Triage Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Issue Triage Dashboard")
st.write("Monitor GitHub issues analyzed automatically by Gemini AI.")

# Load results
try:
    with open("results.json", "r", encoding="utf-8") as file:
        results = json.load(file)
except FileNotFoundError:
    results = []

if not results:
    st.info("No analyzed issues yet.")
    st.stop()


# Convert AI analysis into separate fields
rows = []

for result in results:
    analysis = result.get("analysis", "")

    category_match = re.search(
        r"Category:\*?\*?\s*(Bug|Feature Request|Documentation|Performance|Other)",
        analysis,
        re.IGNORECASE
    )

    priority_match = re.search(
        r"Priority:\*?\*?\s*(High|Medium|Low)",
        analysis,
        re.IGNORECASE
    )

    summary_match = re.search(
        r"Short summary:\*?\*?\s*(.*)",
        analysis,
        re.IGNORECASE
    )

    rows.append({
        "Issue": result.get("issue_number", ""),
        "Summary": summary_match.group(1) if summary_match else "See AI analysis",
        "Category": category_match.group(1).title() if category_match else "Other",
        "Priority": priority_match.group(1).title() if priority_match else "Medium",
        "AI Analysis": analysis
    })

df = pd.DataFrame(rows)


# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Issues", len(df))
col2.metric("High Priority", len(df[df["Priority"] == "High"]))
col3.metric("Bugs", len(df[df["Category"] == "Bug"]))
col4.metric("Feature Requests", len(df[df["Category"] == "Feature Request"]))


st.divider()

# Filters
st.subheader("🔎 Filter Issues")

col1, col2 = st.columns(2)

with col1:
    priority_filter = st.selectbox(
        "Priority",
        ["All", "High", "Medium", "Low"]
    )

with col2:
    category_filter = st.selectbox(
        "Category",
        ["All", "Bug", "Feature Request", "Documentation",
         "Performance", "Other"]
    )

filtered_df = df.copy()

if priority_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Priority"] == priority_filter
    ]

if category_filter != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == category_filter
    ]


st.subheader("📋 Analyzed Issues")

st.dataframe(
    filtered_df[
        ["Issue", "Summary", "Category", "Priority"]
    ],
    use_container_width=True,
    hide_index=True
)


st.subheader("🤖 AI Analysis")

for _, row in filtered_df.iterrows():
    with st.expander(f"Issue #{row['Issue']} — {row['Priority']} Priority"):
        st.write(row["AI Analysis"])