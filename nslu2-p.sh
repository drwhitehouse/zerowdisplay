#!/bin/bash

RED=$(( $RANDOM % 256 ))
GREEN=$(( $RANDOM % 256 ))
BLUE=$(( $RANDOM % 256 ))

curl http://chowfaan.hot.dim-sum.home:5000/pt/$RED/$GREEN/$BLUE
