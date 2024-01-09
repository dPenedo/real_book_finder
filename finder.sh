#!/bin/bash

echo "What Real Book Tune you want to find?"
read tune_to_find

grep -A 1 -ir "$tune_to_find" *.json

