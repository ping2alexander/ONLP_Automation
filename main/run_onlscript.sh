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
	echo -e "\e[1;37m" ;# Default font color:White
							  
}

CheckTestbedFilePresence ()
{
	echo " ---------------------------------------------------------------------------------------------------- "
	echo "            Check if testbed file exist            "
	echo " ---------------------------------------------------------------------------------------------------- "

	echo "Check if testbed file is present in the specific location"
	echo "Tesbed file location: $1"
	echo "Testbed filename: $2"
	
	if [ ! -f "$1/$2" ]
	then
		echo -e "\e[1;31mError:Specified testbed file is not present in the location:  $1"
		echo -e "\e[1;37m" ;# Default font color:White
		exit 1;
	else
		echo -e "\e[1;32mTestbed file exist in the location"
		echo -e "\e[1;37m" ;# Default font color:White
	fi
}


ValidateCommandlineInput ()
{
	if [[ -z ${TESTBED} ]]; then 
		echo -e "\e[1;31mError: Mandatory commandline arguments are missing - please check usage information"
		echo -e "\e[1;37m" ;# Default font color:White
		Usage
		exit 1;
	fi
	if [[ -z ${TEMPFILE} ]]; then
                echo -e "\e[1;31mError: Mandatory commandline arguments are missing - please check usage information"
		echo -e "\e[1;37m" ;# Default font color:White
                Usage
                exit 1;
        fi
	if [[ -z ${MARKER} ]]; then
		MARKER='All'
		echo -e "\e[1;32mTestcase groupname(pytest marker) is not given as a input argument. Choosing default argument \"All\""
		echo -e "\e[1;37m"
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
	       echo -e "\e[1;32mIndividual script mode is selected.!!!"
	       echo -e "\e[1;37m" ;# Default font color:White
	fi
	#elif [[ ! -z ${LIST} ]] ; then
        #        TESTCASES=${LIST}
	#else
	#	TESTCASES=${CommonTestcase_array[*]}
	#fi
	return 1
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

#exec 1> >(tee -a "./log/ONL_${TESTBED}_$(date +"%m_%d_%Y_%T").txt")

echo ""

echo " ---------------------------------------------------------------------------------------------------- "
echo "|                                                                                                    |"
echo "|                     ONL(Open Network Linux) Automation                                             |"
echo "|                                                                                                    |"
echo " ---------------------------------------------------------------------------------------------------- "

# Check whether all mandatory command-line arguments are provided as input. If not, return error and print help text.


echo -e "\nStep:1 - Validating the commandline arguments passed to the main shell script \n"

ValidateCommandlineInput

echo -e "\e[1;33mUser Input Arguments"
echo -e "\e[1;33m===================="
echo -e "\e[1;33mTestbed Filename  : ${TESTBED}"
echo -e "\e[1;33mTemp Filename     : ${TEMPFILE}"
echo -e "\e[1;33mTestcase groupname: ${MARKER}"
echo -e "\e[1;37m" ; # Default font color

CheckTestbedFilePresence $TESTBED_PATH $TESTBED

#Parse testbed file and create a tmp file contains all test variable under: ./../tmp folder

DEBUG='-v'
CONSOLE_LOG='-s'
FILENAME=${TEMPFILE}
EXTRA_CLI_ARGUMENT="--filename ${FILENAME} --testbed ${TESTBED}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_testbed_file_parser.py ${EXTRA_CLI_ARGUMENT} 

echo -e "\e[1;33m-------------------------------------------------------------------"
echo -e "\e[1;33m                     Topology Diagram                              "
echo -e "\e[1;33m-------------------------------------------------------------------"

python3 ./topology.py -f ${TESTBED}

echo -e "\e[1;37m" ;# Default font color:White

# Gather system information from all DUT's and store it in the tmp file.

EXTRA_CLI_ARGUMENT_LIST="--filename ${FILENAME}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_collectSystemData.py ${EXTRA_CLI_ARGUMENT_LIST}

#Testcase execution start

echo -e "\e[1;33m------------------------------------------------------------------------------------------"
echo -e "\e[1;33m                                                                                          |"
echo -e "\e[1;33m                                   TESTCASE EXECUTION START                               |"
echo -e "\e[1;33m                                                                                          |"
echo -e "\e[1;33m------------------------------------------------------------------------------------------"
echo -e "\e[1;37m" ;# Default font color:White

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

echo -e "\e[1;33m======================== TESTCASE EXECUTION END  ====================================="

#Testcase exection end
