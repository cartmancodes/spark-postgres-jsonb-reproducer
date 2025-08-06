# my_app.py
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("MyLocalPySparkApp") \
        .master("local[*]") \
        .getOrCreate()

    data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    df = spark.createDataFrame(data, ["Name", "Value"])

    print("DataFrame content:")
    df.show()

    spark.stop()