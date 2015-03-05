#!/bin/bash

(mongod --dbpath=./database --noauth) |
(
sleep 2;
python handler.py
)
