#!/bin/bash

opencv_createsamples -info cars.info -num 8695 -w 48 -h 24 -vec cars.vec

opencv_traincascade -data data -vec cars.vec -bg bg.txt -numPos 8650 -numNeg 500 -numStages 10 -w 48 -h 24 -featureType LBP
