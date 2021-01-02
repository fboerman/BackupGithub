#!/usr/bin/env bash

mkdir -p repos
mv giturls.txt repos/
cd repos
cat giturls.txt | parallel --bar -j16 git clone --quiet {}