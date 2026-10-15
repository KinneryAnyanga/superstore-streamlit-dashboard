# Superstore Sales Dashboard

An interactive sales analytics dashboard built with **Streamlit**, **pandas** and **Plotly**. It lets you explore the classic Superstore retail dataset, track sales performance, profitability and regional trends, and slice the data on the fly with sidebar filters.

<!-- Add a screenshot or GIF of the dashboard here, e.g.: -->
<!-- ![Dashboard preview](screenshots/dashboard.png) -->

## Features

- **KPI cards**: Total Sales, Total Profit, Quantity Sold and Profit Margin (%), updated live as filters change.
- **Sidebar filters**: Order date range, Category, Region and Segment.
- **Monthly Sales Trend**: line chart of sales aggregated by month.
- **Sales by Category**: bar chart comparing product categories.
- **Profit by Sub-Category**: horizontal bar chart with a red-to-green colour scale, so loss-making sub-categories stand out.
- **Sales Distribution by Region**: donut chart showing each region's share of sales.
- **Filtered data explorer**: expandable table of the underlying records, with a record count and date span.
- **Empty-state handling**: a warning is shown if the selected filters return no data.

## Tech Stack

| Tool | Purpose |
| --- | --- |
| [Streamlit](https://streamlit.io/) | Web app framework and UI widgets |
| [pandas](https://pandas.pydata.org/) | Data loading, cleaning and aggregation |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Interactive charts |

## Project Structure

```
superstore-streamlit-dashboard/
├── Superstore.csv      # Source dataset
├── superstore.py       # Streamlit app
└── requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.9 or newer
- `pip`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/KinneryAnyanga/superstore-streamlit-dashboard.git
cd superstore-streamlit-dashboard

# 2. (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run superstore.py
```

Streamlit will open the dashboard in your browser, usually at `http://localhost:8501`.

## How It Works

1. **Load and clean**: `Superstore.csv` is read (Latin-1 encoding), `Order Date` is parsed as a date, `Sales`, `Profit` and `Quantity` are coerced to numeric, and rows with missing values in those fields are dropped. The result is cached with `@st.cache_data` for fast reruns.
2. **Filter**: the sidebar controls narrow the dataset by date, category, region and segment.
3. **Summarise**: KPIs are calculated from the filtered data, then grouped by month, category, sub-category and region.
4. **Visualise**: Plotly charts are rendered in a two-column layout, followed by the raw filtered table.

## Dataset

The app uses the Superstore sales dataset (`Superstore.csv`), which contains order-level retail transactions including order dates, customer segments, product categories and sub-categories, regions, sales, quantity and profit.

## Possible Improvements

- Add year-over-year comparisons and growth indicators to the KPI cards.
- Add state/city-level geographic maps.
- Add top customers and top products views.
- Add a download button for the filtered data.
- Deploy to Streamlit Community Cloud and link the live demo here.

## Author

**Kinnery Anyanga**
GitHub: [@KinneryAnyanga](https://github.com/KinneryAnyanga)
