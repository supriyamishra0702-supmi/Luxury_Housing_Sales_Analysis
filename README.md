# 📄 Project Documentation: Luxury Housing Sales Analysis – Bengaluru

## 🚀 Project Summary
> "This project delivers an end-to-end Business Intelligence solution for the luxury real estate market in Bengaluru. Using a dataset of 100,000+ records, I built a modular ETL pipeline in **Python** to clean and engineer features, migrated the processed data into a **SQL (SQLite)** environment for structured storage, and developed an interactive **Power BI** dashboard. The analysis uncovers critical market hotspots, builder performance rankings, and configuration demand shifts, providing data-driven insights to optimize sales and pricing strategies in the urban real estate domain."

## 📊 Overview
This project is an end-to-end data engineering and analytics solution. I analyzed over **90,000 luxury housing records** in Bengaluru to identify market trends, builder performance, and buyer preferences. The goal was to build a real-world enterprise data pipeline using **Python, SQL, and Power BI**.

---

## 🛠️ ETL Pipeline

### **Step 1: Data Cleaning & Preprocessing (Python)**
I used **Pandas** to handle a large dataset of 100,000+ rows. Key tasks included:
*   **Standardizing Currency:** Cleaned the `Ticket_Price_Cr` column by removing strings like "Cr" and "₹" to make it numeric.
*   **Handling Nulls:** Removed rows with missing price data to ensure financial analysis remained accurate.
*   **Feature Engineering:** Created new metrics like `Price_per_Sqft` and a `Booking_Flag` for better visualization.
*   **Normalization:** Cleaned builder and location names to remove duplicates.

<img width="602" height="333" alt="clean_and_load_terminal run" src="https://github.com/user-attachments/assets/b02d2ea9-d036-4b20-8227-347f3de93221" />

### **Step 2: Data Warehousing (SQL)**
Instead of just using a flat CSV, I moved the data into a **SQL environment (SQLite)** using **SQLAlchemy**.
*   Ensured data integrity and allowed for structured querying.
*   The database (`real_estate.db`) serves as the **"Single Source of Truth"** for the dashboard.

### **Step 3: Interactive Dashboarding (Power BI)**
I connected Power BI to the SQL database via a **Python Script connection**.
*   **Interactivity:** Added slicers for Builders and Markets for dynamic filtering.
*   **Custom Logic:** Wrote **DAX measures** to calculate the "Average Market Amenity Score."
*   **Spatial Analysis:** Integrated a Map visual to show geographic density.

<img width="935" height="524" alt="powerBI" src="https://github.com/user-attachments/assets/d276f7fd-0cd7-41fa-9efb-02f39e3c0462" />

---

## 🔍 SQL Data Validation
To ensure the data was loaded correctly, I executed several validation queries:

<img width="949" height="329" alt="SQL Database Validation Results" src="https://github.com/user-attachments/assets/294cba09-2e43-4257-9be6-7c63d22051cb" />

1.  **Verification of Row Count**
    *   **Query:** `SELECT COUNT(*) FROM luxury_housing;`
    *   **Result:** Confirmed **90,981 records** successfully migrated.
2.  **Builder Revenue Check**
    *   **Query:** `SELECT Developer_Name, SUM(Ticket_Price_Cr) FROM luxury_housing GROUP BY Developer_Name ORDER BY 2 DESC LIMIT 5;`
    *   **Purpose:** Validated that financial columns are numeric and aggregations are working.
3.  **Null Value Audit**
    *   **Query:** `SELECT COUNT(*) FROM luxury_housing WHERE Ticket_Price_Cr IS NULL;`
    *   **Result:** **0 nulls** found.

---

## 💡 Key Business Insights
*   📍 **Market Hotspots:** Luxury housing is highly concentrated in the **East (Whitefield)** and **South (Sarjapur)** corridors, driven by tech park proximity.
*   🏢 **Product Demand:** Massive shift toward **3BHK and 4BHK** units; luxury buyers prioritize spacious living.
*   ⭐ **The "Amenity Gap":** Average amenity score is **7.50**, indicating high-end facilities are now a standard expectation.

---

## 📁 Repository Structure
*   `clean_and_load.py`: Python script for cleaning and SQL insertion.
*   `real_estate.db`: SQL database containing cleaned data.
*   `Luxury_Housing_Analysis.pbix`: Final Power BI dashboard.
*   `README.md`: Project documentation.

## 🎓 Skills Learned
*   Building complete **ETL pipelines**.
*   **Database Management** via SQLAlchemy and SQLite.
*   Advanced **DAX calculations** in Power BI.
*   Data storytelling and **Business Intelligence**.

