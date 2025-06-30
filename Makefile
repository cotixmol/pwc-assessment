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

alembic-migrate:
	@echo "Running Alembic migrations inside the api container..."
	docker-compose exec api alembic upgrade head

bash:
	@echo "Opening a shell inside the api container..."
	docker-compose exec api bash