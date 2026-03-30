DOCKER_COMPOSE := docker compose
OS := $(shell uname)

build:
ifeq ($(OS),Linux)
	@echo "Building for linux"
	$(DOCKER_COMPOSE) build
endif

run:
ifeq ($(OS),Linux)
	@echo "Running for Linux"
	$(DOCKER_COMPOSE) up -d
endif

stop:
	$(DOCKER_COMPOSE) down 

clean: stop
	$(DOCKER_COMPOSE) rm -f
	docker system prune -y
