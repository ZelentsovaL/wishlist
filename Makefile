dev:
	poetry run uvicorn main:app --reload --host 0.0.0.0 --port 3000

build:
	docker-compose -f docker/docker-compose.yml --env-file .env --project-directory . up --build

deploy:
	docker-compose -f docker/docker-compose.yml --env-file .env --project-directory . up --build -d