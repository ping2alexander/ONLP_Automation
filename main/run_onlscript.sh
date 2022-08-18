#!/bin/bash


Usage ()
{
	echo -e "\e[1;32mUsage: $0 [options]"
	echo -e "\e[1;32mOption with (*) must be provided"
	echo -e "\e[1;32m-t <testbed filename>		- Specify testbed filename(*)"
	echo -e "\e[1;32m-s <individul script name>	- Specify test cases to execute."
	#echo -e "\e[1;32m-l <list of testcases>		- Specify the list of testcases to execute. Example: Common or Platform_<XXXXXX>. Default: Execute all testcases from Common list"
	echo -e "\e[1;32m-m <pytestmarker>		- Specity the testcase groupname"
	echo -e "\e[1;33m				  Example: -m \"All\" or -m \"Sanity\"" 
	echo -e "\e[1;33m					   -m \"Belgite\""
	echo -e "\e[1;37m" ;# Default font color:White
							  
}

CheckTestbedFilePresence ()
{
	echo "Check if testbed file is present in the specific location"
	echo "Tesbed file location: $1"
	echo "Testbed filename: $2"
	
	if [ ! -f "$1/$2" ]
	then
		echo -e "\e[1;31mError: Specified testbed file is not present in the location:  $1"
		echo -e "\e[1;37m" ;# Default font color:White
		exit 1;
	else
		echo -e "\e[1;32mSuccess: Testbed file is present in the configuration directory !!!"
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

PARENTPATH=`echo $MAINPATH | awk '{ print substr( $0, 2 ) }'`
SCRIPT_PATH=`echo $SCRIPT_PATH | awk '{ print substr( $0, 2 ) }'`
TESTBED_PATH=`echo $TESTBED_PATH | awk '{ print substr( $0, 2 ) }'`
TMPFILEPATH=`echo $TMPFILEPATH | awk '{ print substr( $0, 2 ) }'`
PYTHONPATH=`echo $PYTHONPATH | awk '{ print substr( $0, 2 ) }'`
MAINPATH=`echo $FULL_PATH | awk '{ print substr( $0, 2 ) }'`
Reportdir='Reports'
Resultdir='Results'
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
		#f) TEMPFILE="${OPTARG}";;
		m) MARKER=${OPTARG};;
		*) Usage;
			exit 1;;
	esac
done

f=$(echo $TESTBED | tr ".yml" "\n")
TEMPFILE=${f[0]}
Log='log'

subdir=$(shuf -i 100000-1000000 -n 1)
echo $subdir

echo "Creating sub directory under Report and Result directory"

echo "Creating sub directory under Report and Result directory"

if [ ! -d "$subdir" ]
then
        echo "Directory doesn't exist. Creating now"
        mkdir ${PARENTPATH}/${Resultdir}/${subdir}
	mkdir ${PARENTPATH}/${Log}/${subdir}
        echo "Directory created successfully !!!"
else
        echo "Directory already exist"
fi

exec 1> >(tee -a "./log/${subdir}/log.txt")

echo ""

echo " ---------------------------------------------------------------------------------------------------- "
echo "|                                                                                                    |"
echo "|                     ONL(Open Network Linux) Automation                                             |"
echo "|                                                                                                    |"
echo " ---------------------------------------------------------------------------------------------------- "

# Check whether all mandatory command-line arguments are provided as input. If not, return error and print help text.


echo -e "*****************************************************************************************"
echo -e "Step:1 - Validating the commandline arguments passed to the main shell script"
echo -e "*****************************************************************************************"

ValidateCommandlineInput

echo -e "\e[1;34mCommandline arguments and environment variable declared"
echo -e "\e[1;34m*******************************************************"
echo -e "\e[1;34m|\tTestbed Filename       : ${TESTBED}"
echo -e "\e[1;34m|\tTemp Filename          : ${TEMPFILE}"
echo -e "\e[1;34m|\tTestcase groupname     : ${MARKER}"
echo -e "\e[1;34m|\tScript location        : ${SCRIPT_PATH}"
echo -e "\e[1;34m|\tTestbed file location  : ${TESTBED_PATH}"
echo -e "\e[1;34m|\tLibrary file location  : ${PYTHONPATH}"
echo -e "\e[1;37m" ; # Default font color

