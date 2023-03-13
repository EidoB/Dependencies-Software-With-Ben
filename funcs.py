import os
import socket
import subprocess
import datetime
import winreg
from tkinter import messagebox

ERRORS = []


logfile = open('benandeido.log', 'w+')
clientaddress = open('clientipaddresses.txt', 'r')


def checkpythonpath():

    m_path = os.environ['Path']
    all_envvar = os.environ
    if ('PYTHONHOME' and 'PYTHONPATH' in all_envvar) and ('c:\python' or 'C:\Python' in m_path) and (
            'c:\python\Scripts' or 'C:\Python\Scripts' in m_path):
        if ("c:\python" or "c:\Python" in os.environ['PYTHONHOME']) and (
                "c:\python" or "c:\Python" in os.environ['PYTHONPATH']):
            write_to_log('INFO Python path configured properly')
        else:
            write_to_log('ERROR one of Python path not configured')
            ERRORS.append("error")
    else:
        write_to_log('ERROR one of Python path not configured')
        ERRORS.append("error")


def checkbmcipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_bmc_ip_list = "10.11.18.1 10.11.28.1 10.11.38.1 10.11.48.1 10.11.218.1"
    if ip_address in battery_bmc_ip_list:
        write_to_log('INFO your BMC IP address is set properly')
    else:
        write_to_log('ERROR your BMC address is not set properly')
        ERRORS.append("error")


def checkdbipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_db_ip_list = "10.11.18.3 10.11.28.3 10.11.38.3 10.11.48.3 10.11.218.3"
    if ip_address in battery_db_ip_list:
        write_to_log('INFO Your DB IP address is set properly')
    else:
        write_to_log('ERROR your DB address is not set properly')
        ERRORS.append("error")

def checkicsipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_ics_ip_list = "10.12.18.13 10.12.28.13 10.12.38.13 10.12.48.13"
    if ip_address in battery_ics_ip_list:
        write_to_log('INFO Your ICS IP address is set properly')
    else:
        write_to_log('ERROR your ICS IP address is not set properly')
        ERRORS.append("error")

def checkclientipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # print(clientaddress.read())
    for line in clientaddress:
        line = str(line)
        if ip_address in line:
            write_to_log('INFO your client IP address is set properly')
            break
    else:
        write_to_log('ERROR your client IP address is not set properly')
        ERRORS.append("error")


def checkbmcsoftwares():
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(data)
    softwares = ""
    try:
        for i in range(len(a)):
            softwares = softwares + a.split("\\r\\r\\n")[6:][i]
    except IndexError as e:
        pass
    if ' Microsoft Visual C++ 2010  x86 Redistributable' in softwares:
        write_to_log('INFO Visual C++ 2010  x86 Redistributable is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2010  x86 Redistributable is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2008 Redistributable - x64' in softwares:
        write_to_log('INFO Visual C++ 2008  Redistributable x64 is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2008 Redistributable x64 is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2008 Redistributable - x86' in softwares:
        write_to_log('INFO Visual C++ 2008  Redistributable x86 is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2008 Redistributable x86 is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X64 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Minimum Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X64 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Additional Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X86 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Minimum Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X86 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Additional Runtime is missing')
        ERRORS.append("error")


def checkclientsoftwares():
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(data)
    softwares = ""
    try:
        for i in range(len(a)):
            softwares = softwares + a.split("\\r\\r\\n")[6:][i]
    except IndexError:
        pass
    if 'Microsoft Visual C++ 2019 X64 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Minimum Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X64 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Additional Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X86 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Minimum Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X86 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Additional Runtime is missing')
        ERRORS.append("error")


def checkicssoftwares():
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(data)
    softwares = ""
    try:
        for i in range(len(a)):
            softwares = softwares + a.split("\\r\\r\\n")[6:][i]
    except IndexError as e:
        pass
    if ' Microsoft Visual C++ 2010  x86 Redistributable' in softwares:
        write_to_log('INFO Visual C++ 2010  x86 Redistributable is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2010  x86 Redistributable is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X64 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Minimum Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X64 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Additional Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X86 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Minimum Runtime is missing')
        ERRORS.append("error")
    if 'Microsoft Visual C++ 2019 X86 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Additional Runtime is missing')
        ERRORS.append("error")


def checkdbsoftwares():
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(data)
    softwares = ""
    try:
        for i in range(len(a)):
            softwares = softwares + a.split("\\r\\r\\n")[6:][i]
    except IndexError as e:
        pass
    if 'SQL Server 2017' in softwares:
        write_to_log('INFO SQL Server 2017 is existing')
    else:
        write_to_log('ERROR SQL Server 2017 is missing')
    if ' Microsoft Visual C++ 2010  x86 Redistributable' in softwares:
        write_to_log('INFO Visual C++ 2010  x86 Redistributable is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2010  x86 Redistributable is missing')
        ERRORS.append("error")


def write_to_log(log_data):
    now = datetime.datetime.now()

    with open('benandeido.log', 'a') as file:
        # Write the date and time to the file
        file.write(f"{now} - {log_data}\n")


def python_path_exe_checker():
    filename = "python.exe"
    directory = 'C:/Python'
    if os.path.exists(os.path.join(directory, filename)):
        write_to_log(f"INFO The file 'python' exists in C:\python")
    else:
        write_to_log(f"ERROR The file 'python' does not exist in C:\python")
        ERRORS.append("error")


