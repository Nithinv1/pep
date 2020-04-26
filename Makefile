# Rules to only make the required HTML versions, not all of them,
# without the user having to keep track of which.
#
# Not really important, but convenient.

PYTHON=python3

all: sphinx

sphinx:
	$(PYTHON) build.py

rss:
	$(PYTHON) pep2rss.py .

install:
	echo "Installing is not necessary anymore. It will be done in post-commit."

clean:
	-rm pep-0000.rst
	-rm *.html
	-rm -rf build

update:
	git pull https://github.com/python/peps.git

venv:
	$(PYTHON) -m venv venv
	./venv/bin/python -m pip install -U docutils sphinx

package: all rss
	mkdir -p package/peps
	$(PYTHON) package.py
	cp pep-*.txt build/peps/
	cp pep-*.rst build/peps/
	cp *.png build/peps/
	cp *.rss package/peps
	tar -C package -czf package/peps.tar.gz peps
