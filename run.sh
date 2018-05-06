#!/bin/bash

SCNAME='server'
screen -AmdS $SCNAME sudo python3 manage.py runserver 0.0.0.0:80
