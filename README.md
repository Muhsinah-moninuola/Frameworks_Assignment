# COVID-19 Research Papers Analysis

This project analyzes a dataset of COVID-19 related research papers, performing exploratory data analysis (EDA), data cleaning, visualization, and building an interactive dashboard using **Streamlit**.

---

## Project Workflow

### **Part 1: Data Cleaning**
- Load dataset and inspect metadata.
- Handle missing/null values.
- Convert `publish_time` to datetime format.
- Extract publication **year** from `publish_time`.
- Create new column: **abstract word count**.

### **Part 2: Data Analysis & Visualization**
Performed exploratory analysis:
- **Publications by year** → count trend over time.
- **Top journals** publishing COVID-19 research.
- **Word frequency** analysis of paper titles.
- **Abstract word count distribution**.

Visualizations created:
- Line chart → Number of publications over time.
- Bar chart → Top publishing journals.
- Word cloud → Common words in paper titles.
- Distribution plots → Abstract length & sources.

### **Part 3: Streamlit Application**
An interactive dashboard built with **Streamlit**:
- Display dataset sample.
- Interactive filters (year, journal, source).
- Publication trend visualization.
- Journal distribution chart.
- Word cloud of paper titles.

---

## Installation

Clone the repository:
```bash
git clone https://github.com/Muhsinah-moninuola/Frameworks_Assignment/
cd Frameworks_Assignment
```

## Install dependencies:
```bash
pip install -r requirements.txt
```
Dependencies:
- pandas
- matplotlib
- seaborn
- wordcloud
- streamlit
- collections (Python standard library)

## Usage

Run the analysis notebook:

```bash
jupyter notebook
```
Or launch the Streamlit app:
```bash
streamlit run app.py
```

## Example Insights
- Publication activity peaked in 2020, aligning with the COVID-19 outbreak.
- Journals such as BMC Infect Dis and Respir Res were among the top publishers.
- Frequent words in titles highlight research focus areas like "infection", "respiratory", and "coronavirus".
- Abstract lengths vary widely, suggesting different depth levels of studies.
```
📂 Project Structure
├── data/
│   └── covid19_papers.csv        # Raw dataset
├── notebooks/
│   └── analysis.ipynb            # Data cleaning & visualization
├── app.py                        # Streamlit dashboard
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

## Future Improvements
- Add sentiment analysis of abstracts.
- Apply NLP techniques to cluster research themes.
- Deploy Streamlit app on Streamlit Cloud or Heroku.

---
## Author
Developed by Alaran Muhsinah
For exploratory data analysis and visualization of COVID-19 research trends.
