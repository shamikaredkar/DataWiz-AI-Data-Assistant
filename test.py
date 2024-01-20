import os

apikey = os.getenv('OPENAI_API_KEY')
print(f'API Key: {apikey}')

import sys

module_name = 'PythonREPLTool'

# Check each directory in sys.path
for directory in sys.path:
    module_path = os.path.join(directory, module_name + '.py')
    
    # Check if the module file exists in the directory
    if os.path.isfile(module_path):
        print(f"Module '{module_name}' is located at: {module_path}")
        break
else:
    print(f"Module '{module_name}' not found.")