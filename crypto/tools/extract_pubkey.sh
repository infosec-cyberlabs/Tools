#!/bin/bash
# @Author: John Hammond
# @Date:   2016-12-25 23:20:21
# @Last Modified by:   John Hammond
# @Last Modified time: 2017-01-01 20:24:59


RED=`tput setaf 1`
NC=`tput sgr0`


if [ "$1" == "" ]
then
	echo "${RED}Please enter a filename! $NC"
	echo "usage: $0 [publickey.pub]"
	exit -1
else

	full_output=`openssl rsa -pubin -in $1 -text -noout|tr -d "\n"`
	modulus=$(echo $full_output | grep -oE "Modulus(.*?)Exponent")
	modulus=${modulus/Modulus: }
	modulus=${modulus/Exponent}
	modulus=$(echo $modulus | tr -d " " | tr -d ":" | cut -d "(" -f2| cut -d ")" -f1)

	modulus=`python -c "print int(\"$modulus\",16)"`

	exponent=$(echo $full_output | grep -oE "Exponent(.*)")
	exponent=${exponent/Exponent}
	exponent=$(echo $exponent | tr -d " " | tr -d ":" | cut -d "(" -f2| cut -d ")" -f1)

	exponent=`python -c "print int(\"$exponent\",16)"`


	echo n=$modulus
	echo ""
	echo e=$exponent


fi




