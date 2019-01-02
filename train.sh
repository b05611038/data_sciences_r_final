#!/bin/bash
read -p "Please check that you wants to crawl the data from the freeway database(yes or no) " check
if [ $check == "yes" ];then
    read -p "Please input the starting year you want to grab data(from 2013): " grab_year
    python3 src/crawl_process.py $grab_year;
fi
read -p "Please input the time range of training data, please input start time(ex. 2013/1/1): " start_time
read -p "Please input the time range of training data, please input end time(ex. 2019/1/1): " end_time
read -p "Please input the parameter C for SVR training(larger means more precise model): " C
python3 src/training_process.py $start_time $end_time $C
