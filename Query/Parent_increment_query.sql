-- Databricks notebook source
copy into fmcg.gold.fact_orders
from(
    select 
    cast(date as DATE) as date,
    product_code,
    cast(customer_code as BIGINT) as customer_code,
    cast (sold_quantity as BIGINT) as sold_quantity
    from
    '/Volumes/fmcg/gold/parent_incremental_update/incremental_load/fact_orders.csv'
)
fileformat = CSV
format_options('header' = 'true');