'''
Name : Azwad Aziz
Session : 16
Batch : N-212-2
'''

## Both generator and the class works like Range function 
## Takes in inputs as (End,Start,Step) and prints the numbers




import sys
class Group:

    def __init__(self,end,start=0,step=1):
        self.end = end
        self.start = start
        self.step = step
        self.count =0
    
    def __iter__(self):
        return self

    def __next__(self):
        
        if self.end>self.start and self.step>0:
            if self.count == 0:
                self.count +=1
                return self.start   

            self.start = self.start + self.step
            if self.start < self.end:
                    
                return self.start
                
            
            else:
                raise StopIteration
        elif self.end<self.start and self.step<0:
            if self.count == 0:
                self.count +=1
                return self.start

            self.start = self.start + self.step
            if self.start>self.end:
                return self.start
            else:
                raise StopIteration
        else:
            print("Invalid input")
                
                 
            
         
myiter = Group(-15,9,-2)

for i in myiter:
    print(i)
# output
# 9
# 7
# 5
# 3
# 1
# -1
# -3
# -5
# -7
# -9
# -11
# -13



def Set(end,start=0,step=1):
    
    if end>start and step>0:
        while start<end:
        
            if start < end:
                yield start
                start += step
            else:
                raise sys.exit()
    
    
    elif end<start and step<0:
        while end<start:
        
            if start>end:
                yield start
                start += step
            else:
                raise sys.exit()
    
    
    else:
        print("Invalid input")

for i in Set(-10,5,-2):
    print(i)

# output 
# 5
# 3
# 1
# -1
# -3
# -5
# -7
# -9