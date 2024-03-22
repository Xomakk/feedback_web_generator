#!/bin/bash

gigachain install-rus-certs

exec gunicorn -w 4 'main:app' --bind=0.0.0.0:5000