install: requirements.txt web_sandbox/
	( \
		virtualenv -p python3 wenv; \
		. wenv/bin/activate; \
		pip3 install -r requirements.txt; \
		pip3 install -e .; \
	)
run: web_sandbox/ instance/
	( \
		. wenv/bin/activate; \
		flask run; \
	)