install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	echo "Not implemented yet"
	#python -m pytest -vv test_*.py

format:	
	black *.py dblib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib/*.py


all: install lint test