#!/bin/bash

gunicorn 'main:app' --workers 4 --bind=0.0.0.0:8000