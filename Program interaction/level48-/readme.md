# Level 48

$ ipython solve.py | cat

# Level 49

$ ipython
In [1]: import subprocess
   ...: 
   ...: # Command to execute
   ...: command1 = ["/challenge/embryoio_level49"]
   ...: command2 = ["grep","pwn"]
   ...: 
   ...: # Execute the first command and capture its stdout
   ...: process1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
   ...: 
   ...: # Execute the second command and pass the stdout of the first command as input
   ...: process2 = subprocess.Popen(command2, stdin=process1.stdout)
   ...: 
   ...: #r , o = process2.communicate()
   ...: 

# Level 50

$ ipython

In [4]: import subprocess
   ...: 
   ...: # Command to execute
   ...: command1 = ["/challenge/embryoio_level50"]
   ...: command2 = ["sed","/pwn/p"]
   ...: 
   ...: # Execute the first command and capture its stdout
   ...: process1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
   ...: 
   ...: # Execute the second command and pass the stdout of the first command as input
   ...: process2 = subprocess.Popen(command2, stdin=process1.stdout)

# Level 51

In [2]: import subprocess
   ...: 
   ...: # Command to execute
   ...: command1 = ["/challenge/embryoio_level51"]
   ...: command2 = ["rev"]
   ...: command3 = command2
   ...: 
   ...: # Execute the first command and capture its stdout
   ...: process1 = subprocess.Popen(command1, stdout=subprocess.PIPE)
   ...: 
   ...: # Execute the second command and pass the stdout of the first command as input
   ...: process2 = subprocess.Popen(command2, stdin=process1.stdout,stdout = subprocess.PIPE)
   ...: 
   ...: #r , o = process2.communicate()
   ...: process3 =  subprocess.Popen(command3, stdin=process2.stdout)

# Level 52

In [2]: import subprocess
   ...: 
   ...: # Command to execute
   ...: command1 = ["/challenge/embryoio_level52"]
   ...: command2 = ["cat"]
   ...: 
   ...: # Execute the first command and capture its stdout
   ...: process2 = subprocess.Popen(command2, stdout=subprocess.PIPE)
   ...: 
   ...: # Execute the second command and pass the stdout of the first command as input
   ...: process1 = subprocess.Popen(command1, stdin=process2.stdout)
   ...: 
   ...: r , o = process2.communicate()

# Level 53

In [1]: import subprocess
   ...: 
   ...: # Command to execute
   ...: command1 = ["/challenge/embryoio_level53"]
   ...: command2 = ["rev"]
   ...: 
   ...: # Execute the first command and capture its stdout
   ...: process2 = subprocess.Popen(command2, stdout=subprocess.PIPE)
   ...: 
   ...: # Execute the second command and pass the stdout of the first command as input
   ...: process1 = subprocess.Popen(command1, stdin=process2.stdout)
   ...: 
   ...: r , o = process2.communicate()
   (dont forget to press ctrl+D after enter the input )
