#!/bin/bash

curl -X POST http://localhost:8000/equipements/ \
  -H "Content-Type: application/json" \
  -d @equipement.json
    