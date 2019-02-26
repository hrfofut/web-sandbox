# Download and install dependencies
install: requirements.txt web_sandbox/
	( \
		virtualenv -p python3 wenv; \
		. wenv/bin/activate; \
		pip3 install -r requirements.txt; \
	)
# Test website locally
run: web_sandbox/ instance/
	( \
		. wenv/bin/activate; \
		flask run; \
	)# Test website locally

run_chat: web_sandbox/ instance/
	( \
		. wenv/bin/activate; \
		python3 web_sandbox/chat.py; \
	)