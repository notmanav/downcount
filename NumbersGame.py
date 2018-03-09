#! /usr/bin/python
from __future__ import division
import random
from os.path import sys
from time import sleep
from math import floor

class Problem:
    def __init__(self):
        self.numbers=list()
        self.bigpool=[25,50,75,100]
        self.target=0
    
    def generateProblem(self):
        random.shuffle(self.bigpool)      
        howmanybig=random.randint(0,4)
        #try one more time so that 1 & 2 have double the chance than 3,4
        if(howmanybig>2 or howmanybig==0):
            howmanybig=random.randint(0,4)
        for i in range(6):
            val=random.randint(1,10)
            if(i<howmanybig):
                val=self.bigpool.pop()
            self.numbers.append(val)
        
        self.target=random.randint(100,999)
    
    
    
    def printproblem(self):
        sys.stdout.write("\r %s \x1b[K" % (self.getproblemstr()))
        sys.stdout.flush()
    
    def getproblemstr(self):
        return " | ".join(str(x) for x in self.numbers)
        

class Solver:
    
    def solveProblem(self,p):
        self.recurse(str(p.numbers[0]),p.numbers, p.target)
  
    # still has a bug that the first letter on the board is the first letter in solution. maybe adding a no-op value(0/1) as the first item in the list will fix it
    def recurse(self,stringsofar,numberslist,target):
        for i in range(1,len(numberslist)):
            #Add with previous result
            res1=numberslist[0]+numberslist[i]
            stringnow=stringsofar+"+"+str(numberslist[i])
            if(res1!=target):
                newlist=list(numberslist)
                newlist.pop(i)
                newlist.pop(0)
                newlist.insert(0, res1)
                self.recurse(stringnow,newlist,target)
            else:
                print stringnow +" || Test Result "+ str(eval(stringnow) ==target)
            #multiply with previous string
            res1=numberslist[0]*numberslist[i]
            stringnow="("+stringsofar+")*"+str(numberslist[i])
            if(res1!=target):
                newlist=list(numberslist)
                newlist.pop(i)
                newlist.pop(0)
                newlist.insert(0, res1)
                self.recurse(stringnow,newlist,target)
            else:
                print stringnow +" || Test Result "+  str(eval(stringnow) ==target)
            #subtract
            res1=numberslist[0]-numberslist[i]
            stringnow=stringsofar+"-"+str(numberslist[i])
            if(res1!=target):
                newlist=list(numberslist)
                newlist.pop(i)
                newlist.pop(0)
                newlist.insert(0, res1)
                self.recurse(stringnow,newlist,target)
            else:
                print stringnow + " || Test Result "+ str(eval(stringnow) ==target) 
            #divide
            res1=numberslist[0]/numberslist[i]
            stringnow="("+stringsofar+")/"+str(numberslist[i])
            if(res1==floor (res1)):
                if(res1!=target):
                    newlist=list(numberslist)
                    newlist.pop(i)
                    newlist.pop(0)
                    newlist.insert(0, res1)
                    self.recurse(stringnow,newlist,target)
                else:
                    print(stringnow +" || Test Result "+  str(eval(stringnow) ==target))

for i in range(1):          
    p=Problem()
    p.generateProblem()
    p.numbers=[25,75,100,50,3,3]
    p.target=996
    print p.getproblemstr()
    print p.target
    Solver().solveProblem(p)
    #p.printproblem()
    #sleep(0.5)
print
    #Solver().solveProblem(p)