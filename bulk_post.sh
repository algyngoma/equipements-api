#!/bin/bash

echo "---- IMPORT ÉQUIPEMENTS ----"

jq -c '.[]' equipements_bulk.json | while read item; do
  echo "→ Envoi : $item"
  curl -X POST http://localhost:8000/equipements/ \
    -H "Content-Type: application/json" \
    -d "$item"
  echo -e "\n"
done

echo "---- GET ALL ----"
curl -X GET http://localhost:8000/equipements/
echo -e "\n"
