# Databricks notebook source
#03/08/2026
#Class Notes- Python Fundamentals

# COMMAND ----------

name='Rofhiwa' #here, we are declaring a vriableto be name, and inside the variable we are storing the value 'Rofhiwa
print(name)

# COMMAND ----------

print(name)

# COMMAND ----------

x='Rofhiwa Nemukula'

print(x) #print helps us to display the information stored in the variable

# COMMAND ----------

# MAGIC %md
# MAGIC 1. x- is a variable
# MAGIC 2. 'Rofhiwa Nemukula'- is a value, that is why it has single quotes.
# MAGIC If the value has single quotes, it makes it a string (words)
# MAGIC 3. Variable names are case sensitive (NAME <>name<>NAme<>NAMe) even though it means the same thing.
# MAGIC 4. Single quotes and double quotes mean the same thing.

# COMMAND ----------

name='Rofhiwa'

NAME='ROFHIWA'

# COMMAND ----------

print(name) #demo for case-sesitivity for variable names

# COMMAND ----------

print(NAME) #demo for case-sesitivity for variable names

# COMMAND ----------

# MAGIC %md
# MAGIC VARIABLE NAMING RULES
# MAGIC
# MAGIC 1. Variable names are case sensitive (NAME <>name<>NAme<>NAMe) even though it means the same thing
# MAGIC 2. Variable names can contain letters (A-Z), numbers (0-9) and underscores(_). An underscore is the ONLY symbol you can use in a  variable name.
# MAGIC 3. A variable name cannot start with a number.
# MAGIC 4. Do not use Python keywords as variable names. Example of Python keywords (true, if,else, class, lambda, etc.)

# COMMAND ----------

2name='rofhii' #error because variable name cannot start with a number

# COMMAND ----------

name_surname= 'Nomvelo Gcaba' #demo for the underscore rule, the code ran because a variable name can contain an underscore

print(name_surname)

# COMMAND ----------

name-age='Nomvelo 24'  #demo for the underscore rule, the code did not run because a variable name can ONLY contain an underscore symbol- nothing else



# COMMAND ----------

age_name='24 MvelorH'

print(age_name)

# COMMAND ----------

_girl='me'

print(_girl) #A variable name CAN start with an underscore BUT cannot start with a number.

# COMMAND ----------

print='wack'

print(print) # A keyword cannot be used as a variable name

# COMMAND ----------

if='now'  # A keyword cannot be used as a variable name

return='my time'  # A keyword cannot be used as a variable name

# COMMAND ----------

name="Nomvelo"



# COMMAND ----------



# COMMAND ----------

# MAGIC %md