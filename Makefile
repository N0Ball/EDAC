.PHONY: all

build-docs:
	gendocs --config mkgendocs.yml

docs: build-docs
	mkdocs serve

create_docs: build-docs
	mkdocs gh-deploy