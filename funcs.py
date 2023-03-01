import os
import socket

logfile = open('benandeido.log','w+')
clientaddress = open('clientipaddresses.txt','r')

def checkpythonpath():
    m_path = os.environ['Path']
    all_envvar = os.environ
    if ('PYTHONHOME' and 'PYTHONPATH' in all_envvar) and ('c:\python' or 'C:\Python' in m_path ) and ('c:\python\Scripts' or 'C:\Python\Scripts' in m_path )  :
        if ("c:\python" or "c:\Python" in os.environ['PYTHONHOME'] )and ("c:\python" or "c:\Python" in os.environ['PYTHONPATH'] ):
            pass
        else:
            print('Python is missing from that system')
            logfile.write('Python is missing or path not configured \n')
    else:
        print('Python is missing from that system')
        logfile.write('Python is missing or path not configured \n')

def checkbmcipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_bmc_ip_list = "10.11.18.1 10.11.28.1 10.11.38.1 10.11.48.1 10.11.218.1"
    if ip_address in battery_bmc_ip_list:
        pass
    else:
        print('your bmc address not set')
        logfile.write('your bmc address is not set properly\n')

def checkdbipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    battery_db_ip_list = "10.11.18.3 10.11.28.3 10.11.38.3 10.11.48.3 10.11.218.3"
    if ip_address in battery_db_ip_list:
        pass
    else:
        print('your db address not set')
        logfile.write('your db address is not set properly\n')

def checkclientipaddress():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # print(clientaddress.read())
    for line in clientaddress:
        line = str(line)
        if ip_address in line:
            break
    else:
        print('your client address not set')
        logfile.write('your client address is not set properly\n')

# checkbmcipaddress()
# checkpythonpath()
# checkdbipaddress()
# checkclientipaddress()