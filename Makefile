all:
	docker-compose up -d

clean:
	docker-compose down --remove-orphans -v --rmi local
