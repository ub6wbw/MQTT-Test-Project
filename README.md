**Installing PostgreSQL:**
sudo apt-get update && sudo apt-get upgrade && sudo apt install postgresql postgresql-contrib

**Let's switch to the postgres user:**
sudo -i -u postgres

**Create DB**
**psql ->**
CREATE DATABASE mqtt_data;

**Connect to DB**
psql -d mqtt_data

# MQTT-Test-Project
