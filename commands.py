import subprocess
import os
import sys
import shlex

def git_init():
	os.chdir(os.getcwd())
	subprocess.call('git init')

def git_create_readme(msg="New project"):
	readme = 'echo "#{0}" >> README.md '.format(msg)
	subprocess.call(readme, shell=True)

def git_add():
	subprocess.call('git add --all')

def git_commit(msg="New commit"):
	subprocess.call('git commit -m "{0}"'.format(msg))	

def git_remote(url="git@github.com:JersonMartinez/gitpy.git"):
	subprocess.call('git remote add origin {0}'.format(url))

def git_push():
	subprocess.call('git push -u origin master')

if __name__ == '__main__':
	git_init()
	git_create_readme(msg="Gitpy")
	git_add()
	git_commit()
	git_remote()
	git_push()