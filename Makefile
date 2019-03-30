all: run

gen-proto:
	protoc --python_out='.' ./content_creation_db/protos/*.proto

init_db:
	python -m content_creation_db.db.main

venv:
	pipenv shell

run:
	pipenv run server
