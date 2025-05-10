MAKEFLAGS += --silent

OPTIONS ?= --no-color --remove-orphans --build --force-recreate

.PHONY: all test clean

all:
	DOCKER_BUILDKIT=1 docker-compose up $(OPTIONS) -d

%:
	docker-compose up $(OPTIONS) $@ -d # --exit-code-from postman
	docker-compose ps -a

generator:
	[ -f ./scripts/$@.sh ] && bash ./scripts/$@.sh

test:
	[ -f ./tests/$@.sh ] && bash ./tests/$@.sh

clean:
	docker-compose down --remove-orphans -v --rmi local
