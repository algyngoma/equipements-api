#!/bin/bash

echo "---- POST test ----"
curl -X POST http://localhost:8000/equipements/ \
  -H "Content-Type: application/json" \
  -d @equipement.json

echo -e "\n---- GET all ----"
curl -X GET http://localhost:8000/equipements/

echo -e "\n---- GET 1 ----"
curl -X GET http://localhost:8000/equipements/1

echo -e "\n---- DELETE 1 ----"
curl -X DELETE http://localhost:8000/equipements/1

echo -e "\n---- GET all ----"
curl -X GET http://localhost:8000/equipements/
