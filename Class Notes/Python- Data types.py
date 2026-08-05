# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
#05/08/2026
#Class notes- DATA TYPES

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. STRING/TEXT TYPE
# MAGIC - Refers to a combination of characters
# MAGIC - it is a string(str) or object
# MAGIC - we indicate that the value is a string is it has single quotes ('') or double quotes ("")

# COMMAND ----------

school_name='Brightlearn'

type(school_name)  #type function is used to specify the data type contained in a specific variable

# COMMAND ----------

#We can use tripple double quotes at the start and at the end of the variable if it is a multiline string.
# The multi-line text works the same for single and double quotes.
#It is always advisable to use double quotes "" to avoid a code clash.

Love_message= '''
Hello babe,

I hope you are well,

I miss you so much!

please call me.

'''



print(Love_message)


# COMMAND ----------

type(Love_message)

# COMMAND ----------

df="bhenjn1n23b    jjduehfuehfenemsnmd"

print(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Numeric Type
# MAGIC - Integer (int): a number without a decimal e.g 24
# MAGIC - Float (float): a number with a decimal

# COMMAND ----------

x=28

type(x) #you do not have to use single or double quotes for numeric values

# COMMAND ----------

y= 12.99

type(y)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Sequence
# MAGIC - It is an array
# MAGIC - multiple values are stored in one variable
# MAGIC - list
# MAGIC - tuple
# MAGIC - range

# COMMAND ----------

my_cars= ["Toyota C-HR","Lamboghini","HAVAL"]

type(my_cars)   #A list has [square brackets] 

print(my_cars) 

# COMMAND ----------

my_cars= ("Toyota C-HR","Lamboghini","HAVAL")

type(my_cars)   #A tuple has round brackets

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Mapping type
# MAGIC - We call this a dictionary {dict}
# MAGIC - Key:Value pair
# MAGIC - Stores multiple values in a single code, separated by quotes and a comma- makes the output look organised.

# COMMAND ----------

my_profile= {
   "first_name":"Nomvelo",
   "last_name":"Gcaba",
   "age":24,
   "position":"sales rep",
   "company":"PCI"

}

print(my_profile)

type(my_profile)