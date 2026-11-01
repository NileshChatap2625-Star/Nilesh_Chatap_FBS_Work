class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec

    def __str__(self):
        return f"HR={self.hr} MIN={self.min} SEC={self.sec}"

    def __add__(self, other):
        thr = self.hr + other.hr
        tmin = self.min + other.min
        tsec = self.sec + other.sec

        return Time(thr, tmin, tsec)


t1 = Time(1, 2, 3)
t2 = Time(2, 3, 4)

print(t1 + t2)