#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 09:30:32 2018

@author: mignot
"""

#Ex1

def somdiv(n):
    s=0
    for i in range(1,n):
        if n%i == 0 :
            s+=i
    return s


def parfait(n):
    liste=[]
    for i in range(1,n):
        s=0
        for j in range(1,i//2+1):
            if i%j==0:
                s+=j
        if s==i:
            liste.append(i)
    return liste


def amicaux(n):
    liste=[]
    for i in range(1,n):
        s1=0
        s2=0
        for j in range(1,i):
            if i%j==0:
                s1+=j
        for k in range(1,s1):
            if s1%k==0:
                s2+=k
        if s2==s1:
            liste.append([s1,s2])
    return liste

def amicauxb(n):
    l=[]
    for i in range(1,n):
        s = somdiv(i)
        for j in range(i+1,n):
            if s==j and somdiv(j)==i:
                l.append([i,j])
    return l

def amicauxbis(n):
    l=[]
    for i in range(1,n):
        s = somdiv(i)
        if somdiv(s)==i and i<s<n:
            l.append([i,s])
    return l

#Ex2
    
import math
from math import *

def est_premier(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def liste_premier(n):
    l = []
    for i in range(2,n+1):
        if est_premier(i)==True:
            l.append(i)
    return l

def chanceux(p):
    for k in range(0,p-1):
        if not est_premier(p+k**2+k):
            return False
    return True

def chance(n):
    li=[]
    for i in liste_premier(n):
        if chanceux(i):
            li.append(i)
    return li

#ex3
    
def taxicab(n):
    s=0
    for i in range(1,int(n**(1/3))+1):
        for j in range(i,int(n**(1/3))+1):
            if j**3+i**3 == n:
                s+=1
    if s>1 :
        return True

def liste_taxicab(n):
    li=[]
    for i in range(1,n):
        if taxicab(i):
            li.append(i)
    return(li)
    
    
#PROF
    
def taxicabb(N):
    n = int(N**(1/3)+0.1)
    li=[]
    for i in range(1,n+1):
        ic = i**3
        for j in range(i+1,n+1):
            s=ic+j**3
            if s<=N:
                for k in range(i+1,n+1):
                    kc= k**3
                    for l in range(k+1,n+1):
                        if s == kc + l**3:
                            print(f"Le taxicab numbers : {s}, peut s'écrire {i}**3+{j**3} et {k}**3+{l}**3")
                            li.append([s,[i,j],[k,l]])
    return li
                   



#ex4
def demo():
    a=123
    b=str(a)
    for x in b:
        print(int(x))
        
def suivant(x):
    x=str(x)
    xn=()
    compteur = 1
    for i in range(1,len(x)):
        if x[0]==x[i]:
            compteur += 1
        else:
            xn