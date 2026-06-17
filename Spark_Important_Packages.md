# PySpark Important Packages Notes

## What is spark.jars.packages?

Used to download and attach external libraries (JARs) to Spark at runtime.

```python
spark = (
    SparkSession.builder
    .appName("Demo")
    .config(
        "spark.jars.packages",
        "groupId:artifactId:version"
    )
    .getOrCreate()
)
```

---

# 1. Avro

### Package

```python
.config(
    "spark.jars.packages",
    "org.apache.spark:spark-avro_2.13:4.1.2"
)
```

### Read Avro

```python
df = spark.read.format("avro").load("employee_avro")
```

### Write Avro

```python
df.write.format("avro") \
        .mode("overwrite") \
        .save("employee_avro")
```

---

# 2. Kafka

### Package

```python
.config(
    "spark.jars.packages",
    "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2"
)
```

### Read Kafka Stream

```python
df = spark.readStream \
          .format("kafka") \
          .option("kafka.bootstrap.servers", "localhost:9092") \
          .option("subscribe", "orders") \
          .load()
```

---

# 3. Delta Lake

### Package

```python
.config(
    "spark.jars.packages",
    "io.delta:delta-spark_2.13:4.0.0"
)
```

### Write Delta

```python
df.write.format("delta").save("delta_table")
```

### Read Delta

```python
spark.read.format("delta").load("delta_table")
```

---

# 4. PostgreSQL

### Package

```python
.config(
    "spark.jars.packages",
    "org.postgresql:postgresql:42.7.7"
)
```

### Read PostgreSQL

```python
df = spark.read.jdbc(
    url=url,
    table="employees",
    properties=props
)
```

---

# 5. MySQL

### Package

```python
.config(
    "spark.jars.packages",
    "com.mysql:mysql-connector-j:9.3.0"
)
```

### Read MySQL

```python
df = spark.read.jdbc(
    url=url,
    table="employees",
    properties=props
)
```

---

# 6. SQL Server

### Package

```python
.config(
    "spark.jars.packages",
    "com.microsoft.sqlserver:mssql-jdbc:12.10.0.jre11"
)
```

---

# 7. MongoDB

### Package

```python
.config(
    "spark.jars.packages",
    "org.mongodb.spark:mongo-spark-connector_2.13:10.5.0"
)
```

---

# 8. Cassandra

### Package

```python
.config(
    "spark.jars.packages",
    "com.datastax.spark:spark-cassandra-connector_2.13:3.5.1"
)
```

---

# 9. AWS S3

### Package

```python
.config(
    "spark.jars.packages",
    "org.apache.hadoop:hadoop-aws:3.4.1"
)
```

### Read from S3

```python
df = spark.read.parquet(
    "s3a://bucket/path"
)
```

---

# 10. Apache Iceberg

### Package

```python
.config(
    "spark.jars.packages",
    "org.apache.iceberg:iceberg-spark-runtime-4.1_2.13:1.10.0"
)
```

---

# Multiple Packages

```python
spark = (
    SparkSession.builder
    .appName("Demo")
    .config(
        "spark.jars.packages",
        ",".join([
            "org.apache.spark:spark-avro_2.13:4.1.2",
            "org.postgresql:postgresql:42.7.7",
            "org.apache.hadoop:hadoop-aws:3.4.1"
        ])
    )
    .getOrCreate()
)
```

---

# Maven Coordinate Format

```text
groupId:artifactId:version
```

Example:

```text
org.apache.spark:spark-avro_2.13:4.1.2
```

| Part             | Meaning     |
| ---------------- | ----------- |
| org.apache.spark | Group ID    |
| spark-avro_2.13  | Artifact ID |
| 4.1.2            | Version     |

---

# Most Important for Data Engineers

1. Kafka
2. Delta Lake
3. PostgreSQL JDBC
4. MySQL JDBC
5. SQL Server JDBC
6. S3 (hadoop-aws)
7. Avro
8. Iceberg
9. MongoDB
10. Cassandra

---

# Common File Formats

### CSV

```python
spark.read.csv("file.csv")
```

### JSON

```python
spark.read.json("file.json")
```

### Parquet

```python
spark.read.parquet("file.parquet")
```

### ORC

```python
spark.read.orc("file.orc")
```

### Avro

```python
spark.read.format("avro").load("file.avro")
```
