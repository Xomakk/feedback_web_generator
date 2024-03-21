#!/bin/bash

gigachain install-rus-certs

gunicorn -w 4 'main:app'