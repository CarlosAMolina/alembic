alembic-autogenerate-first:
	alembic revision --autogenerate -m "add customers model"

alembic-downgrade:
	alembic downgrade -1

alembic-run-migration:
	alembic upgrade head

docker-run:
	docker compose up -d

docker-stop:
	docker compose down

