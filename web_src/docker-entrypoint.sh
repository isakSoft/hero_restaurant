#!/usr/bin/env bash

set -ex
echo "PWD=$PWD"

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
