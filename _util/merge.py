#!/usr/bin/env python

# reference build https://travis-ci.org/louiscklaw/test_git_repo/builds/625335510
# https://docs.travis-ci.com/user/environment-variables/

import sys
import os, re, subprocess
import slack

from fabric.api import local, shell_env, lcd, run, settings

SLACK_TOKEN = os.environ['SLACK_TOKEN']

merge_direction = {
  '^test/(.+?)$': 'feature',
  '^feature' : 'develop',
  # 'develop': 'master'
}

TRAVIS_BRANCH = os.environ['TRAVIS_BRANCH']
TRAVIS_COMMIT = os.environ['TRAVIS_COMMIT']
TRAVIS_BUILD_NUMBER = os.environ['TRAVIS_BUILD_NUMBER']
GITHUB_REPO = os.environ['TRAVIS_REPO_SLUG']
GITHUB_TOKEN = os.environ['GITHUB_TOKEN']


PUSH_URI="https://{}@github.com/{}".format(GITHUB_TOKEN, GITHUB_REPO)

TEMP_DIR = local('mktemp -d', capture=True)
local('git clone "{}" "{}"'.format(PUSH_URI, TEMP_DIR))

def slack_message(message, channel):
  client = slack.WebClient(token=SLACK_TOKEN)
  response = client.chat_postMessage(
      channel=channel,
      text=message,
      username='TravisMergerBot',
      icon_url=':sob:'
      )

def run_command(command_body):
  command_result = local(command_body, capture=True)
  print(command_result)
  return command_result

def push_commit(uri_to_push):
    print('push commit')
    run_command("git push {} {}".format(uri_to_push, merge_to))

def merge_to_branch(commit_id, merge_to):
  with( shell_env( GIT_COMMITTER_EMAIL='travis@travis', GIT_COMMITTER_NAME='Travis CI' ) ):
    print('checkout {} branch'.format(merge_to))
    run_command('git checkout {}'.format(merge_to))

    print('Merging "{}"'.format(commit_id))
    result_to_check = run_command('git merge --ff-only "{}"'.format(commit_id))

    if result_to_check.failed:
      slack_message('error found during merging BUILD{} `{}` from `{}` to `{}`'.format(TRAVIS_BUILD_NUMBER, GITHUB_REPO, TRAVIS_BRANCH, merge_to), '#travis-build-result')
    else:
      slack_message('merging BUILD{} from {} `{}` to `{}` done'.format(TRAVIS_BUILD_NUMBER, GITHUB_REPO, TRAVIS_BRANCH, merge_to), '#travis-build-result')

print('starting merger')
merge_found = False
for merge_from, merge_to in merge_direction.items():
  m = re.match(merge_from, TRAVIS_BRANCH)
  if (m == None ) :
    # print('skipping merge for branch {}'.format(TRAVIS_BRANCH))
    # slack_message('skip merging for BUILD #{} `{}` from `{}` to `{}`'.format(TRAVIS_BUILD_NUMBER, GITHUB_REPO, TRAVIS_BRANCH, merge_to), '#travis-build-result')
    pass

  else:
    merge_found = True
    if len(m.groups()) == 1:
      sub_branch = m.group(1)
      merge_to = merge_to+'/'+sub_branch

      print(f'try to merge {merge_from} -> {merge_to}')

      with lcd(TEMP_DIR):
        merge_to_branch(TRAVIS_COMMIT, merge_to)
        push_commit(PUSH_URI)

    else:
      print(f'try to merge {merge_from} -> {merge_to}')

      with lcd(TEMP_DIR):
        merge_to_branch(TRAVIS_COMMIT, merge_to)
        push_commit(PUSH_URI)

if not merge_found:
  print('no merge direction for this branch')