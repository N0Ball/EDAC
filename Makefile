.PHONY: all

build-docs:
	gendocs --config mkgendocs.yml

docs: build-docs
	mkdocs serve

deploy_docs: build-docs
	mkdocs gh-deploy