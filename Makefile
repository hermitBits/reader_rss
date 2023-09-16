.PHONY: help
help: ## show help message
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

python/setup: requirements.txt ## Cria virtualenv e instala as dependencias de pacotes
	python3 -m virtualenv venv
	./venv/bin/pip install -r requirements.txt

python/lint: venv/bin/activate ## Faz checagem de codestyle com pylint
	./venv/bin/python3 -m pylint *

python/run: venv/bin/activate ## Executa o código
	./venv/bin/python3 main.py

python/clean: ## limpa o ambiente virtual criado
	rm -rf venv
