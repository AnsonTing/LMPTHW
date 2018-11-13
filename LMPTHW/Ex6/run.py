from subprocess import Popen, PIPE

p = Popen(['python', 'test.py'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
stdout, stderr = p.communicate(input='a\n')
print stdout
print stderr
