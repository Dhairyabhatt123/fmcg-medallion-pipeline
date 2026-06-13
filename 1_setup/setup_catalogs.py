# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC create catalog if not exists fmcg;
# MAGIC use catalog fmcg;

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists fmcg.gold;
# MAGIC create schema if not exists fmcg.silve;
# MAGIC create schema if not exists fmcg.bronze;

# COMMAND ----------

# MAGIC %sql 
# MAGIC show catalogs

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from fmcg.gold.fact_orders;