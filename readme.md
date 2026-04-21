# 📄 Project Documentation: Luxury Housing Sales Analysis – Bengaluru

## 🚀 Project Summary
"This project delivers an end-to-end Business Intelligence solution for Bengaluru's luxury real estate market. I developed a multi-page interactive dashboard that answers **10 critical business questions** regarding market trends, builder dominance, and consumer behavior. The pipeline features a custom **Python-based ETL process**, a structured **SQL (SQLite) data warehouse**, and advanced **DAX-driven visualizations**."

---

## 🛠️ ETL Pipeline & Feature Engineering

### **Data Cleaning & Logic**
I used **Python (Pandas)** to handle the dataset of 90,000+ rows. Since the raw data lacked a direct conversion metric, I engineered a **Booking_Status** feature to enable deeper sales analysis:
*   **Booking Logic:** Properties with 'Ready to Move' status or 'Secondary' transaction types were classified as **'Booked'**, while others were marked as **'Inquiry'**.
*   **Booking_Flag:** Created a numeric indicator (1/0) to calculate **Booking Conversion Rates** across micro-markets and builders.

### **Data Warehousing**
*   **SQL Integration:** Processed data was migrated into a **SQLite** environment (`real_estate.db`) to ensure data integrity and allow for structured querying.
*   **Validation:** Verified the database using SQL queries to confirm a successful migration of 90,981 records with 0 null values in key financial columns.

---

## 📊 Dashboard Analytics (Answering the 10 Business Questions)

The dashboard is divided into two strategic views to provide a comprehensive market analysis:

### **Page 1: Executive Market Overview**
*   **Q1: Market Trends:** Analyzed quarterly booking trends segmented by 15+ micro-markets (Line Chart).
*   **Q2 & Q10: Builder Performance:** Ranked developers by total revenue and identified the market leader (**Puravankara**) using Top-N filtering.
*   **Q5: Configuration Demand:** Visualized the distribution of 3BHK, 4BHK, and 5BHK+ units across locations.
*   **Q9: Geographical Insights:** Mapped luxury project concentration hotspots across Bengaluru.

### **Page 2: Sales & Efficiency Deep-Dive**
*   **Q3: Amenity Impact:** Scatter plot correlating **Average Amenity Scores (7.51)** with Booking Success Rates.
*   **Q4 & Q6: Efficiency Analysis:** 100% Stacked Bar charts identifying the most successful Sales Channels and Micro-Markets for conversion.
*   **Q7: Builder Dominance Matrix:** A quarterly heatmap of revenue contribution by developer.
*   **Q8: Possession Impact:** Analysis of how 'Ready to Move' vs. 'Under Construction' status affects different Buyer Types.

---

## 🔍 SQL Data Validation Results
The integrity of the SQL database was verified with the following results:
*   **Row Count:** 90,981 records.
*   **Market Avg Amenity:** 7.51 (Confirmed via DAX and SQL).
*   **Total Revenue KPI:** 1.16M Cr (Validated across all platforms).

---

## 📁 Repository Structure
*   `clean_and_load.py`: Python script for ETL, feature engineering, and SQL insertion.
*   `real_estate.db`: SQL database containing the cleaned, structured data.
*   `Luxury_Housing_Final.pbix`: 2-Page interactive Power BI report.
*   `cleaned_luxury_data.xlsx`: Final processed dataset.

## 🎓 Skills Mastered
*   **Python:** Data cleaning, feature engineering, and SQLAlchemy integration.
*   **SQL:** Schema design and data validation.
*   **Power BI:** Multi-page dashboard design, DAX measures, and drill-down analytics.
*   **Business Intelligence:** Translating raw data into actionable market insights.
