#!/bin/bash

virtualenv env --quiet --distribute
source env/bin/activate
pip install -q -r requirements.txt --download-cache=cache/pip

