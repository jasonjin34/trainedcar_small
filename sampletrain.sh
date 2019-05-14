#!/bin/bash

opencv_createsamples -info cars.info -num 550 -w 48 -h 24 -vec cars.vec

opencv_traincascade -data data -vec cars.vec -bg bg.txt -numPos 500 -numNeg 512 -numStages 20 -w 48 -h 24 -featureType LBP
