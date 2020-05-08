

dummy:
	@echo "Available targets:"
	@echo "    make install		Install to the system locations"
	@echo "    make test		Run a very basic test suite"


install:
	install -D mailback.py $(DESTDIR)/usr/bin/mailback
	install -D mailback.1 $(DESTDIR)/usr/share/man/man1/mailback.1


test:
	python3 -m unittest discover
