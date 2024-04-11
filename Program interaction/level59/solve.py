import subprocess

# Command to execute
command1 = ["/challenge/embryoio_level59"]
command2 = ["rev"]

# Execute the first command and capture its stdout
process1 = subprocess.Popen(command2, stdout=subprocess.PIPE)

# Execute the second command and pass the stdout of the first command as input
process2 = subprocess.Popen(command1, stdin=process1.stdout)

r , o = process2.communicate()


