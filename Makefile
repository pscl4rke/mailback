

dummy:
	@echo "Available targets:"
	@echo "    make install		Install to the system locations"
	@echo "    make test		Run a very basic test suite"


install:
	install -D mailback.py $(DESTDIR)/usr/bin/mailback
	install -D mailback.1 $(DESTDIR)/usr/share/man/man1/mailback.1


test:
	python3 -m unittest discover


image-to-run += test-in-container-3.10-slim-bullseye
image-to-run += test-in-container-3.11-slim-bullseye
image-to-run += test-in-container-3.12-slim-bookworm
image-to-run += test-in-container-3.13-slim-bookworm

test-in-container: $(image-to-run)
	@echo
	@echo "=============================================================="
	@echo "Successfully tested all versions with ephemerun:"
	@echo "$^" | tr ' ' '\n'
	@echo "=============================================================="
	@echo

test-in-container-%:
	@echo
	@echo "=============================================================="
	@echo "Testing with docker.io/library/python:$*"
	@echo "=============================================================="
	@echo
	ephemerun \
		-i "docker.io/library/python:$*" \
		-v "`pwd`:/root/src:ro" \
		-W "/root/src" \
		-S "python -m unittest discover ." \
