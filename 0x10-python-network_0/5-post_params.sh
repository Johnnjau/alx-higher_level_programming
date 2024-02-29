#!/bin/bash
#sends POST request specifiying email and subject value
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
