# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

st.set_page_config(layout="wide", page_title="CORD-19 Data Explorer")

@st.cache_data
def load_data(path='metadata_cleaned_sample.csv'):
    return pd.read_csv(path, parse_dates=['publish_time'])

# Load
df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of the CORD-19 metadata (sample).")

# Sidebar controls
years = sorted(df['year'].unique())
min_y, max_y = min(years), max(years)
year_range = st.sidebar.slider("Select year range", min_value=int(min_y), max_value=int(max_y), value=(int(max_y)-2, int(max_y)))
source_options = ['All'] + sorted(df['source_x'].unique().tolist())
source_sel = st.sidebar.selectbox("Source", source_options)
top_n = st.sidebar.slider("Top N journals", min_value=5, max_value=30, value=10)

# Filter data
df_f = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
if source_sel != 'All':
    df_f = df_f[df_f['source_x'] == source_sel]

st.write(f"Showing {len(df_f)} papers from {year_range[0]} to {year_range[1]} (source: {source_sel})")

# Publications by year plot
year_counts = df_f['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(8,3))
ax.bar(year_counts.index.astype(int), year_counts.values)
ax.set_xlabel('Year'); ax.set_ylabel('Count'); ax.set_title('Publications by Year')
st.pyplot(fig)

# Top journals
top_j = df_f['journal'].value_counts().head(top_n)
fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.barh(top_j.index[::-1], top_j.values[::-1])
ax2.set_title(f'Top {top_n} Journals')
st.pyplot(fig2)

# Show sample data
st.subheader("Sample of data")
st.dataframe(df_f[['title','journal','publish_time','source_x']].head(50))

# Simple title word frequency (top 20)
def clean_text(s):
    s = str(s).lower()
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    s = re.sub(r'\s+',' ', s).strip()
    return s

titles = df_f['title'].dropna().astype(str).apply(clean_text).tolist()
all_words = " ".join(titles).split()
stopwords = {'the','and','of','in','a','to','for','with','on','by','an','is','are','using','study','studies','case','cases','report','reports'}
filtered = [w for w in all_words if w not in stopwords and len(w)>2]
freq = Counter(filtered)
top20 = freq.most_common(20)
st.subheader("Top title words")
st.table(pd.DataFrame(top20, columns=['word','count']))

st.write("Built with Streamlit — run with: `streamlit run app.py`")
