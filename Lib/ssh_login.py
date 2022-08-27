import pytest
import paramiko
import time

class Login():
    def __init__(self, ipaddress, Username, Passwd):
        self.ipaddress = ipaddress
        self.username = Username
        self.password = Passwd
        self.client = None
        self.__deviceConnect()

    def __deviceConnect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password, look_for_keys=False, allow_agent=False)
        except AuthenticationException as err:
            print("Device authentication failed, please check username and password")
    def Logout(self):
        self.client.close()
    
    def SendACommand(self, command):
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
        except:
            print("Error: Session is closed or not open yet. please connect to the DUT")
            return -1;

        status = stdout.channel.recv_exit_status()

        if status is 0:
            res = stdout.read().decode("utf8")
            return res;
        elif status is -1:
            print("Error: CLI Command is not yet executed")
            print(stderr.read().decode("utf8"));
            exit;
        else:
            print(status)
            print("CLI Error: {}".format(stderr.read().decode("utf8")))


