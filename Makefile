OPTIONS ?= --no-color --remove-orphans --build --force-recreate

all:
	DOCKER_BUILDKIT=1 docker-compose up $(OPTIONS) -d

%:
	docker-compose up $(OPTIONS) $@ --exit-code-from postman
	docker-compose ps -a

generator:
	[ -f ./scripts/$@.sh ] && bash ./scripts/$@.sh

test:
	[ -f ./tests/$@.sh ] && bash ./tests/$@.sh

clean:
	docker-compose down --remove-orphans -v --rmi local
