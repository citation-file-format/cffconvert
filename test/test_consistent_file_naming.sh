#!/bin/bash

function check_file_naming {
    for s in $strings
    do
        left=$(echo $s  | rev | cut -d'/' -f-2 | cut -c 4- | rev | cut -c -2)
        right=$(echo $s | rev | cut -d'/' -f-2 | cut -c 4- | cut -c -2 | rev)
        if [ $left != $right ]
        then
            echo "Inconsistently named file: $s"
            HAS_ERRORS=1
        fi
    done
}

arg=$1

HAS_ERRORS=0

if [ $arg = 'test' ]
then 
    strings=$(find . | grep "./test/$SCHEMA_VERSION/.*\.py$")
    check_file_naming
elif [ $arg = 'clitest' ]
then 
    strings=$(find . | grep "./clitest/$SCHEMA_VERSION/.*\.py$")
    check_file_naming
elif [ $arg = 'livetest' ]
then
    strings=$(find . | grep "./livetest/.*\.py$")
    check_file_naming
else
    exit 1
fi

exit $HAS_ERRORS