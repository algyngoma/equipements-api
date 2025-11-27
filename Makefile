# ================== VARIABLES ==================
API      = http://localhost:8000
DC       = docker compose -f ../infra/docker-compose.yml

# Pour éviter que make crée des fichiers nommés comme les cibles
.PHONY: up down restart logs seed reset-db test dev lint format ci clean

# ================== DOCKER =====================
up:
	$(DC) up --build -d

down:
	$(DC) down -v

restart: down up

logs:
	$(DC) logs -f api

# ================== BDD / SEEDING ==============
seed:
	./bulk_post.sh

reset-db:
	docker exec mongo mongo --eval "db.dropDatabase()"

# ================== TESTS ======================
test:
	pytest -q

# ================== QUALITÉ CODE (OPTIONNEL) ===
lint:
	ruff app tests

format:
	black app tests

# ================== CI / UTILITAIRE ============
ci: test

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
