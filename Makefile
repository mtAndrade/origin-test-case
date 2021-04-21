PORT ?= 8080
PROJECT ?= origin
MODULE ?= risk_profiler

PYTHONPATH=$(shell pwd)
ENVIRONMENT_CMD ?= PYTHONPATH="${PYTHONPATH}" pipenv run
DOCKER_PARAMS ?= -f docker/ports.yml 
DOCKER_CMD = docker-compose -f docker-compose.yml ${DOCKER_PARAMS} -p ${PROJECT}

install: 
	pipenv install

start:
	@echo "[STARTING aiohttp LOCAL SERVER 0.0.0.0:$(PORT)]"
	@$(ENVIRONMENT_CMD) python -m ${MODULE}

test:
	@echo "START Tests"
	@$(ENVIRONMENT_CMD) python -m unittest discover -s tests -p "*_test.py" --verbose

docker-build: 
	@$(DOCKER_CMD) build

docker-start: 
	@$(DOCKER_CMD) up -d

docker-test: docker-start
	@echo "\n\n[RUNNING TESTS]\n"
	@${DOCKER_CMD} run web make test
