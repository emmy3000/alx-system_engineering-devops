# 0x14. MySQL

## Task[0]: Install MySQL

* Install mysql 5.7

Copy the key here to your clipboard
```html
https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html
```

Save it in a file on your machine i.e. signature.key and then
```bash
sudo apt-key add signature.key
```

add the apt repo:
```bash
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
```

update apt
```bash
sudo apt-get update
```

now check your available versions:
```bash
vagrant@ubuntu-focal:/vagrant$ sudo apt-cache policy mysql-server
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
```

Now install mysql 5.7
```bash
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```


## Task[1]:  Let us in!

- In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

- Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
- Make sure that `holberton_user` has permission to check the primary/replica status of your databases.
- In addition to that, make sure that task #3 of your SSH project is completed for `web-01` and `web-02`. You will likely need to add the public key to `web-02` as you only added it to `web-01` for this project. The checker will connect to your servers to check MySQL status

### Solution:

* Log in to your primary MySQL server (web-01) as the root user:
```bash
mysql -uroot -p
```

* run the following command to create the `holberton_user`:
```sql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
```

* Grant Permissions to `holberton_user`:
```sql
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
```

### Output
```bash
ubuntu@221827-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
```


## Task[2]: If only you could see what I've seen with your eyes

- In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

- Create a database named `tyrell_corp`.
- Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
- Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.

### Solution

Enter the root password when prompted.

* Create the `tyrell_corp` database:
```sql
CREATE DATABASE tyrell_corp;
```

* Switch to the `tyrell_corp` database:
```sql
USE tyrell_corp;
```

* Create the nexus6 table within the `tyrell_corp` database and add an entry to it:
```sql
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO nexus6 (name) VALUES ('Leon');
```

* Grant SELECT permissions to the `holberton_user` for the nexus6 table:
```sql
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
```

* Exit the MySQL prompt:
```sql
EXIT;
```

### Output

* Verify the table data uses the `holberton_user` as follows:
```bash
mysql -uholberton_user -p -e "USE tyrell_corp; SELECT * FROM nexus6;"
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
```
This confirms that the `tyrell_corp` database, `nexus6` table, and the entry with `id=1` and `name=Leon` exist and can be accessed by the `holberton_user`.


## Task[3]: Quite an experience to live in fear, isn't it?

- Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (`web-01`), create a new user for the replica server.

- The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
- `replica_user` must have the appropriate permissions to replicate your primary MySQL server.
- `holberton_user` will need `SELECT` privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.

### Solution

* Log in to your primary MySQL server (`web-01`) as the root user:
```bash
mysql -uroot -p
```
Enter your password.

* Create the `replica_user` with the appropriate permissions:
```sql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'your_replica_user_password';
```
Replace `your_replica_user_password` with the password you'd like to set for the `replica_user`.
```sql
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
```
```sql
FLUSH PRIVILEGES;
```

* Ensure that `holberton_user` has `SELECT` privileges on the `mysql.user` table to check the `Repl_slave_priv`:
```sql
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
```
```sql
FLUSH PRIVILEGES;
```

### Output

* Verify the user and replication privileges:
```sql
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
```
This confirms that the `replica_user` has the appropriate replication privileges and that `holberton_user` has `SELECT` privileges on the `mysql.user` table.


## Task[4]: Setup a Primary-Replica infrastructure using MySQL

- Having a replica member on for your MySQL database has 2 advantages:

**Redundancy:** If you lose one of the database servers, you will still have another working one and a copy of your data

**Load distribution:** You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed

