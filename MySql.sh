#!/bin/bash

#your database username
USERNAME="YOUR_USERNAME"
#your database password
PASSWORD="YOUR_PASSWORD"
#your dbname
DBNAME="YOUR_DB_NAME"
#your server_address
SERVERADDRESS="YOUR_SERVER_ADDRESS"

#Run Mysql query and send data to while loop through pip
mysql --silent -h $SERVERADDRESS -P 3306 -u $USERNAME -p$PASSWORD -D $DBNAME <<<"YOUR_DATABASE_QUERY" 2>/dev/null |

#READ COLUMN NAME original_image through loop(note= IFS is used for seperating the output in multiple line)
#replace col_name with your column name like eg. "Select name from employees" so you should change "col_name" to "name"
while IFS='\n' read col_name
do
  
  echo $col_name
  
  echo " "

done 


#bash script for reading the database in linux
