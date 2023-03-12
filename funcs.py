import os
import socket
import subprocess
import datetime
import winreg

logfile = open('benandeido.log','w+')
clientaddress = open('clientipaddresses.txt','r')

def checkpythonpath():
    m_path = os.environ['Path']
    all_envvar = os.environ
    if ('PYTHONHOME' and 'PYTHONPATH' in all_envvar) and ('c:\python' or 'C:\Python' in m_path ) and ('c:\python\Scripts' or 'C:\Python\Scripts' in m_path )  :
        if ("c:\python" or "c:\Python" in os.environ['PYTHONHOME'] )and ("c:\python" or "c:\Python" in os.environ['PYTHONPATH'] ):
            write_to_log('INFO Python path configured properly')
        else:
            write_to_log('ERROR one of Python path not configured')
    else:
        write_to_log('ERROR one of Python path not configured')

def checkbmcipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_bmc_ip_list = "10.11.18.1 10.11.28.1 10.11.38.1 10.11.48.1 10.11.218.1"
    if ip_address in battery_bmc_ip_list:
        write_to_log('INFO your BMC IP address is set properly')
    else:
        write_to_log('ERROR your BMC address is not set properly')

def checkdbipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_db_ip_list = "10.11.18.3 10.11.28.3 10.11.38.3 10.11.48.3 10.11.218.3"
    if ip_address in battery_db_ip_list:
        write_to_log('INFO Your DB IP address is set properly')
    else:
        write_to_log('ERROR your DB address is not set properly')

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
    if 'Microsoft Visual C++ 2008 Redistributable - x64' in softwares:
        write_to_log('INFO Visual C++ 2008  Redistributable x64 is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2008 Redistributable x64 is missing')
    if 'Microsoft Visual C++ 2008 Redistributable - x86' in softwares:
        write_to_log('INFO Visual C++ 2008  Redistributable x86 is existing')
    else:
        write_to_log('ERROR Microsoft Visual C++ 2008 Redistributable x86 is missing')
    if 'Microsoft Visual C++ 2019 X64 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Minimum Runtime is existing')
    else: 
        write_to_log('ERROR Visual C++ 2019 X64 Minimum Runtime is missing')
    if 'Microsoft Visual C++ 2019 X64 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Additional Runtime is missing')
    if 'Microsoft Visual C++ 2019 X86 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Minimum Runtime is missing')
    if 'Microsoft Visual C++ 2019 X86 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Additional Runtime is missing')

def checkclientsoftwares():
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(data)
    softwares = ""
    try:
        for i in range(len(a)):
            softwares = softwares + a.split("\\r\\r\\n")[6:][i]
    except IndexError as e:
        pass
    if 'Microsoft Visual C++ 2019 X64 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Minimum Runtime is existing')
    else: 
        write_to_log('ERROR Visual C++ 2019 X64 Minimum Runtime is missing')
    if 'Microsoft Visual C++ 2019 X64 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Additional Runtime is missing')
    if 'Microsoft Visual C++ 2019 X86 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Minimum Runtime is missing')
    if 'Microsoft Visual C++ 2019 X86 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Additional Runtime is missing')

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
    if 'Microsoft Visual C++ 2019 X64 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Minimum Runtime is existing')
    else: 
        write_to_log('ERROR Visual C++ 2019 X64 Minimum Runtime is missing')
    if 'Microsoft Visual C++ 2019 X64 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X64 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X64 Additional Runtime is missing')
    if 'Microsoft Visual C++ 2019 X86 Minimum Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Minimum Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Minimum Runtime is missing')
    if 'Microsoft Visual C++ 2019 X86 Additional Runtime' in softwares:
        write_to_log('INFO Visual C++ 2019 X86 Additional Runtime is existing')
    else:
        write_to_log('ERROR Visual C++ 2019 X86 Additional Runtime is missing')

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

def check_dotnet_framework_35():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\NET Framework Setup\NDP\v3.5")
        value = winreg.QueryValueEx(key, "Install")
        if value[0] == 1:
            write_to_log("INFO '.NET Framework 3.5' is installed")
    except FileNotFoundError:
        write_to_log("ERROR '.NET Framework 3.5' is not installed")

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


# checkbmcipaddress()
# checkpythonpath()
# checkdbipaddress()
# checkclientipaddress()
# checkbmcsoftwares()
# write_to_log('zibi zibi zib')
# python_path_exe_checker()
# check_dotnet_framework_35()
# bmc_server_log_name()
# map_path_checker()
# checkbmcsoftwares()
# checkdbsoftwares()
# checkclientsoftwares()
#create check winpcap, ESRI ArcGIS, Screen Pressor, NTP meinberg, function that run all the functions per host