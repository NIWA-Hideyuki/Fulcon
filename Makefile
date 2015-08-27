# Fulcon
# Copyright (C) 2015 NIWA Hideyuki

VERSION=0.1


fulcon :
	(cd src && make)

install :
	(cd src && make install)

uninstall :
	(cd src && make uninstall)

clean :
	(cd src && make clean)
