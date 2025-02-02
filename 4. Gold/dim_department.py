# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS gold.dim_department
# MAGIC (
# MAGIC Dept_Id string,
# MAGIC SRC_Dept_Id string,
# MAGIC Name string,
# MAGIC datasource string
# MAGIC )

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE gold.dim_department 

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into gold.dim_department
# MAGIC select 
# MAGIC distinct
# MAGIC Dept_Id ,
# MAGIC SRC_Dept_Id ,
# MAGIC Name ,
# MAGIC datasource 
# MAGIC  from silver.departments
# MAGIC  where is_quarantined=false

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from gold.dim_department
