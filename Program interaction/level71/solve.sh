#!/bin/bash

# Set the LC_CTYPE environment variable to AR_ar
command="/challenge/embryoio_level71 $(for ((i=1; i<=244; i++)); do echo -n "$i "; done) faomlytnlj"
main="env -i LC_CTYPE=AR_ar 37=kqmiraivsa  $command"
$main