def check_dotnet_framework_35():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\NET Framework Setup\NDP\v3.5")
        value = winreg.QueryValueEx(key, "Install")
        if value[0] == 1:
            write_to_log("INFO '.NET Framework 3.5' is installed")
    except FileNotFoundError:
        write_to_log("ERROR '.NET Framework 3.5' is not installed")
        ERRORS.append("error")


def bmc_server_log_name():
    with open('benandeido.log', 'a') as file:
        file.write(f"Details for BMC Server:\n")


def db_server_log_name():
    with open('benandeido.log', 'a') as file:
        file.write(f"Details for DB Server:\n")


def ics_server_log_name():
    with open('benandeido.log', 'a') as file:
        file.write(f"Details for ICS Server:\n")


def client_log_name():
    with open('benandeido.log', 'a') as file:
        file.write(f"Details for Client:\n")


def map_path_checker():
    directory = 'C:/Maps'
    if os.path.exists(os.path.join(directory)):
        write_to_log(f"INFO The folder Maps exists in C Drive")
    else:
        write_to_log(f"ERROR The The folder Maps does not exist in C Drive")
        ERRORS.append("error")


client_dict = [
    {
        "programName": "ArcGIS Engine Runtime",
        "programVersion": "9.3.3500",
    },
    {
        "programName": "Infognition ScreenPressor v2.1",
        "programVersion": "",
    }
]

NTP_dict = [
    {
        "programName": "Network Time Protocol",
        "programVersion": "4.2.8p15",
    },
    {
        "programName": "NTP Time Server Monitor 1.04",
        "programVersion": "0.9g",
    }
]

winpcap_dict = [
    {
        "programName": "WinPcap 4.1.3",
        "programVersion": "",
    },
]


def find_softwares_winreg():
    dictionary_of_programs = []
    key_path = r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    for i in range(winreg.QueryInfoKey(key)[0]):
        subkey_name = winreg.EnumKey(key, i)
        subkey_path = os.path.join(key_path, subkey_name)
        try:
            subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
            display_name, _ = winreg.QueryValueEx(subkey, "DisplayName")
            display_version, _ = winreg.QueryValueEx(subkey, "DisplayVersion")
            dictionary_of_programs.extend(([{"programName": display_name, "programVersion": display_version}]))
            # print(dictionary_of_programs)
            
        except WindowsError:
            pass
    return dictionary_of_programs

def check_if_program_exist(component_dict):
    dictionary_of_programs = find_softwares_winreg()
    for program in component_dict:
        program_name = program["programName"] 
        program_version = program["programVersion"] 
        program_found = False
        for program_check in dictionary_of_programs:
            if program_name in program_check["programName"]:
                program_found = True
                current_program_version = program_check["programVersion"]
                if program_version in current_program_version:
                    write_to_log(f"INFO The program '{program_name}' is installed")
                else:
                    write_to_log(
                        f"ERROR The program '{program_name}' is installed on the component but not with the correct version. An existing version: {current_program_version}. Desired version: {program_version}")
        if not program_found:
            write_to_log(f"ERROR The program '{program_name}' is not exist in the component")
            ERRORS.append("error")


def waiting_message():
    messagebox.showinfo(title="FBE Dependency Checker", message="Please wait until the check is completed...")


def done_message(component_name):
    messagebox.showinfo(title="Done", message="the dependencies check is over")
    with open(file="benandeido.log", mode="r") as logs:
        error = logs.read()
        errors = error.count("ERROR")
        if errors == 0:
            messagebox.showinfo(title="good news!", message=f"all the programs is fully installed on thr {component_name}, well done!")
        else:
            messagebox.showwarning(title=component_name, message=f"The program founds {len(ERRORS)} errors. Please check the log file in the program working directory - 'benandeido.log'")


def bmc_checker():
    waiting_message()
    bmc_server_log_name()
    checkbmcipaddress()
    checkpythonpath()
    python_path_exe_checker()
    check_dotnet_framework_35()
    checkbmcsoftwares()
    map_path_checker()
    check_if_program_exist(NTP_dict)
    done_message("BMC Server")
    ERRORS.clear()


def db_checker():
    waiting_message()
    db_server_log_name()
    checkdbipaddress()
    check_dotnet_framework_35()
    checkdbsoftwares()
    check_if_program_exist(winpcap_dict)
    check_if_program_exist(NTP_dict)
    done_message("DB Server")
    ERRORS.clear()

def ics_checker():
    waiting_message()
    ics_server_log_name()
    checkicsipaddress()
    check_dotnet_framework_35()
    checkicssoftwares()
    check_if_program_exist(NTP_dict)
    done_message('ICS Server')
    ERRORS.clear()


def client_checker():
    waiting_message()
    client_log_name()
    checkclientipaddress()
    check_dotnet_framework_35()
    checkclientsoftwares()
    check_if_program_exist(NTP_dict)
    check_if_program_exist(client_dict)
    done_message('Client')
    ERRORS.clear()






# checkbmcipaddress()
# checkpythonpath()
# checkdbipaddress()
# checkclientipaddress()
# write_to_log('zibi zibi zib')
# python_path_exe_checker()
# check_dotnet_framework_35()
# bmc_server_log_name()
# map_path_checker()
# checkbmcsoftwares()
# checkdbsoftwares()
# checkclientsoftwares()
#to check the ICS network IP address for BMC and DB
#Optional - to check if routes existed 

