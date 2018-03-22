#! /usr/bin/python
from __future__ import division
import random
import re
from os.path import sys
from time import sleep
from math import floor

class Problem:
    def __init__(self):
        self.numbers=list()
        self.bigpool=[25,50,75,100]
        self.target=0
        self.winners=set()
    
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
        self.recurse("",0,p.numbers, p.target,p.winners,False)
        print "And the "+str(len(p.winners)) +" winners are..."
        #sort by number(amount/size) of numbers and then the length of overall string
        p.winners=sorted(p.winners,key=lambda winner: (len(re.split("[\(\)\\+\-/]+",winner)),len(winner)))
        for winner in p.winners:
            print winner + (" = "+str(p.target)) if(eval(winner) ==p.target) else ""
  
    # still has a bug that the first letter on the board is the first letter in solution. maybe adding a no-op value(0/1) as the first item in the list will fix it
    def recurse(self,stringsofar,ressofar,numberslist,target,winners,verbose):
        for i in range(0,len(numberslist)):
            #Add with previous result
            if(ressofar==0):
                resnow=numberslist[i]
                stringnow=str(numberslist[i])
                self.validate(stringnow, resnow, numberslist, target, winners,verbose, i)
            else:
                resnow=ressofar+numberslist[i]
                stringnow=stringsofar+"+"+str(numberslist[i])               
                self.validate(stringnow, resnow, numberslist, target, winners,verbose, i)
                #multiply with previous string
                resnow=ressofar*numberslist[i]
                stringnow="("+stringsofar+")*"+str(numberslist[i])
                self.validate(stringnow, resnow, numberslist, target, winners,verbose, i)
                #subtract
                resnow=ressofar-numberslist[i]
                stringnow=stringsofar+"-"+str(numberslist[i])
                self.validate(stringnow, resnow, numberslist, target, winners,verbose, i)
                #divide
                resnow=ressofar/numberslist[i]
                stringnow="("+stringsofar+")/"+str(numberslist[i])
                if(resnow==floor (resnow)):
                    self.validate(stringnow, resnow, numberslist, target, winners,verbose, i)
        
    def validate(self,stringnow,resnow,numberslist,target,winners,verbose,i):
        if(resnow!=target):
            newlist=list(numberslist)
            newlist.pop(i)
            self.recurse(stringnow,resnow,newlist,target,winners,verbose)
        else:
            if(verbose):
                print stringnow +" || Test Result "+ str(eval(stringnow) ==target)
            winners.add(stringnow)
            


for i in range(1):          
    p=Problem()
    p.generateProblem()
    #p.numbers=[50,75,100,25,3,3]
    #p.target=996
    print p.getproblemstr()
    #print p.target
    Solver().solveProblem(p)
    #p.printproblem()
    #sleep(0.5)
print
    #Solver().solveProblem(p)