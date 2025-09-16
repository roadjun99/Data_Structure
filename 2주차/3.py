class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
        self.trim()

    def set(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s
        self.trim()

    def hour(self):
        return self.h
    
    def minute(self):
        return self.m
    
    def second(self):
        return self.s
    
    def isAM(self):
        return self.h < 12
    
    def isSame(self, t2):
        return (self.h, self.m, self.s) == (t2.hour(), t2.minute(), t2.second())
    
    def difference(self, t2):
        result1 = self.h * 3600 + self.m * 60 + self.s
        result2 = t2.hour() * 3600 + t2.minute() * 60 + t2.second()
        difference = abs(result1 - result2)

        h1 = difference // 3600
        m1 = (difference % 3600) // 60
        s1 = difference % 60

        return Time(h1, m1, s1)
    
    def trim(self):        
        if self.s < 0:
            self.m -= (-self.s + 59) // 60
            self.s = (self.s + 60) % 60

        if self.m < 0:
            self.h -= (-self.m + 59) // 60
            self.m = (self.m + 60) % 60

        if self.h < 0:
            self.h = 0

        if self.s >= 60:
            self.m += self.s // 60
            self.s %= 60

        if self.m >= 60:
            self.h += self.m // 60
            self.m %= 60

        self.h = self.h % 24

    def display(self): 
        print(f"{self.h:02}:{self.m:02}:{self.s:02} ")

a = Time(9,0,0)
b = Time(22,13,30)
         
print("Hour: ", a.hour())         
print("Minute: ", a.minute())     
print("Second: ", a.second())    
print("isAM: ", a.isAM())         
print("isSame: ", a.isSame(b))
print("difference: ", end = '')
a.difference(b).display()       
print("display: ", end = '')
a.display()                    