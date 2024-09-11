#!/bin/sh

./wait-for db:3306

python app/app.py
