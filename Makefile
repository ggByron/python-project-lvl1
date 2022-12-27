install:
	poetry install

brain-even:
	poetry run brain-even

brain-games:
	poetry run brain-games

build:
	poetry build

lint:
	poetry run flake8 brain_games

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

publish:
	poetry publish --dry-run
