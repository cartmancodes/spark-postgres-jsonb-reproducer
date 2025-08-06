# Download and install spark binaries 

1. Download spark docker image:
docker pull bitnami/spark:3.5.0

2. Create temp diretory and Install the binaries fom the docker image 
mkdir -p ~/spark-binaries
cd ~/spark-binaries

3. Run temp container and copy spark binaries 
docker run --name temp_spark_container bitnami/spark:3.5.0 bash -c "true"
docker cp temp_spark_container:/opt/bitnami/spark .
docker rm temp_spark_container

4. Set SPARK_HOME 
export SPARK_HOME="/Users/shubhojeetchakraborty/spark-binaries/spark"
export PATH="$PATH:$SPARK_HOME/bin"

5. Apply thee changes
source ~/.zshrc # Or source ~/.bash_profile

# Run spark application 

spark-submit main.py