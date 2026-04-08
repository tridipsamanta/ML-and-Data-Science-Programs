#!/bin/bash#!/bin/bash

cd "/Users/tridipsamanta/Desktop/My Projects/Data Science programs..."

echo "Commit at $(date)" >> log.txt

git add log.txt
git commit -m "Daily auto commit $(date)"
git push

date >> log.txt
git add log.txt
git commit -m "Daily update $(date)"
git push
