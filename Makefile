setup:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
install:
	pip install .
check:
	pip check
	PYTHONPATH=calibpy pytest
lint:
	flake8 --version
	flake8
	echo TODO hatch fmt -l
