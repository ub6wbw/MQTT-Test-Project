**Installing PostgreSQL:**
sudo apt-get update && sudo apt-get upgrade && sudo apt install postgresql postgresql-contrib

**Let's switch to the postgres user:**
sudo -i -u postgres

**Create DB:**
psql CREATE DATABASE mqtt_data;

**Connect to DB:**
psql -d mqtt_data

**Create table in DB:**


mqtt_data=# CREATE TABLE mqtt_data_test(
event_num int8,
event_date char(8),
event_time char(8),
event_payload char(64)
);

# MQTT-Test-Project
