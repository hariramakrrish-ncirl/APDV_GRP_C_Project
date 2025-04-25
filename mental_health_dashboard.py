import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# --- Database connection ---
engine = create_engine("postgresql://postgres:hari@localhost:5432/mental_health_project")

# --- Load data ---
@st.cache_data
def load_data():
    df = pd.read_sql("SELECT * FROM combined_master", con=engine)
    return df

df = load_data()

# --- Sidebar filters ---
st.sidebar.title("🔍 Filters")
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df.year.min()),
    max_value=int(df.year.max()),
    value=(2015, 2020)
)

available_countries = sorted(df['country_code'].dropna().unique())
default_countries = [code for code in ['USA', 'IND', 'GBR'] if code in available_countries]
countries = st.sidebar.multiselect("Select Countries", available_countries, default=default_countries)

filtered_df = df[
    (df["year"] >= year_range[0]) &
    (df["year"] <= year_range[1]) &
    (df["country_code"].isin(countries))
]

# --- App Title ---
st.title("📊 Mental Health, GDP & Awareness Dashboard")

# --- Line Plot ---
st.subheader("📈 Suicide Rate vs GDELT Events Over Time")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered_df, x="year", y="suicide_rate", label="Suicide Rate", marker="o", ax=ax1)
sns.lineplot(data=filtered_df, x="year", y="event_count", label="GDELT Events", marker="s", ax=ax1)
plt.grid(True, linestyle="--", alpha=0.3)
st.pyplot(fig1)

# --- Correlation Heatmap ---
st.subheader("📊 Correlation Matrix")
corr = filtered_df[["suicide_rate", "gdp", "event_count", "avg_tone"]].corr()
fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

# --- Pie Chart ---
st.subheader("🥧 Media Coverage Share by Country")
top_countries = filtered_df.groupby("country_code")["event_count"].sum().nlargest(5)
fig3, ax3 = plt.subplots()
top_countries.plot.pie(autopct="%1.1f%%", ax=ax3)
plt.ylabel("")
plt.title("Top 5 Countries by GDELT Mental Health Event Volume")
st.pyplot(fig3)

# --- Data Preview ---
st.subheader("🧾 Preview of Filtered Data")
st.dataframe(filtered_df.head(50))
