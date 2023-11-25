**Installing PostgreSQL:**
sudo apt-get update && sudo apt-get upgrade && sudo apt install postgresql postgresql-contrib

**Create User in PostgreSQL:**
createuser --interactive --pwprompt
(name - mqtt, password - mqtt123)

**Let's switch to the postgres user:**
sudo -i -u postgres

**psql**
CREATE DATABASE mqtt

# MQTT-Test-Project
