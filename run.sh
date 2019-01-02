#!/bin/bash
python3 src/show_route.py
read -p "Please input the start gate of freeway: " start_place
read -p "Please input the end gate of freeway: " end_place
python3 src/main.py $start_place $end_place
