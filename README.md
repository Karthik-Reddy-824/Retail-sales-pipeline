# Retail Sales Analytics Pipeline

## Overview
End-to-end data pipeline that extracts, transforms, and loads retail data into a database and visualizes insights using Streamlit.

## Tech Stack
- Python (Pandas)
- SQLite
- Streamlit
- APScheduler

## Steps
1. Run ETL Pipeline:
   python scripts/pipeline.py

2. Start Dashboard:
   streamlit run app.py

3. Start Scheduler:
   python scheduler.py

## Features
- Automated ETL pipeline
- SQL-based analytics
- Interactive dashboard

##Architecture:
                +------------------+
                |  Raw CSV Data    |
                |  superstore.csv  |
                +------------------+
                          |
                          v
                +------------------+
                |   Extract Layer  |
                |   extract.py     |
                +------------------+
                          |
                          v
                +------------------+
                | Transform Layer  |
                | transform.py     |
                +------------------+
                          |
                          v
                +------------------+
                |    Load Layer    |
                |    load.py       |
                +------------------+
                          |
                          v
                +------------------+
                |   SQLite DB      |
                |    sales.db      |
                +------------------+
                          |
                          v
                +------------------+
                | Streamlit App    |
                |    app.py        |
                +------------------+
                          ^
                          |
                +------------------+
                | APScheduler      |
                | scheduler.py     |
                +------------------+

