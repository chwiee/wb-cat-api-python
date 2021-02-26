#!/bin/bash

echo "-- ----------
      -- Wallace Bruno Gentil
      -- WB CAT API 
      -- v1.0
      -- ----------"

validate () {
  if [ $1 -eq 0 ]; then echo -e "[  Ok  ]" ; else echo -e "[ Fail ]" ; exit 1 ; fi
}

printf "%-100s" "Check if u run script with sudo"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root 'sudo'"
  exit
else
  validate 0
fi

printf "%-100s" "Check if docker has been installed"
  which docker &>/dev/null
  validate $?
  
printf "%-100s" "Check if docker has been installed"
  which docker-compose &>/dev/null
  validate $?

printf "%-100s" "Check if docker has been installed"
  which git &>/dev/null
  validate $?

printf "%-100s" "Create folder 'WB' on /tmp"
  mkdir /tmp/WB
  validate $?

printf "%-100s" "Cloning project in /tmp/wb/"
  

printf "%-100s" "Check if ports are available"
sudo lsof -i -P -n | grep LISTEN | ports

printf "%-100s" "Create 'WB' docker network"
  docker network create WB
  validate $?

printf "%-100s" "Using docker-compose to init all applications"

printf "%-100s" "Start 'kibana' container"

printf "%-100s" "Check if elasticsearch service are ready to receive requests"

printf "%-100s" "Create index and mapping 'audit-py'"
  curl -XPUT "http://localhost:9200/audit-py" -H 'Content-Type: application/json' -d'{"mappings": {"properties": {"@timestamp" : {"type": "date","format": ["dd/MM/yyyy HH:mm:ss"]}}}}'