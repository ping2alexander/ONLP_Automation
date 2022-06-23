#!/bin/sh

source ./../Scripts/testcaseList.sh

echo ${CommonTestcase_array[*]}

Usage ()
{
	echo "Usage: $0 [options]"
	echo "Option with (*) must be provided"
	echo "-t <testbed filename>		- Specify testbed filename(*)"
	echo "-s <individul script name>	- Specify test cases to execute. Default: Execute all testcases from Common list."
	echo "-lst <list of testcases>	- Specify the list of testcases to execute. Example: Common or Platform_<XXXXXX>. Default: Execute all testcases from Common list"
	echo "-r <report directory>		- Specify the report directory name"
}

ParseTestbedfile ()
{
	echo "***************************************************"
	echo "            Parsing testbed file                   "
	echo "***************************************************"

	echo "Check testbed file is present in the specific location"
	echo "Tesbed file location: $1"
	echo "Testbed filename: $2"
	
	if [ ! -f "$1/$2" ]
	then
		echo "Specified testbed file is not present in the location:  $1"
		exit 1;
	else
		echo "File exist"
	fi
	
}

DefaultTestcaselist ()
{
	echo ${CommonTestcase_array[*]}
}


ValidateCommandlineInput ()
{
	if [[ -z ${TESTBED} ]]; then 
		echo "TESTBED file is not set"
		Usage
		exit 1;
	fi
	if [[ -z ${SCRIPT} && -z ${TESTCASES} ]]; then 
		echo "Neither SCRIPT (-s) nor TESTCASE (-lst) is set.."
	fi
}

#Setting environment variable

SCRIPT=$0
FULL_PATH=$(realpath ${SCRIPT})
MAINPATH==$(dirname $FULL_PATH)
PARENTPATH=$(dirname $MAINPATH)
SCRIPT_PATH="${PARENTPATH}/Scripts"
TESTBED_PATH="${PARENTPATH}/cfg"
TMPFILEPATH="${PARENTPATH}/tmp"

# SCRIPT_PATH, TESTBED_PATH and TMPFILEPATH contains '=' as a starting character. Remove '=' from the sring using blow commands.

SCRIPT_PATH=`echo $SCRIPT_PATH | awk '{ print substr( $0, 2 ) }'`
TESTBED_PATH=`echo $TESTBED_PATH | awk '{ print substr( $0, 2 ) }'`
TMPFILEPATH=`echo $TMPFILEPATH | awk '{ print substr( $0, 2 ) }'`

LOG_PATH="${SCRIPT_PATH}/log"
TESTCASES=""
TESTBED=""
DEFAULT_TESTCASES=""
SCRIPT=""
REPORT=""

#echo "Script name : $SCRIPT"
#echo "Parent directory: $PARENTPATH"
#echo "Script location: $SCRIPT_PATH"
#echo "Testbed file location: $TESTBED_PATH"
#echo "Tmp file location: $TMPFILEPATH"

#if [ $# -lt 2 ]; then 
#	Usage
#	exit 1
#fi	

while getopts t:s:r:lst: flag
do
	case "${flag}" in
		t) TESTBED=${OPTARG};;
		s) SCRIPT=${OPTARG};;
		r) REPORT=${OPTARG};;
		lst) TESTCASES="${DEFAULT_TESTCASES} ${OPTARG}";;
		*) Usage;
			exit 1;;
	esac
done



#Parse testbed file and create a tmp file contains all test variable under: ./../tmp folder

DefaultTestcaselist
#ParseTestbedfile $TESTBED_PATH $testbed 

