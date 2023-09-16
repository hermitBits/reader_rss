python/setup: requirements.txt
	python3 -m virtualenv venv
	./venv/bin/pip install -r requirements.txt

python/lint: venv/bin/activate
	./venv/bin/python3 -m pylint *

python/run: venv/bin/activate
	./venv/bin/python3 main.py

python/clean:
	rm -rf venv

default: help