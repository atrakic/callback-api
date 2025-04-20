
OPTIONS ?= --build --remove-orphans --force-recreate

all:
	docker-compose up $(OPTIONS) -d

generator:
	[ -f ./scripts/$@.sh ] && bash ./scripts/$@.sh

test:
	[ -f ./tests/$@.sh ] && bash ./tests/$@.sh

clean:
	docker-compose down --remove-orphans -v --rmi local

