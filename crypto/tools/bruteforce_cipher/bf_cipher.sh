#!/bin/bash

# Just some colors to add spice...
RED=`tput setaf 1`							# code for red console text
GREEN=`tput setaf 2`						# code for green text
NC=`tput sgr0`								# Reset the text color


# Set this to nothing by default, to test if they have been set later...
ENCRYPTED_FILE=""
KEY=""

function display_help() {
	cat <<EOF
Usage:
	$0 -f ENCRYPTED_FILE -k KEY

Parameters:
	-f
		Specify the encrypted file that will be created and used for this server.
		
	-k
		Specify the suspected key that should decrypt the encrypted file (supplied with -f)

	-h
		Display this help message

Credits:
	This script was originally found through this writeup:
	https://github.com/Beers4Flags/writeups/tree/master/hackit2016/network/australia-voice-of-the-future
	I have only modified it to make it a bit more of a universal tool.
EOF
}

while getopts k:f:h opt; do

	case $opt in
		k)
			echo "$0: ${GREEN}using key ${OPTARG}${NC}"
			KEY=$OPTARG
			;;
		f)
			echo "$0: ${GREEN}using encrypted file ${OPTARG}${NC}"
			ENCRYPTED_FILE=$OPTARG
			;;
		h)
			display_help
			exit 0
			;;
		\?)
			exit -1
			;;
	esac
done


# Make sure we supplied the parameters we need.
if [ "$ENCRYPTED_FILE" == "" ]; then
	echo "$0: ${RED}you must specify an encrypted file to test against!${NC}"
	display_help
	exit -1
fi

if [ "$KEY" == "" ]; then
	echo "$0: ${RED}you must specify a key to test with!${NC}"
	display_help
	exit -1
fi



CIPHERLIST="-aes-128-cbc               -aes-128-cbc-hmac-sha1     -aes-128-cbc-hmac-sha256   -aes-128-ccm               -aes-128-cfb               -aes-128-cfb1              -aes-128-cfb8              -aes-128-ctr               -aes-128-ecb               -aes-128-gcm               -aes-128-ofb               -aes-128-xts               -aes-192-cbc               -aes-192-ccm               -aes-192-cfb               -aes-192-cfb1              -aes-192-cfb8              -aes-192-ctr               -aes-192-ecb               -aes-192-gcm               -aes-192-ofb               -aes-256-cbc               -aes-256-cbc-hmac-sha1     -aes-256-cbc-hmac-sha256   -aes-256-ccm               -aes-256-cfb               -aes-256-cfb1              -aes-256-cfb8              -aes-256-ctr               -aes-256-ecb               -aes-256-gcm               -aes-256-ofb               -aes-256-xts               -aes128                    -aes192                    -aes256                    -bf                        -bf-cbc                    -bf-cfb                    -bf-ecb                    -bf-ofb                    -blowfish                  -camellia-128-cbc          -camellia-128-cfb          -camellia-128-cfb1         -camellia-128-cfb8         -camellia-128-ecb          -camellia-128-ofb          -camellia-192-cbc          -camellia-192-cfb          -camellia-192-cfb1         -camellia-192-cfb8         -camellia-192-ecb          -camellia-192-ofb          -camellia-256-cbc          -camellia-256-cfb          -camellia-256-cfb1         -camellia-256-cfb8         -camellia-256-ecb          -camellia-256-ofb          -camellia128               -camellia192               -camellia256               -cast                      -cast-cbc                  -cast5-cbc                 -cast5-cfb                 -cast5-ecb                 -cast5-ofb                 -des                       -des-cbc                   -des-cfb                   -des-cfb1                  -des-cfb8                  -des-ecb                   -des-ede                   -des-ede-cbc               -des-ede-cfb               -des-ede-ofb               -des-ede3                  -des-ede3-cbc              -des-ede3-cfb              -des-ede3-cfb1             -des-ede3-cfb8             -des-ede3-ofb              -des-ofb                   -des3                      -desx                      -desx-cbc                  -id-aes128-CCM             -id-aes128-GCM             -id-aes128-wrap            -id-aes128-wrap-pad        -id-aes192-CCM             -id-aes192-GCM             -id-aes192-wrap            -id-aes192-wrap-pad        -id-aes256-CCM             -id-aes256-GCM             -id-aes256-wrap            -id-aes256-wrap-pad        -id-smime-alg-CMS3DESwrap  -idea                      -idea-cbc                  -idea-cfb                  -idea-ecb                  -idea-ofb                  -rc2                       -rc2-40-cbc                -rc2-64-cbc                -rc2-cbc                   -rc2-cfb                   -rc2-ecb                   -rc2-ofb                   -rc4                       -rc4-40                    -rc4-hmac-md5              -rc5                       -rc5-cbc                   -rc5-cfb                   -rc5-ecb                   -rc5-ofb                   -seed                      -seed-cbc                  -seed-cfb                  -seed-ecb                  -seed-ofb "

#KEY="75948631736985999017212639734863100000"
for mode in $CIPHERLIST
do
	echo "$0: ${GREEN}trying '$mode' ... ${NC}"
    openssl enc -d -in "$ENCRYPTED_FILE" -out file__"$mode".dec -k "$KEY" $mode
done