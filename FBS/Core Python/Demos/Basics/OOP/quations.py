## add integers numbers

a = 10
b = 20
print('Sum of integer = ',a+b)


c = 'Nilesh'
d = 'Chatap'

print('sum of string=', c+d)

e = 10.5
f = 12.5

print('Sum of floting numbers =', e+f)

list1 = [1,2,3]
list2 = [4,5]

print('sum of list=', list1+list2)


# class Time:
#     def __init__(self, hr, min, sec):
#         self.hr = hr
#         self.min = min
#         self.sec = sec

#     def __str__(self):
#         return f"{self.hr} : {self.min} : {self.sec}"

#     def __add__(self, other):
#         thr = self.hr + other.hr
#         tmin = self.min + other.min
#         tsec = self.sec + other.sec
        

#         return Time(thr, tmin, tsec)



# t1 = Time(1, 2, 3)
# t2 = Time(2, 3, 4)

# print(t1 + t2)



####  

class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __str__(self):
        return f"{self.hr} : {self.min} : {self.sec}"

    def __add__(self, other):
        tsec = self.sec + other.sec
        emin = tsec // 60
        tsec = tsec % 60
        tmin = self.min + other.min + emin
        ehr = tmin // 60
        tmin = tmin % 60
        thr = self.hr + other.hr + ehr

        return Time(thr, tmin, tsec)



t1 = Time(12, 33, 55)
t2 = Time(6, 30, 56)

print(t1 + t2)

