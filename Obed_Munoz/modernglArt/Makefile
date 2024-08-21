# build & test automation
APP_NAME=linesArt
SHELL := /bin/bash

all:
	python ./${APP_NAME}.py

deps:
	pip install numpy
	pip install Pillow
	pip install moderngl

virtualenv:
	virtualenv .venv

clean:
	rm -rf *.o ${APP_NAME}
