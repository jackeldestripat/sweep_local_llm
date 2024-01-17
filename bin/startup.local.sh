#!/bin/sh

redis-server redis.conf --bind 0.0.0.0 --port 6379 &
PYTHONPATH=. python sweepai/watch.py
