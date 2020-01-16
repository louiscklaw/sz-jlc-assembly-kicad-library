#!/usr/bin/env python3

import os, sys

submodule_path = []
cwd = os.path.dirname(os.path.abspath(__file__))
gitmodules_path = os.path.sep.join([cwd,'..','.gitmodules'])

with open(gitmodules_path, 'r') as fi:
  try:
    for line in fi.readlines():
      if line.find('path = ') > -1:
        submodule_path.append(line.strip().split('path = ')[1])

    for command_path in submodule_path:
      print('running shallow command for path {}'.format(command_path))
      os.system('git config -f .gitmodules submodule.{}.shallow true'.format(command_path))

    sys.exit(0)

  except Exception as e:
    print('error found during settings shallow submodules ...')
    sys.exit(1)
