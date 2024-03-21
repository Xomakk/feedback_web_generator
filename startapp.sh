#!/bin/bash

gigachain install-rus-certs

gunicorn -w 4 'main:app' --bind=0.0.0.0:8000