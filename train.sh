#!/bin/bash
read -p "Please input the start year for grabbing data(from 2013)" years
read -p "Please input the start year for grabbing data(from 2013)" years
if [[ -z "${python3}" ]]; then
  python3 src/training_process.py
else
  python src/training_process.py
fi
