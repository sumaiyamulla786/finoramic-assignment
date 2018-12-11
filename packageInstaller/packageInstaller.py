import subprocess
import os
import json

fnull = open(os.devnull, 'w')
packages = open('package.json', 'r')

#loading json file in a dictionary
install_packages = json.load(packages)
dependencies = install_packages['dependencies']
failed = False

# iterating over all the dependencies
for key, value in dependencies.items():
    package = key + '==' + value
    try:
      # install one dependency at a time
      subprocess.check_call(['pip', 'install', '-qqq', package], stdout=fnull, stderr=fnull)
      # using fnull to supress all levels of logging
    except subprocess.CalledProcessError:
      #handling failed packages and appending them for display later, continue with the installation of others
      failed = True
      print("Failed ", key)

# cleaning up descriptors
fnull.close()
packages.close()

# checking for successs
if(not failed):
  print('SUCCESS')