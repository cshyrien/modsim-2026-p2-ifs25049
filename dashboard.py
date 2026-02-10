import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Kuesioner", layout="wide")
st.title("📊 Dashboard Visualisasi Kuesioner")

# =====================
# LOAD DATA
# =====================
@st.cache_data
def load_data():
    return pd.read_excel("data_kuesioner.xlsx")

df = load_data()

# hapus kolom Partisipan
df_q = df.drop(columns=["Partisipan"])

# =====================
# MAPPING NILAI
# =====================
score_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

sentimen_map = {
    "SS": "Positif",
    "S": "Positif",
    "CS": "Netral",
    "CTS": "Negatif",
    "TS": "Negatif",
    "STS": "Negatif"
}

df_long = df_q.melt(
    var_name="Pertanyaan",
    value_name="Jawaban"
)

df_long["Skor"] = df_long["Jawaban"].map(score_map)
df_long["Kategori"] = df_long["Jawaban"].map(sentimen_map)

# =====================
# 1. BAR CHART DISTRIBUSI JAWABAN
# =====================
st.subheader("1️⃣ Distribusi Jawaban Keseluruhan")
fig1 = px.bar(
    df_long,
    x="Jawaban",
    category_orders={
        "Jawaban": ["SS", "S", "CS", "CTS", "TS", "STS"]
    },
    text_auto=True,
    title="Distribusi Jawaban Kuesioner"
)
st.plotly_chart(fig1, use_container_width=True)

# =====================
# 2. PIE CHART PROPORSI JAWABAN
# =====================
st.subheader("2️⃣ Proporsi Jawaban")
pie_data = df_long["Jawaban"].value_counts().reset_index()
pie_data.columns = ["Jawaban", "Jumlah"]

fig2 = px.pie(
    pie_data,
    names="Jawaban",
    values="Jumlah",
    title="Proporsi Jawaban Kuesioner"
)
st.plotly_chart(fig2, use_container_width=True)

# =====================
# 3. STACKED BAR PER PERTANYAAN
# =====================
st.subheader("3️⃣ Distribusi Jawaban per Pertanyaan")
stacked = (
    df_long
    .groupby(["Pertanyaan", "Jawaban"])
    .size()
    .reset_index(name="Jumlah")
)

fig3 = px.bar(
    stacked,
    x="Pertanyaan",
    y="Jumlah",
    color="Jawaban",
    barmode="stack",
    title="Distribusi Jawaban per Pertanyaan"
)
st.plotly_chart(fig3, use_container_width=True)

# =====================
# 4. RATA-RATA SKOR PER PERTANYAAN
# =====================
st.subheader("4️⃣ Rata-rata Skor per Pertanyaan")
mean_data = df_long.groupby("Pertanyaan")["Skor"].mean().reset_index()

fig4 = px.bar(
    mean_data,
    x="Pertanyaan",
    y="Skor",
    text_auto=".2f",
    title="Rata-rata Skor per Pertanyaan"
)
st.plotly_chart(fig4, use_container_width=True)

# =====================
# 5. DISTRIBUSI POSITIF / NETRAL / NEGATIF
# =====================
st.subheader("5️⃣ Distribusi Kategori Jawaban")
cat_data = df_long["Kategori"].value_counts().reset_index()
cat_data.columns = ["Kategori", "Jumlah"]

fig5 = px.bar(
    cat_data,
    x="Kategori",
    y="Jumlah",
    text_auto=True,
    title="Distribusi Jawaban Positif, Netral, dan Negatif"
)
st.plotly_chart(fig5, use_container_width=True)

# =====================
# BONUS: HEATMAP
# =====================
st.subheader("🎁 Bonus: Heatmap Rata-rata Skor")
heatmap_data = mean_data.set_index("Pertanyaan").T

fig6 = px.imshow(
    heatmap_data,
    text_auto=True,
    aspect="auto",
    title="Heatmap Rata-rata Skor Kuesioner"
)
st.plotly_chart(fig6, use_container_width=True)
