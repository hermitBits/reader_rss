VIRTUALENV_NAME=venv
PYTHON_EXE=python3
PIP_EXE=pip
PATH_LINT=*

default: help

python/setup: requirements.txt ## Cria virtualenv e instala as dependencias de pacotes
	${PYTHON_EXE} -m virtualenv ${VIRTUALENV_NAME}
	./${VIRTUALENV_NAME}/bin/${PIP_EXE} install -r requirements.txt

python/lint: ${VIRTUALENV_NAME}/bin/activate ## Faz checagem de codestyle com pylint
	./${VIRTUALENV_NAME}/bin/${PYTHON_EXE} -m pylint ${PATH_LINT}

python/run: ${VIRTUALENV_NAME}/bin/activate ## Executa o código
	./${VIRTUALENV_NAME}/bin/${PYTHON_EXE} main.py

python/clean: ## limpa o ambiente virtual criado
	@find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@rm -rf ${VIRTUALENV_NAME}

python/tests: ${VIRTUALENV_NAME}/bin/activate ## executa testes
	./${VIRTUALENV_NAME}/bin/${PYTHON_EXE} -m pytest -v

.PHONY: help
help: ## show help message
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
