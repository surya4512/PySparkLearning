


# when We have Different Python versions
import os

python_path = r"t:\DataEngineer\Learning\PySparkClass\PySparkLearning\venv\Scripts\python.exe"

os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path


# Check 
echo %PYSPARK_PYTHON%
echo %PYSPARK_DRIVER_PYTHON%




## SQL retry
import os
os.environ["HADOOP_HOME"]   = "C:\\hadoop"
os.environ["PATH"]          = "C:\\hadoop\\bin;" + os.environ["PATH"]
os.environ["JAVA_HOME"]     = r"C:\Program Files\Java\jdk-17"

or 
Environments
HADOOP_HOME  -  C:\\hadoop
PATH         -  C:\\hadoop\\bin;
JAVA_HOME    -  C:\Program Files\Java\jdk-17











