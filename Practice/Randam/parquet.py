import os
from pyspark.sql import SparkSession

# 1. Safety net for Windows Hadoop issues (forces Spark to see your Hadoop folder)
os.environ['HADOOP_HOME'] = 'C:\\hadoop'

# 2. Initialize Spark Session
print("Starting Spark Session...")
spark = SparkSession.builder \
    .appName("LocalEmployeeJob") \
    .master("local[*]") \
    .getOrCreate()

# Optional: Set log level to ERROR to hide the massive walls of Spark INFO text
spark.sparkContext.setLogLevel("ERROR")

# 3. Define the data
data = [
    (1, 'Aarav Shah', 'Engineering', 72000, 2019),
    (2, 'Priya Menon', 'HR', 45000, 2021),
    (3, 'Rahul Verma', 'Sales', 58000, 2020),
    (4, 'Sneha Iyer', 'Finance', 81000, 2018),
    (5, 'Karan Patel', 'Engineering', 95000, 2017),
    (6, 'Divya Nair', 'Marketing', 52000, 2022),
    (7, 'Amit Sharma', 'HR', 43000, 2021),
    (8, 'Neha Gupta', 'Engineering', 88000, 2018),
    (9, 'Rohan Joshi', 'Sales', 61000, 2019),
    (10, 'Ananya Singh', 'Finance', 76000, 2020)
]

columns = ["emp_id", "name", "dept", "salary", "join_year"]

# 4. Create and show the DataFrame
print("Creating DataFrame...")
df = spark.createDataFrame(data, columns)
df.show(truncate=False)

# 5. Write to Parquet (Partitioned)
output_path = "delete/employee_data_system.parquet"
print(f"Writing data to Parquet format at: {output_path}")

df.write.parquet(
    path=output_path,
    mode="overwrite",
    partitionBy=["dept"]
)

print("Job completed successfully!")

# 6. Cleanly shut down Spark
spark.stop()