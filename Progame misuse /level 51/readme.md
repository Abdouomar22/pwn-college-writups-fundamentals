there is a flag in ssh-keygen -D which allows you to load keys from shared library PKCS#11 (PKCS#11 is a standard for cryptographic tokens and enables access to cryptographic hardware such as smart cards and hardware security modules (HSMs))
# Usage of ssh-keygen -D
ssh-keygen -D <pkcs11_provider>
# How to ?
we need to exploit this option (-D) to plugin our code to get privillege of root in order to read flag file .
The plugin must have C_GetFunctionList function to run normally and we plugin our code to run the shell with privileged mode
then run the command (gcc -shared escale.c -o lib.so) to create shared library , finally run the command (ssh-keygen -D ./lib.so)
and you will get a prompt of a shell then read the flag by (cat /flag) .
