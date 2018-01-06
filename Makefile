

dummy:
	@echo "Available targets:"
	@echo "    make install		Install to the system locations"


install:
	install -D mailback $(DESTDIR)/usr/bin/mailback


