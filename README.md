# 🚀 Install Spark Binaries from Docker Image

This guide shows how to extract Spark **v3.5.0** binaries from the Bitnami Docker image and run a Spark application locally without a full Spark setup.

---

## 📥 Step 1: Download Spark Docker Image

```bash
docker pull bitnami/spark:3.5.0
```

---

## 📁 Step 2: Create Temporary Directory for Spark Binaries

```bash
mkdir -p ~/spark-binaries
cd ~/spark-binaries
```

---

## 🐳 Step 3: Extract Spark Binaries from Docker Image

```bash
# Run a temporary container
docker run --name temp_spark_container bitnami/spark:3.5.0 bash -c "true"

# Copy Spark binaries from the container
docker cp temp_spark_container:/opt/bitnami/spark .

# Clean up the temporary container
docker rm temp_spark_container
```

---

## ⚙️ Step 4: Set Environment Variables

Add the following lines to your shell config file (`~/.zshrc` or `~/.bash_profile`):

```bash
export SPARK_HOME="$HOME/spark-binaries/spark"
export PATH="$PATH:$SPARK_HOME/bin"
```

---

## 🔄 Step 5: Apply the Changes

```bash
# For Zsh users
source ~/.zshrc

# For Bash users
source ~/.bash_profile
```

---

## 💡 Step 6: Run Your Spark Application

Make sure your `main.py` Spark application is ready. Then run:

```bash
spark-submit main.py
```

---

✅ You now have Spark 3.5.0 binaries ready to use locally!
