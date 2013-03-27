#!/bin/bash
CACHE_DIR=/var/tmp/pipcache
virtualenv env
source env/bin/activate
mkdir -p ${CACHE_DIR}
pip install --download-cache=${CACHE_DIR} -r requirements.txt
