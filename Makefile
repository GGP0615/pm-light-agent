.PHONY: build deploy test lint

build:
	docker build -t pm-light-agent:latest .

deploy:
	gcloud builds submit --config infra/cloudbuild.yaml .

lint:
	flake8 .

test:
	pytest