**Requirements:**
- MySQL primary must be hosted on `web-01` - do not use the `bind-address`, just comment out this parameter.
- MySQL replica must be hosted on `web-02`.
- Setup replication for the MySQL database named `tyrell_corp`.
- Provide your MySQL primary configuration as answer file(`my.cnf` or `mysqld.cnf`) with the name `4-mysql_configuration_primary`.
- Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`.

**Tips:**
- Once MySQL replication is setup, add a new record in your table via MySQL on `web-01` and check if the record has been replicated in MySQL `web-02`. If you see it, it means your replication is working!
- Make sure that UFW is allowing connections on `port 3306` (default MySQL port) otherwise replication will not work.

### Solution

* For answer file `4-mysql_configuration_primary`:

- MASTER configurations
```bash
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
# By default we only accept connections from localhost
# bind-address  = 127.0.0.1
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
server-id       = 1
log_bin         = /var/log/mysql/server_01.log
binlog_do_db    = tyrell_corp
```
- `bind-address` with localhost IP address value will be commented out to enable it accept connections from other network interfaces.
- Introduction of new directives
-- `server-id`: uniquely identifies the MySQL server in a replication environment usually an integer value.
-- `log_bin`:  enables binary logging in MySQL, these records all change to the database as binary log events in a binary log file used for replication, point-in-time recovery, and other purposes.
-- `binlog_do_db`: specifies which databases should be logged in the binary log and filters the binary log events, so only changes made to the specified databases are recorded.


* For answer file `4-mysql_configuration_replica`:

- SLAVE configurations
```bash
[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
log-error       = /var/log/mysql/error.log
# By default we only accept connections from localhost
# bind-address  = 127.0.0.1
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
server-id       = 2
log_bin         = /var/log/mysql/server_02.log
binlog_do_db    = tyrell_corp
```
- Same implementation is carried out here with unique values assigned to certain directives.

- Restart MySQL service
```bash
user@hostname: sudo service mysql restart
```

- Log into MySQL as root
```bash
user@hostname: mysql -uroot -p
Enter password:
```

- Show status of the master web server(`web-01`):
```sql
mysql> SHOW MASTER STATUS;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| server_01.000001 |      154 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)
```

- Export SQL script to slave web server(`web-02`):
```bash
user@hostname: rsync -e "ssh -i /home/user/.ssh/id_rsa" tyrell_corp.sql user@web-02_server_IP:~/tyrell_corp.sql
```

- Create back-up for the database `tyrell_corp` using the `mysqldump` via the CLI(on `web-01`).
```bash
user@hostname: mysqldump -uroot -p tyrell_corp > ~/tyrell_corp
```

- Import newly created database with same name in `web-02`:
```bash
user@hostname: mysql -uroot -p
Enter password:
```
```sql
mysql -> CREATE DATABASE tyrell_corp;
```
```sql
mysql> CHANGE MASTER TO
    -> MASTER_HOST='source_host_name',
    -> MASTER_USER='replication_user_name',
    -> MASTER_PASSWORD='replication_password',
    -> MASTER_LOG_FILE='recorded_log_file_name',
    -> MASTER_LOG_POS=recorded_log_position;
```

- Start the slave process
```sql
mysql> START SLAVE;
```

- Excute the MySQL command for slave replicant server to display status:
```bash
user@hostname: mysql -uroot -p
Enter password:
```
```sql
mysql> SHOW SLAVE STATUS\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 54.xxx.xx.xxx
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: server_01.000001
          Read_Master_Log_Pos: 154
               Relay_Log_File: 221827-web-02-relay-bin.000002
                Relay_Log_Pos: 320
        Relay_Master_Log_File: server_01.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 154
              Relay_Log_Space: 535
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 1
                  Master_UUID: 55c0a301-2692-11ee-a1d6-xxxxxxxxxxxxxxxx
             Master_Info_File: /var/lib/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp:
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
1 row in set (0.00 sec)
```
- Slave replicant server is up and running


## Task[5]: MySQL backup

What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.

Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

Requirements:

The MySQL dump must contain all your MySQL databases
The MySQL dump must be named `backup.sql`
The MySQL dump file has to be compressed to a `tar.gz` archive
This archive must have the following name format: `day-month-year.tar.gz`
The user to connect to the MySQL database must be `root`
The Bash script accepts one argument that is the password used to connect to the MySQL database

### Solution:

* Defiine script for creating database backup:
```bash
#!/usr/bin/env bash
# Bash script for generating MySQL dump and compressed archive of all databases.

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <mysqldump_generator>"
    exit 1
fi

# Create a directory to store the backup file
backup_dir="mysql_backups"
mkdir -p "$backup_dir"

# Define the backup file name
backup_file="$backup_dir/backup.sql"

# Generate the MySQL dump
mysqldump -u root -p"$1" --all-databases > "$backup_file"

# Get the current date in the desired format (day-month-year)
current_date=$(date +'%d-%m-%Y')

# Compress the dump file to a tar.gz archive with the date in the name
tar -czvf "$backup_dir/$current_date.tar.gz" "$backup_file"

# Remove the original dump file
rm "$backup_file"
```

### Output

```bash
user@hostname:~$ ./5-mysql_backup mydummypassword
backup.sql
user@hostname:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
user@hostname:~$ more backup.sql
-- MySQL dump 10.13  Distrib 5.7.25, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database:
-- ------------------------------------------------------
-- Server version   5.7.25-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `tyrell_corp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tyrell_corp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tyrell_corp`;

--
-- Table structure for table `nexus6`
--

DROP TABLE IF EXISTS `nexus6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nexus6` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
user@hostname:~$
user@hostname:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
```
