NAME="libvirt_exporter"
VERSION?=$(shell cat VERSION)
TOKEN?="TODO: SET A TOKEN"
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64"
	cp libvirt_exporter "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild/SOURCES" && tar cvfz $(NAME)-$(VERSION).linux-amd64.tar.gz $(NAME)-$(VERSION).linux-amd64
	rpmbuild --define "version $(VERSION)" --define '_topdir '"$(PWD)/rpmbuild" -ba --clean contrib/$(NAME).spec

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64"
	rm -f "$(PWD)/rpmbuild/SOURCES/$(NAME)-$(VERSION).linux-amd64.tar.gz"
