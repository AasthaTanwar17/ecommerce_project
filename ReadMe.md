# E-Commerce Order Analytics Project

## Project Overview
This project implements an **end-to-end E-Commerce Order Analytics pipeline** on **Databricks** using the **Medallion Architecture (Bronze → Silver → Gold)**.

The goal is to ingest raw e-commerce data, clean and enrich it, and finally produce **business-ready analytical tables** that can be directly used for **dashboards, reporting, and insights**.

## Project Structure

```
ecommerce_project/
│
├── resources/
│   └── workflow_notebook        # Created job using SDK
│
├── src/
│   ├── components/
│   │   ├── Bronze_layer         # Bronze layer ingestion notebooks (Autoloader)
│   │   ├── silver_layer         # Silver layer cleansing & enrichment notebooks
│   │   ├── gold_layer           # Gold layer aggregation notebooks
│   │   └── Parameters           # Centralized parameters (paths, table names)
│   │
│   └── logic/
│       └── transformation_functions.py  # Reusable transformation & helper functions
│
├── Ecommerce_DashBoard           # Databricks SQL dashboard for analytics
├── ReadMe.md                     # Project documentation
├── .gitignore
```

## Tech Stack

- **Databricks (Free Edition)**
- **Apache Spark (PySpark)**
- **Delta Lake**
- **Databricks Autoloader**
- **SQL & PySpark**

## Input Datasets

### 1. `customers.csv`
| Column Name | Description |
|------------|-------------|
| customer_id | Unique customer identifier |
| customer_name | Customer full name |
| city | Customer city |
| signup_date | Customer signup date |

### 2. `orders.csv`
| Column Name | Description |
|------------|-------------|
| order_id | Unique order identifier |
| customer_id | Linked customer ID |
| order_date | Date of order |
| order_status | Order status |

### 3. `order_items.csv`
| Column Name | Description |
|------------|-------------|
| order_item_id | Unique order item ID |
| order_id | Linked order ID |
| product_name | Product name |
| quantity | Quantity ordered |
| price | Unit price |

---

## Bronze Layer – Raw Ingestion

### Responsibilities
- Ingest CSV files using **Databricks Autoloader**
- Handle schema drift
- Track ingestion metadata

### Metadata Columns
- `_ingest_time`
- `_file_path`

### Bronze Tables
- `customers_bronze`
- `orders_bronze`
- `order_items_bronze`

**Outcome**: Raw, immutable data serving as the single source of truth

---

## Silver Layer – Data Cleaning & Enrichment

### `customers_silver`
**Cleaning & Validation**
- Remove null customer names
- Remove invalid city values
- Deduplicate customer records
- Standardize customer names
- Validate `signup_date`

### `orders_silver`
**Cleaning & Validation**
- Remove null `order_id` or `customer_id`
- Handle invalid `order_date`
- Deduplicate order records
- Filter valid order statuses (`Completed`, `Shipped`)
- Standardize date formats


### `order_items_silver`
**Cleaning & Validation**
- Remove null `order_id`
- Filter `quantity <= 0`
- Filter `price <= 0`

**Derived Columns**
- `total_price = quantity * price`

---

### `orders_enriched_silver`
**Derived Metrics**
- Order-level total amount
- Number of items per order

**Outcome**: Clean, enriched, analytics-ready Silver tables

Silver Tables:
- `customers_silver`
- `orders_silver`
- `order_items_silver`
- `orders_enriched_silver`

---

## Gold Layer – Business Aggregations

### 1. `sales_summary_gold`
**Metrics**
- Total orders
- Total revenue
- Average order value
- Daily revenue trend


### 2. `customer_performance_gold`
**Metrics**
- Total spend per customer
- Order count per customer


### 3. `product_performance_gold`
**Metrics**
- Revenue per product
- Quantity sold per product

**Outcome**: Curated Gold tables optimized for BI & reporting


## Dashboard-Ready Metrics

- Total Revenue
- Total Orders
- Average Order Value (AOV)
- Top Customers by Spend
- Top Products by Revenue

These tables can be directly connected to **Power BI, Tableau, or Databricks SQL Dashboards**.


## How to Run the Project

1. Upload CSV files to the Databricks volume or DBFS
2. Run Bronze ingestion notebooks (Autoloader)
3. Execute Silver transformation notebooks
4. Build Gold aggregation tables
5. Query Gold tables for analytics & dashboards


## Key Learnings

- Hands-on implementation of **Medallion Architecture**
- Using **Autoloader** for scalable ingestion
- Data quality enforcement in Silver layer
- Designing **business-focused Gold models**

---
