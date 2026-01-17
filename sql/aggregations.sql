-- SQL 

-- BEFORE: heavy Python aggregation

-- AFTER: pushdown aggregation
INSERT INTO daily_sales_summary
SELECT
  event_date,
  region,
  SUM(amount) AS total_sales,
  COUNT(*) AS orders
FROM fact_orders
GROUP BY event_date, region;
