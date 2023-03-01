import os
import json

#find pathes
m_path = os.environ['Path']
all_envvar = os.environ
if ('PYTHONHOME' and 'PYTHONPATH' in all_envvar) and ('c:\python' and 'C:\python\scripts' in m_path )   :
    if os.environ['PYTHONHOME']:
        print(True)
else:
    print ('python is missing')

# m_pythonhome = os.environ['PYTHONHOME']
# m_pythonpath = os.environ['PYTHONPATH']

# print(m_path)



#query if path exists
# if "Python" or 'python' in m_path:
#     print ('nope\nnope')
# else:
#     print("no Python installed")
