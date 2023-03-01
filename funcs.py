import os
import json

#find pathes

m_path = os.environ['Path']
all_envvar = os.environ
if ('PYTHONHOME' and 'PYTHONPATH' in all_envvar) and ('c:\python' or 'C:\Python' in m_path ) and ('c:\python\Scripts' or 'C:\Python\Scripts' in m_path )  :
    if ("c:\python" or "c:\Python" in os.environ['PYTHONHOME'] )and ("c:\python" or "c:\Python" in os.environ['PYTHONPATH'] ):
        pass
    else:
        print('Python is missing from that system')
else:
    print('Python is missing from that system')


