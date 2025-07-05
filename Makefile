up:
	@echo "Building images and starting containers in detached mode..."
	docker-compose up --build -d

down:
	@echo "Stopping and removing containers..."
	docker-compose down

restart:
	@echo "Restarting services..."
	docker-compose restart

logs:
	@echo "Following logs..."
	docker-compose logs -f

alembic-autogenerate:
	@read -p "Enter migration name: " name; \
	echo "Running Alembic autogenerate inside the api container..."; \
	alembic revision --autogenerate -m "$$name"

alembic-migrate:
	@echo "Running Alembic migrations inside the api container..."
	docker-compose exec api alembic upgrade head

docker-terminal:
	@echo "Opening a shell inside the api container..."
	docker-compose exec api bash

pre-commit:
	@echo "Running pre-commit hooks..."
	pre-commit run --all-files
