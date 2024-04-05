#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int pwncollege() {
    pid_t pid = fork(); // Create a child process

    if (pid == -1) {
        // Fork failed
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Child process
FILE *inputFile = fopen("/tmp/jhaawx", "r");
    if (inputFile == NULL) {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    // Redirect stdin to the input file
    if (dup2(fileno(inputFile), STDIN_FILENO) == -1) {
        perror("dup2");
        fclose(inputFile);
        exit(EXIT_FAILURE);
    }

    // Close the file stream after redirection
    fclose(inputFile);
        char *binaryPath = "/challenge/embryoio_level33";
        char *args[] = {NULL};
        
        // Execute the binary program in the child process
        execv(binaryPath, args);
        
        // If execv returns, an error occurred
        perror("execv");
        exit(EXIT_FAILURE);
    } else {
        // Parent process
        // Wait for the child process to finish
        wait(NULL);
    }

    return 0;
}

int main(){
 
   pwncollege();
 return 0;
}
