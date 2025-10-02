include common.mk

# Our directories
CITIES_DIR = cities
DB_DIR = data
REQ_DIR = .
SEC_DIR = security
SERVER_DIR = server

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

all_tests: FORCE
	cd $(CITIES_DIR); make tests
	cd $(SEC_DIR); make tests
	cd $(SERVER_DIR); make tests

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt
	@echo "You should set PYTHONPATH to: "
	@echo $(shell pwd)

docs: FORCE
	cd $(API_DIR); make docs
