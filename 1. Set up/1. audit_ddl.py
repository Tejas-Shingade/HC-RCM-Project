# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS ADB_RCM_Project.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS ADB_RCM_Project.audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table  ADB_RCM_Project.audit.load_logs 

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from audit.load_logs
