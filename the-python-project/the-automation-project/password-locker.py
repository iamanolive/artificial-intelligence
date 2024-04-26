PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345"
}

import sys
argument1, argument2 = input().split(" ")
if argument1 == "" or argument2 == "":
    print("Usage: python password-locker.py [account] - copy account password")
    sys.exit()
account = argument1

import pyperclip
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("There is no account named " + account)