#!/bin/bash

source ./../Scripts/testcaseList.sh

Usage ()
{
	echo "Usage: $0 [options]"
	echo "Option with (*) must be provided"
	echo "-t <testbed filename>		- Specify testbed filename(*)"
	echo "-s <individul script name>	- Specify test cases to execute. Default: Execute all testcases from Common list."
	echo "-l <list of testcases>		- Specify the list of testcases to execute. Example: Common or Platform_<XXXXXX>. Default: Execute all testcases from Common list"
	echo "-r <report directory>		- Specify the report directory name"
	echo "-f <tempfilename> 		- Specify the temp filename where all testbed and system information will be stored as python variable(*)"
}

CheckTestbedFilePresence ()
{
	echo "***************************************************"
	echo "            Check testbed file presence            "
	echo "***************************************************"

	echo "Check testbed file is present in the specific location"
	echo "Tesbed file location: $1"
	echo "Testbed filename: $2"
	
	if [ ! -f "$1/$2" ]
	then
		echo "Specified testbed file is not present in the location:  $1"
		exit 1;
	else
		echo "Testbed file exist in the location"
	fi
	
}


ValidateCommandlineInput ()
{
	if [[ -z ${TESTBED} ]]; then 
		echo "Error: Argument is missing - TESTBED file is not set"
		Usage
		exit 1;
	fi
	if [[ -z ${SCRIPT} && -z ${LIST} ]]; then 
		echo "Neither SCRIPT (-s) nor TESTCASES (-lst) is set."
		echo "Switch to default mode:"
		TESTCASES=${CommonTestcase_array[*]}
	elif [[ ! -z ${SCRIPT} && ! -z ${LIST} ]] ; then
		#When script and  list are passed as inputs, then script will take higher priority and run	
		TESTCASES=${SCRIPT}
	elif [[ ! -z ${SCRIPT} || -z ${LIST} ]] ; then
                TESTCASES=${SCRIPT}
	elif [[ -z ${SCRIPT} || ! ! ! ! ! ! ! ! -z ${LIST} ]] ; then
                TESTCASES=${LIST}
	else
		TESTCASES=${CommonTestcase_array[*]}
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
PYTHONPATH="${PARENTPATH}/Lib"

# SCRIPT_PATH, TESTBED_PATH and TMPFILEPATH contains '=' as a starting character. Remove '=' from the sring using blow commands.

SCRIPT_PATH=`echo $SCRIPT_PATH | awk '{ print substr( $0, 2 ) }'`
TESTBED_PATH=`echo $TESTBED_PATH | awk '{ print substr( $0, 2 ) }'`
TMPFILEPATH=`echo $TMPFILEPATH | awk '{ print substr( $0, 2 ) }'`
PYTHONPATH=`echo $PYTHONPATH | awk '{ print substr( $0, 2 ) }'`

export LIB_Folder=$PYTHONPATH

LOG_PATH="${SCRIPT_PATH}/log"
LIST=None
TESTBED=""
DEFAULT_TESTCASES="Common"
SCRIPT=None
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

while getopts t:s:r:l:f: flag
do
	case "${flag}" in
		t) TESTBED=${OPTARG};;
		s) SCRIPT=${OPTARG};;
		r) REPORT=${OPTARG};;
		l) LIST="${OPTARG}";;
		f) TEMPFILE="${OPTARG}";;
		*) Usage;
			exit 1;;
	esac
done

export 

# Check whether all mandatory command-line arguments are provided as input. If not, return error and print help text.

ValidateCommandlineInput

CheckTestbedFilePresence $TESTBED_PATH $TESTBED

#Parse testbed file and create a tmp file contains all test variable under: ./../tmp folder

DEBUG='-v'
CONSOLE_LOG='-s'
FILENAME=${TEMPFILE}
EXTRA_CLI_ARGUMENT="--filename ${FILENAME} --testbed ${TESTBED}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_testbed_file_parser.py ${EXTRA_CLI_ARGUMENT} --alluredir=web


# Gather system information from all DUT's and store it in the tmp file.

EXTRA_CLI_ARGUMENT_LIST="--filename ${FILENAME}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_collectSystemData.py ${EXTRA_CLI_ARGUMENT_LIST}

#Testcase execution start

echo $TESTCASES

#Testcase exection end
