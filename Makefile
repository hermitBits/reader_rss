VIRTUALENV_NOME=venv
EXE_PYTHON=python3
EXE_PIP=pip
PATH_LINT=*

default: ajuda

python/configura: requirements.txt ## Cria virtualenv e instala as dependencias de pacotes
	${EXE_PYTHON} -m virtualenv ${VIRTUALENV_NOME}
	./${VIRTUALENV_NOME}/bin/${EXE_PIP} install -r requirements.txt

python/lint: ${VIRTUALENV_NOME}/bin/activate ## Faz checagem de codestyle com pylint
	./${VIRTUALENV_NOME}/bin/${EXE_PYTHON} -m pylint ${PATH_LINT}

python/executar: ${VIRTUALENV_NOME}/bin/activate ## Executa o código
	./${VIRTUALENV_NOME}/bin/${EXE_PYTHON} main.py

python/limpar: ## limpa o ambiente virtual criado
	@find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@rm -rf ${VIRTUALENV_NOME} .pytest_cache .coverage htmlcov

python/teste: ${VIRTUALENV_NOME}/bin/activate ## executa testes
	./${VIRTUALENV_NOME}/bin/${EXE_PYTHON} -m coverage run -m pytest -v
	./${VIRTUALENV_NOME}/bin/${EXE_PYTHON} -m coverage html
	@open htmlcov/index.html

.PHONY: ajuda
ajuda: ## show help message
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
