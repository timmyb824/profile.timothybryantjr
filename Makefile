pip-compile:
	pip install pip-tools pip-autoremove

compile-deps:
	pip-compile -o src/requirements.txt pyproject.toml

compile-dev-deps:
	pip-compile --extra dev -o requirements-dev.txt pyproject.toml

install-deps:
	pip install -r src/requirements.txt

install-dev-deps:
	pip install -r requirements-dev.txt

run:
	python src/main.py

run-app:
	gunicorn --config ./configs/gunicorn_config.py src.main:app --reload

run-app-docker:
	docker-compose up -d --force-recreate --build

