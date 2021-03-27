#!/bin/bash
# Remove comments after $endif, which are causing warning when running ./autogen.sh 

if [ -w abrt.spec.in ]
then
	sed -i -e 's/%endif.*$/%endif/g' ./abrt.spec.in
	echo "Done!"

else
	echo "File not found"
	exit 1
fi	