echo -e "*****************************************************************************************"
echo -e "Step:2 - Check testbed file existence"
echo -e "*****************************************************************************************"


CheckTestbedFilePresence $TESTBED_PATH $TESTBED

echo -e "\e[1;36m******************************************************************************************"
echo -e "\e[1;36mStep:3 Parse testbed file and create a tmp file contains all test variable under: ./../tmp folder"
echo -e "\e[1;36m******************************************************************************************"

DEBUG='-v'
CONSOLE_LOG='-s'
FILENAME=${TEMPFILE}
EXTRA_CLI_ARGUMENT="--filename ${FILENAME} --testbed ${TESTBED}"

pytest ${DEBUG} ${CONSOLE_LOG} ./test_testbed_file_parser.py ${EXTRA_CLI_ARGUMENT} 

echo -e "\e[1;35m******************************************************************************************"
echo -e "\e[1;35mStep: 5                   Topology Diagram                              "
echo -e "\e[1;35m******************************************************************************************"

python3 ./topology.py -f ${TESTBED}

echo -e "\e[1;37m" ;# Default font color:White

# Gather system information from all DUT's and store it in the tmp file.

EXTRA_CLI_ARGUMENT_LIST="--filename ${FILENAME}"

echo -e "\e[1;34m******************************************************************************************"
echo -e "\e[1;34mStep: 5                   DUTs PING test                              "
echo -e "\e[1;34m******************************************************************************************"


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
			pytest ${DEBUG} ./../Scripts/${testcase} --alluredir=${REPORT}
		done
	else
		for testcase in $TESTCASES
                do
                        pytest ${DEBUG} ./../Scripts/${testcase} 
                done
	fi
fi

if [[ ! -z ${MARKER} ]]; then
	pytest ${DEBUG} -m ${MARKER} ./../Scripts/ ${EXTRA_CLI_ARGUMENT_LIST} --alluredir=${PARENTPATH}/${Reportdir}/${subdir} --html=${PARENTPATH}/${Resultdir}/${subdir}/Result.html
fi

echo -e "\e[1;33m======================== TESTCASE EXECUTION END  ====================================="

#Testcase exection end

echo "Copying log and results to the FTP server" > /dev/null

HOST='172.24.77.188'
USER='admin'
PASSWD='admin'
Remotelocation='/'

ncftp ftp://${USER}:${PASSWD}@${HOST}/<<EOF  > /dev/null
mkdir ${subdir}
chmod 777 ${subdir}
cd ${subdir}
mkdir log
mkdir Results
chmod 777 log
chmod 777 Results
EOF

ncftpput -u $USER -p $PASSWD -R $HOST /${subdir}/log ./log/${subdir}/* > /dev/null 2>&1
ncftpput -u $USER -p $PASSWD -R $HOST /${subdir}/Results ./Results/${subdir}/* > /dev/null 2>&1

#Update index_var file with new regId 
python3 Index_add_new_element.py ${subdir} ${FILENAME} ${HOST} > /dev/null

# Update ONL web home page 
ansible-playbook index_task.yml > /dev/null

#python3 RegId_add_new_element.py ${subdir} ${FILENAME} > /dev/null

# Update ONL web home page 
#ansible-playbook RegId_task.yml > /dev/null

#mv regId.html ${subdir}.html > /dev/null

sudo cp -r ./Results/${subdir} /var/www/html/ > /dev/null
sudo cp -r ./log/${subdir} /var/www/html/ > /dev/null
#sudo cp -r ./${subdir}.html /var/www/html/ > /dev/null
sudo cp -r ./index.html /var/www/html/ > /dev/null
#Cleanup

rm a.yml > /dev/null
rm test.yml > /dev/null
rm index.html > /dev/null
#rm ${subdir}.html > /dev/null
