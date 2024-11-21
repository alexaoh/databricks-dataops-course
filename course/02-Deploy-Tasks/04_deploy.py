# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. connect to the UC Shared Cluster you have been assigned, and run through the cells
# MAGIC 3. Run the cells for deploying and running the dev job

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Workflows
# MAGIC
# MAGIC Workflows is on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A job is a definition of a worklow/job/pipelines, composed of many tasks orchestrated in a certain way, whereas a job run is an instantiation of it. One job has many job runs. 

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC The name is: **acme_transport_taxinyc_prep_dev_alexander_featgh11015barcelona_c94b8749**
# MAGIC
# MAGIC It is composed by container_prep_dev_firstname_branchname_shortcommithash

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Where is the job cluster defined?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC On the job itself or inside each task in the job (inherited perhaps, not sure)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Answer here...

# COMMAND ----------


