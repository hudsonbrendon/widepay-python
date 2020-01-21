install:
	pipenv run python setup.py install

black:
	black . --check

coverage:
	pipenv run coverage report -m

test:
	pipenv run python tests/tests.py

dev:
	make install
	make test