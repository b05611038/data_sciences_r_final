# data_sciences_r_final
The final project in the data science r class in 2018 fall.

## Title
Traffic Flow Analysis and Travel Time Prediction of Taiwan Freeway

## Introduction
In the project, we try to improve the prediction of traveling time on the highway. We had found the website which has the same function just like our project. Thus, we do not imitate the function of the website. We focus on the more accurate prediction of traveling time on the highway.
Note: all program in the project is based on python3.5.2, please check the version is newer than it.


## Group member

```
NTU Bio Mechatronics Engineering, Yu-Tang Chang
NTU Bio Mechatronics Engineering, Jia-Yun Chen
NTNU Technology Application and Human Resource Development, Jing-Chun Yuan
```

## Slide

The slide we used in the final report in 2019/01/03 in National Taiwan University.
[slide link(Google drive)](https://drive.google.com/open?id=1__Q59EmY8x_fgnyUowpCQo0v-b45ZNBe)
[backup link(Github)](https://github.com/b05611038/data_sciences_r_final/blob/master/final_slide.pdf)


## Demo Video

The video we show the function of the project.
[Demo link(Google drive)](https://drive.google.com/open?id=1skdbr1zV2DkcQMjffKez-CGjDCFdtgZJ)


## Unix envirnment(MacOS, linux)
The main program will interact with user. It will print out the start gate where you drive on freeway, and it will also print the middle gate of the freeway which is in the midway of your traveling. The most important of the project is that the program will predict how much time you will need from start gate to end gate. The program also grab the time right now and it will help you knows when you will arrive.

### Setup
Please make sure that you have the premission of install python3 packages, and the package of wget and zips.
```sh
./setup.sh
``` 

### Main program

```sh
./run.sh
```

## Windows envirnement
Still working...

## Training Model
The shell script will grab the data from database and sort the data(if choose yes). Finally training the SVR model for travel time prediction in feature of time feature(00:00 and 00:30 will have different input to the model). Then, we labeled the vacation for different day feature. Also, we grab the data from the database in real time. Finally, all the features would concatenate and put into SVR model for training and prediction. The following is the program for user training. 

### Unix envirnment(MacOS, linux)

```sh
./train.sh
```

### Windows envirnement
Still working...

## Reference Website
The reference website we mentioned in the introduction.
[1968 website](https://1968.freeway.gov.tw/?fbclid=IwAR22C619V2EVBrwVWhagKkR_KAJHCcZwwWFbLVtFpm3drutHrtniHrP7o70)

