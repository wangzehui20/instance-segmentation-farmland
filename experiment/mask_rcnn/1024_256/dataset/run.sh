#!/usr/bin/env bash

echo "start..."
python contours2shp.py
wait
python removeshp_overlap.py
echo "end..."