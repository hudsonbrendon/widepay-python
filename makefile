install:
	pipenv run python setup.py install

test:
	make install
	pipenv run python tests/tests.py

