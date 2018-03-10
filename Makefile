

dummy:
	@echo "Available targets:"
	@echo "    make install		Install to the system locations"


install:
	install -D mailback $(DESTDIR)/usr/bin/mailback
	install -D mailback.1 $(DESTDIR)/usr/share/man/man1/mailback.1
