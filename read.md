
#hadoop
https://github.com/cdarlint/winutils/tree/master/hadoop-2.7.2/bin


# java - 17
https://adoptium.net/temurin/releases?version=17






# isssue i face 
1. python version issuses
2. java version issuses
4. hadoop files issuses









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








############################################################################
Get-Item "C:\Program Files\Common Files\Oracle\Java\javapath\java.exe" | Format-List *



java --version
(Get-Command java).Source




java --version
echo $env:JAVA_HOME
(Get-Command java).Source




(Get-Command java).Source



[Environment]::SetEnvironmentVariable(
"JAVA_HOME",
"C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot",
"Machine"
)







