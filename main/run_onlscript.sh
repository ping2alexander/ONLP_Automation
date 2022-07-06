#!/bin/bash


Usage ()
{
	echo -e "\e[1;32mUsage: $0 [options]"
	echo -e "\e[1;32mOption with (*) must be provided"
	echo -e "\e[1;32m-t <testbed filename>		- Specify testbed filename(*)"
	echo -e "\e[1;32m-s <individul script name>	- Specify test cases to execute."
	#echo -e "\e[1;32m-l <list of testcases>		- Specify the list of testcases to execute. Example: Common or Platform_<XXXXXX>. Default: Execute all testcases from Common list"
	echo -e "\e[1;32m-r <report directory>		- Specify the report directory name"
	echo -e "\e[1;32m-f <tempfilename> 		- Specify the temp filename where all testbed and system information will be stored as python variable(*)"
	echo -e "\e[1;32m-m <pytestmarker>		- Specity the testcase groupname"
	echo -e "\e[1;33m				  Example: -m \"All\" or -m \"Sanity\"" 
	echo -e "\e[1;33m					   -m \"Belgite\""
							  
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
		echo "\e[1;31mError:Specified testbed file is not present in the location:  $1"
		exit 1;
	else
		echo "\e[1;32mTestbed file exist in the location"
	fi
	
}


ValidateCommandlineInput ()
{
	if [[ -z ${TESTBED} ]]; then 
		echo -e "\e[1;31mError: Argument is missing - TESTBED file is not set"
		Usage
		exit 1;
	fi
	if [[ -z ${MARKER} ]]; then
		MARKER='All'
	fi
	
	#if [[ -z ${SCRIPT} && -z ${LIST} ]]; then 
	#	echo "\e[1;32mNeither SCRIPT (-s) nor TESTCASES (-lst) is set."
	#	echo "\e[1;32mSwitch to default mode:"
	#	TESTCASES=${CommonTestcase_array[*]}
	#elif [[ ! -z ${SCRIPT} && ! -z ${LIST} ]] ; then
	#	#When script and  list are passed as inputs, then script will take higher priority and run	
	#	TESTCASES=${SCRIPT}
	if [[ ! -z ${SCRIPT} ]]; then
               TESTCASES=${SCRIPT}
	fi
	#elif [[ ! -z ${LIST} ]] ; then
        #        TESTCASES=${LIST}
	#else
	#	TESTCASES=${CommonTestcase_array[*]}
	#fi

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

#export LIB_Folder=$PYTHONPATH

LOG_PATH="${SCRIPT_PATH}/log"
LIST=""
TESTBED=""
DEFAULT_TESTCASES="Common"
SCRIPT=""
REPORT=""
MARKER=""

#echo "Script name : $SCRIPT"
#echo "Parent directory: $PARENTPATH"
#echo "Script location: $SCRIPT_PATH"
#echo "Testbed file location: $TESTBED_PATH"
#echo "Tmp file location: $TMPFILEPATH"

#if [ $# -lt 2 ]; then 
#	Usage
#	exit 1
#fi	

while getopts t:s:r:l:f:m: flag
do
	case "${flag}" in
		t) TESTBED=${OPTARG};;
		s) SCRIPT=${OPTARG};;
		r) REPORT=${OPTARG};;
		#l) LIST="${OPTARG}";;
		f) TEMPFILE="${OPTARG}";;
		m) MARKER=${OPTARG};;
		*) Usage;
			exit 1;;
	esac
done

exec 1> >(tee -a "./log/ONL_${TESTBED}_$(date +"%m_%d_%Y_%T").txt")

# Check whether all mandatory command-line arguments are provided as input. If not, return error and print help text.

ValidateCommandlineInput

CheckTestbedFilePresence $TESTBED_PATH $TESTBED

#Parse testbed file and create a tmp file contains all test variable under: ./../tmp folder

DEBUG='-vv --tb=no'
CONSOLE_LOG='-s'
FILENAME=${TEMPFILE}
EXTRA_CLI_ARGUMENT="--filename ${FILENAME} --testbed ${TESTBED}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_testbed_file_parser.py ${EXTRA_CLI_ARGUMENT} 


# Gather system information from all DUT's and store it in the tmp file.

EXTRA_CLI_ARGUMENT_LIST="--filename ${FILENAME}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_collectSystemData.py ${EXTRA_CLI_ARGUMENT_LIST}

#Testcase execution start
echo ${REPORT}
echo "======================== Testcase exection starts ==================================="

if [[ ! -z ${SCRIPT} ]]; then
	if [[ ! -z ${REPORT} ]]; then
		for testcase in $TESTCASES
		do
			pytest ${DEBUG} ${CONSOLE_LOG} ./../Scripts/${testcase} --alluredir=${REPORT}
		done
	else
		for testcase in $TESTCASES
                do
                        pytest ${DEBUG} ${CONSOLE_LOG} ./../Scripts/${testcase} 
                done
	fi
fi

if [[ ! -z ${MARKER} ]]; then
	if [[ ! -z ${REPORT} ]]; then
		pytest ${DEBUG} ${CONSOLE_LOG} -m ${MARKER} ./../Scripts/ ${EXTRA_CLI_ARGUMENT_LIST} --alluredir=${REPORT} --html=./log/ONL_${TESTBED}_$(date +"%m_%d_%Y_%T").html
	else
		pytest ${DEBUG} ${CONSOLE_LOG} -m ${MARKER} ./../Scripts/ ${EXTRA_CLI_ARGUMENT_LIST}
	fi
fi

echo "======================== Testcase exection end  ====================================="

#Testcase exection end
