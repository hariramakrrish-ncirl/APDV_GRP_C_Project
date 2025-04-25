# Suicide, Economy & Global Events – A Data Story

This repository contains the full submission for our **Analytics Programming & Data Visualisation (APDV)** group project.  
It investigates the intersection of suicide rates, GDP per capita, and global media coverage using merged data from WHO, World Bank, and GDELT.

---

## Objective

To discover cross-domain patterns in mental health outcomes by combining structured and semi-structured datasets, and applying visual and statistical analysis.




---

###  Jupyter Notebooks

| File                | Owner  | Description                                        |
|--------------------|--------|----------------------------------------------------|
| `hari_code.ipynb`    | Hari   | GDELT pipeline: BigQuery → MongoDB → PostgreSQL    |
| `raghul_code.ipynb`  | Rahul  | Suicide rate cleaning and country-level analysis   |
| `tamil_code.ipynb`   | Tamil  | GDP wrangling, pie charts, country comparisons     |
| `visuals.ipynb`      | All    | Final merged dataset visualizations                |

---

###  Streamlit Dashboard

- `Streamlit Dashboard/mental_health_dashboard.py`  
  Interactive dashboard using **Streamlit** & **PostgreSQL**
  - Filters: year, country
  - Includes: line plots, heatmaps, pie charts, and raw data preview

---

## Datasets

| CSV File Name               | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `GDELT_cleaned_data.csv`    | Cleaned GDELT events (mental health only: 1122, 1123, 122, 125)             |
| `GDP_data.csv`              | Raw GDP per capita PPP dataset from World Bank                             |
| `gdps_data.csv`             | Cleaned GDP dataset prepared by Tamil for merging                          |
| `death_rate.csv`            | Raw suicide death rate dataset (per 100k) from WHO                         |
| `Raghul_raw.csv`            | Unprocessed suicide dataset originally handled by Rahul                    |
| `Suicide_rates_data.csv`    | Final cleaned suicide data with year/country_code used in master merge     |
| `master_dataset.csv`        | Final merged dataset: suicide + GDP + GDELT by year and country_code       |

---



## ⚙️ Technologies Used

- Python (Jupyter Notebooks)
- pandas, matplotlib, seaborn, pycountry
- PostgreSQL, MongoDB
- Google BigQuery (GDELT API)
- Streamlit (interactive dashboard)

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/hariramakrrish-ncirl/APDV_GRP_C_Project.git


# Launch a notebook
jupyter notebook visuals.ipynb 
and for all jupyter files 


# Run Streamlit dashboard
cd "Streamlit Dashboard"
streamlit run mental_health_dashboard.py
