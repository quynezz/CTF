using custom password generator for customizable wordlist and then check with `check_password.py`

```bash
# run this one-liner to activate the python environment and using `cupp` command
git clone https://github.com/thehackersbrain/cupp.git && cd cupp && python3 -m venv env && source env/bin/activate && pip3 install -e . && cupp -v
```
or access this website

[cupp instller ref](https://pypi.org/project/cupp/)

fill all the OSINT-ed info from `userinfo.txt`
```bash
$ cupp -i
 _________  ____ _______________________
 \_   ___ \|    |   \______   \______   \
 /    \  \/|    |   /|     ___/|     ___/
 \     \___|    |  / |    |    |    |
  \______  /______/  |____|    |____|
         \/
     Common User Password Profiler
           @thehackersbrain

[+] Enter the information about the target to make a dictionary
[*] If you don't know all the info, just hit Enter when asked! ;)

> First Name: Alice
> Surname: Johnson
> Nickname: AJ
> Birthdate (DDMMYYYY): 15071990

> Partner's Name: Bob
> Nickname:
> Partner's Birthdate (DDMMYYYY):

> Child's Name: Charlie
> Child's Nickname:
> Child's Birthday (DDMMYYYY):

> Pet's Name:
> Company Name:

> Do you want to add some keywords about the target ? [y/n] (n):
> Do you want to add special chars at the end of the words? [y/n] (n):
> Do you want to add random numbers at the end of the words? [y/n] (n):
> Leet mode ? (i.e. leet = 1337) [y/n] (n):

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[22:16:58] Wordlist (alice .txt) Created and Saved...                 functions.py:475
[+] Wordlist alice .txt saved with 5113 words.
> Hyperspeed Print? [y/n] (n):
```
```bash 
# allow the file to execute and change the wordlist file's name to match the code's name
chmod +x check_password.py
mv alice.txt passwords.txt

# run the file 
$ ./check_password.py
Password found: picoCTF{Aj_15901990}
```

FLAG: `picoCTF{Aj_15901990}`
