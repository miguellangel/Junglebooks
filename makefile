ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Windows
    PYTHON   := python                 # on my machine it's python
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := python -m pydoc        # on my machine it's pydoc
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
endif


website:
	FLASK_APP=main.py FLASK_DEBUG=1 $(PYTHON) -m flask run

log:
	git log > IDB3.log

pydoc:
	$(PYDOC) -w models

test-website:
	$(PYTHON) test.py

SHA:
	git rev-parse HEAD

test: IDB2.log pydoc test-website SHA 
