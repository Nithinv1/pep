# Builds PEP files to HTML using sphinx

PYTHON=python3
VENV_DIR=venv
JOBS=8
RENDER_COMMAND=$(PYTHON) build.py -j $(JOBS)

render:
	$(RENDER_COMMAND)

pages: rss
	$(RENDER_COMMAND) --build-dirs

fail-warning:
	$(RENDER_COMMAND) --fail-on-warning

check-links:
	$(RENDER_COMMAND) --check-links

rss:
	$(PYTHON) generate_rss.py

clean:
	-rm -rf build

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	./$(VENV_DIR)/bin/python -m pip install -r requirements.txt

lint:
	$(PYTHON) -m pre_commit --version > /dev/null || $(PYTHON) -m pip install pre-commit
	$(PYTHON) -m pre_commit run --all-files

spellcheck:
	$(PYTHON) -m pre_commit --version > /dev/null || $(PYTHON) -m pip install pre-commit
	$(PYTHON) -m pre_commit run --all-files --hook-stage manual codespell
