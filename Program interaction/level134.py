import glob
import subprocess

# Get the list of executable files matching the pattern
path = glob.glob('/challenge/em*')[0]

# Open the output file
with open('output.txt', 'w') as output_file:
        # Start the cat process for stdout
        cat_stdout = subprocess.Popen(['cat'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        
        # Start the cat process for stdin
        cat_stdin = subprocess.Popen(['cat'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        
        # Run the binary executable with cat processes connected to stdin and stdout
        process = subprocess.Popen([path], stdin=cat_stdin.stdout, stdout=cat_stdout.stdin, stderr=subprocess.PIPE, text=True)
        
        # Read the output line by line from the cat_stdout
        while True:
            line = cat_stdout.stdout.readline()
            if not line:
                break
            print(line, end='')  # Print the line

            # Find the substring 'for: '
            chal = line.find('for: ')
            if chal > 0:
                # Evaluate the expression after 'for: ' and write to the process input
                result = str(eval(line[chal + 4:].strip())) + '\n'
                cat_stdin.stdin.write(result)
                cat_stdin.stdin.flush()
                output_file.write(result)
        
        # Ensure the process has finished
        process.wait()
        cat_stdout.stdout.close()
        cat_stdin.stdin.close()
