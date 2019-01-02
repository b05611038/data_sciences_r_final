#!/bin/bash
if [[ -z "${python3}" ]]; then
  python3 src/show_route.py
else
  python src/show_route.py
fi
read -p "Please input the start gate of freeway: " start_place
read -p "Please input the end gate of freeway: " end_place
if [[ -z "${python3}" ]]; then
  python3 src/main.py $start_place $end_place
else
  python src/main.py $start_place $end_place
fi
