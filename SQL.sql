1.Year-wise Trend of Rice Production Across States (Top 3) 

WITH top_states AS (
  SELECT "Statename", SUM("Rice_production") AS total_rice_prod
  FROM "AgriData_Explorer"
  GROUP BY "Statename"
  ORDER BY total_rice_prod DESC
  LIMIT 3
)
SELECT "Year", SUM("Rice_production") AS total_rice_production_top3
FROM "AgriData_Explorer"
WHERE "Statename" IN (SELECT "Statename" FROM top_states)
GROUP BY "Year"
ORDER BY "Year"


2.Top 5 Districts by Wheat Yield Increase Over the Last 5 Years 

WITH year_range AS (
  SELECT MAX("Year") AS latest_year
  FROM "AgriData_Explorer"
),
yield_change AS (
  SELECT "Distname",
         MAX(CASE WHEN "Year" = (SELECT latest_year FROM year_range) THEN "Wheat_yield" END) AS recent_yield,
         MAX(CASE WHEN "Year" = (SELECT latest_year FROM year_range) - 4 THEN "Wheat_yield" END) AS old_yield
  FROM "AgriData_Explorer"
  GROUP BY "Distname"
)
SELECT "Distname", (recent_yield - old_yield) AS yield_increase
FROM yield_change
WHERE recent_yield IS NOT NULL AND old_yield IS NOT NULL
ORDER BY yield_increase DESC
LIMIT 5;



3.States with the Highest Growth in Oilseed Production (5-Year Growth Rate) 

WITH growth AS (
  SELECT "Statename",
         SUM(CASE WHEN "Year" = (SELECT MAX("Year") FROM "AgriData_Explorer") THEN "Oilseeds_production" END) AS recent,
         SUM(CASE WHEN "Year" = (SELECT MAX("Year") FROM "AgriData_Explorer") - 4 THEN "Oilseeds_production" END) AS past
  FROM "AgriData_Explorer"
  GROUP BY "Statename"
)
SELECT "Statename",
       ROUND((((recent - past) * 100.0) / NULLIF(past, 0))::numeric, 2) AS growth_rate_percent
FROM growth
WHERE recent IS NOT NULL AND past IS NOT NULL
ORDER BY growth_rate_percent DESC	



4.District-wise Correlation Between Area and Production for Major Crops (Rice, Wheat, and Maize) 

SELECT 'Rice' AS crop, "Distname", CORR("Rice_area", "Rice_production") AS correlation
FROM "AgriData_Explorer"
GROUP BY "Distname"
UNION ALL
SELECT 'Wheat', "Distname", CORR("Wheat_area", "Wheat_production")
FROM "AgriData_Explorer"
GROUP BY "Distname"
UNION ALL
SELECT 'Maize', "Distname", CORR("Maize_area", "Maize_production")
FROM "AgriData_Explorer"
GROUP BY "Distname";



5.Yearly Production Growth of Cotton in Top 5 Cotton Producing States 

WITH top_states AS (
  SELECT "Statename", SUM("Cotton_production") AS total_prod
  FROM "AgriData_Explorer"
  GROUP BY "Statename"
  ORDER BY total_prod DESC
  LIMIT 5
)
SELECT "Year", "Statename", SUM("Cotton_production") AS cotton_production
FROM "AgriData_Explorer"
WHERE "Statename" IN (SELECT "Statename" FROM top_states)
GROUP BY "Year", "Statename"
ORDER BY "Year", "Statename";

6.Districts with the Highest Groundnut Production in 2017 (till 2017)

SELECT DISTINCT "Year" FROM "AgriData_Explorer" ORDER BY "Year";


SELECT "Distname", SUM("Groundnut_production") AS total_groundnut_production
FROM "AgriData_Explorer"
WHERE "Year" = 2017
GROUP BY "Distname"
ORDER BY total_groundnut_production DESC
LIMIT 10;


7.Annual Average Maize Yield Across All States 

SELECT "Year", ROUND(AVG("Maize_yield")::numeric, 2) AS avg_maize_yield
FROM "AgriData_Explorer"
GROUP BY "Year"
ORDER BY "Year";



8.Total Area Cultivated for Oilseeds in Each State 

SELECT "Statename", SUM("Oilseeds_area") AS total_oilseeds_area
FROM "AgriData_Explorer"
GROUP BY "Statename"
ORDER BY total_oilseeds_area DESC;


9.Districts with the Highest Rice Yield 

SELECT "Distname", ROUND(AVG("Rice_yield")::numeric, 2) AS avg_rice_yield
FROM "AgriData_Explorer"
GROUP BY "Distname"
ORDER BY avg_rice_yield DESC
LIMIT 10;


10.Compare the Production of Wheat and Rice for the Top 5 States Over 10 Years 

WITH top_states AS (
  SELECT "Statename",
         SUM("Rice_production" + "Wheat_production") AS total_prod
  FROM "AgriData_Explorer"
  WHERE "Year" >= EXTRACT(YEAR FROM CURRENT_DATE) - 10
  GROUP BY "Statename"
  ORDER BY total_prod DESC
  LIMIT 5
),
combined AS (
  SELECT "Year", "Statename", 'Rice' AS crop, SUM("Rice_production") AS production
  FROM "AgriData_Explorer"
  WHERE "Statename" IN (SELECT "Statename" FROM top_states)
    AND "Year" >= EXTRACT(YEAR FROM CURRENT_DATE) - 10
  GROUP BY "Year", "Statename"
  UNION ALL
  SELECT "Year", "Statename", 'Wheat' AS crop, SUM("Wheat_production")
  FROM "AgriData_Explorer"
  WHERE "Statename" IN (SELECT "Statename" FROM top_states)
    AND "Year" >= EXTRACT(YEAR FROM CURRENT_DATE) - 10
  GROUP BY "Year", "Statename"
)
SELECT * FROM combined
ORDER BY "Statename", "Year", crop;

