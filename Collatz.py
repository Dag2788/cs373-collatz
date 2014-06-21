#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    lazy = [-1]* 1000000

    if( i > j):
        i^=j
        j^=i
        i^=j 
    
    maxCycle = 1
    
    if( i < j//2):
        i = j//2 
    
    while (i <= j):

        if lazy[i] != -1 :
            return lazy[i]
        else:
            count = 1
            if i == 0 :
                count=0
            else:
                temp = i
                while (temp != 1):
                    if (temp%2) == 0 :
                        temp = temp//2
                        count = count + 1
                    else:
                        temp = temp + (temp>>1) + 1
                        count = count + 2
        if (maxCycle < count) :
            maxCycle = count
        lazy[i] = count
        i = i+1
        
    return maxCycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
