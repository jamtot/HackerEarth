import subprocess
import sys
import pexpect

if __name__ == "__main__":
    child = pexpect.spawn('python lucky.py')
    with open("input2.txt") as inp:
        inputs = inp.read().splitlines()
        for line in inputs:
            child.expect('> ')
            child.sendline(line)
            child.logfile_read = sys.stdout
