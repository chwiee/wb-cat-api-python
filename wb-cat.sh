#!/bin/bash

echo "-- ----------
      -- Wallace Bruno Gentil
      -- WB CAT API 
      -- v1.0
      -- ----------"

validate () {
  if [ $1 -eq 0 ]; then echo -e "[  Ok  ]" ; else echo -e "[ Fail ]" ; exit 1 ; fi
}

#printf "%-100s" "Check if u run script with sudo"
#if [ "$EUID" -ne 0 ]
#  then echo "Please run as root 'sudo'"
#  exit
#else
#  validate 0
#fi

printf "%-100s" "Check if docker has been installed"
  which docker &>/dev/null
  validate $?
  
printf "%-100s" "Check if docker-compose has been installed"
  which docker-compose &>/dev/null
  validate $?

printf "%-100s" "Check if git has been installed"
  which git &>/dev/null
  validate $?

if [ ! -d /tmp/WB ]; then
  printf "%-100s" "Create folder 'WB' on /tmp"
    mkdir /tmp/WB &>/dev/null
    validate $?
fi 

printf "%-100s" "Cloning project in /tmp/wb/"
  git clone https://github.com/chwiee/wb-cat-api-python.git /tmp/WB &>/dev/null
  validate $?

printf "%-100s" "Create 'WB' docker network"
  docker network create WB &>/dev/null
  validate $?

printf "%-100s" "Using docker-compose to init all applications"
  docker-compose up -d &>/dev/null
  validate $?

while [ "`curl -XGET "http://0.0.0.0:9200/_cluster/health?pretty" --silent | grep -i 'cluster_name'`" == "" ]; do
  printf "Check if elasticsearch service are ready to receive requests \n"
  sleep 3
done

printf "%-100s" "Create index and mapping 'audit-py'"
  curl -XPUT "http://localhost:9200/audit-py" -H 'Content-Type: application/json' -d'{"mappings": {"properties": {"@timestamp" : {"type": "date","format": ["dd/MM/yyyy HH:mm:ss"]}}}}' &>/dev/null
  validate $?

echo "

the application may take a few minutes to populate the database completely.

To use the application, access the address 0.0.0.0,5000 via the browser (see the manual for more information on routes)

Tks :)
<3 Wallace Bruno Gentil

"