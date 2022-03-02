.PHONY: all

build-docs:
	gendocs --config mkgendocs.yml

view-docs: build-docs
	mkdocs serve

deploy-docs: build-docs
	mkdocs gh-deploy