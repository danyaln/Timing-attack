import timeit
import time

possibleChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTWXYZ1234567890"

def verify_password(stored_pwd, entered_pwd):
    if len(stored_pwd) != len(entered_pwd):
        return False
    for i in range(len(stored_pwd)):
        if stored_pwd[i] != entered_pwd[i]:
            return False
    return True

def pass_len():
    pwd = 'a'
    t2 = 0
    ind = 0
    for i in range(1,15):
        s="verify_password('Dan123yal','{}')".format(pwd)
        t1 = float("{:.5f}".format(timeit.timeit(s,number=10001,globals=globals())))
        if t1 > t2:
            t2 = t1
            ind=i
        pwd+='a'
    return ind

stored_pwd = 'Dan123yal'
print(f'password length is: {pass_len()}')

while True:
    passLen = pass_len()
    leftPassLen = passLen - 1
    guessedPass = []
    passStr = ''
    entered_pwd = ''
    tmr = []
    tmr = {key:0 for key in possibleChars}
    for k in range(passLen):
        passStr = ''
        for p in guessedPass:
            passStr += p
        #pdb.set_trace()
        tmr = {key:0 for key in possibleChars}
        for i in range(20000):
            for j in possibleChars:
                entered_pwd = passStr + j + possibleChars[0] * leftPassLen
                st = time.perf_counter_ns()
                verify_password(stored_pwd, entered_pwd)
                endTime = time.perf_counter_ns() - st
                tmr[j] += endTime
        guessedPass.append(sorted(tmr, key=tmr.get, reverse=True)[0])
        leftPassLen -= 1
    print(guessedPass)