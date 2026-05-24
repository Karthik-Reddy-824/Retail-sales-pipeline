-- Total Revenue
pragma table_info(orders);
SELECT SUM(Revenue) AS total_revenue FROM orders;

-- Revenue by Region
SELECT Region, SUM(Revenue) 
FROM orders 
GROUP BY Region;


-- Monthly Revenue
SELECT strftime('%Y-%m', "Order Date") as month, SUM(Revenue)
FROM orders
GROUP BY month;


--rank regions by revenue
select region,sum(revenue)as total_revenue,
rank() over(order by sum(revenue) desc) as revenue_rank
from orders
group by region;

--revenue by category
select p.category, sum(o.revenue) as total_revenue
from orders o 
join products p ON o."Product ID" = p."Product ID"
group by p.category
order by total_revenue desc;