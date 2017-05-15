all: docs publish

docs: FORCE
	pandoc README.md -o docs/source/README.rst; \
	jupyter nbconvert tests/test_jdc.ipynb --to rst --execute; \
	mv tests/test_jdc.rst docs/source/test.rst; \
	cd docs/; \
	sphinx-apidoc -e -f -M -o ./ ../; \
	make html

publish: FORCE
	mkdir -p ~/pages/jdc/; \
	cd ~/pages/jdc/; \
	git rm -r *; \
	mkdir -p ~/pages/jdc/; \
	cp -r ~/code/jdc/docs/build/html/* ~/pages/jdc/; \
	cd ~/pages/jdc/; \
	touch .nojekyll; \
	git add *; \
	git add .nojekyll; \
	git commit -am "$(shell git log -1 --pretty=%B | tr -d '\n')"; \
	git push origin gh-pages; \
	cd ~/code/jdc

FORCE:
