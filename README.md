# data_sciences_r_final
The final project in the data science r class in 2018 fall

## Title
Traffic Flow Analysis and Travel Time Prediction of Taiwan Freeway

## Introduction
In the project, we try to improve the prediction of traveling time on the highway. We had found the website which has the same function just like our project. Thus, we do not imitate the function of the website. We focus on the more accurate prediction of traveling time on the highway.


## Group member

```
NTU Bio Mechatronics Engineering, Yu-Tang Chang
NTU Bio Mechatronics Engineering, Jia-Yun Chen
NTNU Technology Application and Human Resource Development, Jing-Chun Yuan
```

## Slide

The slide we used in the final report in 2019/01/03 in National Taiwan University.
[slide link]()


## Demo Video

The video we show the function of the project.
[Demo link]()


## Unix envirnment(MacOS, linux)

```sh
./run.sh
```

## Windows envirnement
Still working...

## Training Model
The shell script will grab the data from database and sort the data. Finally training the SVR model for travel time prediction in feature of time feature(00:00 and 00:30 will have different input to the model). Then, we labeled the vacation for different day feature. Also, we grab the data from the database in real time. Finally, all the features would concatenate and put into SVR model for training and prediction. The following is the program for user training. 

```sh
./train.sh
```

## Reference Website
The reference website we mentioned in the introduction.
[1968 website](https://1968.freeway.gov.tw/?fbclid=IwAR22C619V2EVBrwVWhagKkR_KAJHCcZwwWFbLVtFpm3drutHrtniHrP7o70)

