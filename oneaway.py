from collections import Counter


def checkreplace(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    diff = 0
    for key in c1.keys():
        if key not in c2.keys():
            diff+=1

    if diff > 1:
        return False
    return True


def checkinsert(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    diff = 0
    for key in c2.keys():
        if key not in c1.keys():
            diff+=1

        if diff>1:
            return False
    return True



def checkremove(str1, str2):
    c1 = Counter(str1)
    c2 = Counter(str2)
    diff = 0
    for key in c1.keys():
        if key not in c2.keys():
            diff += 1
            print(diff)

    if diff > 1:
        return False
    return True


class OneAway:
    def __init__(self, str1 , str2):
        self.string1 = str1
        self.string2 = str2

        self.size1 = len(str1)
        self.size2 = len(str2)

    def oneawayornot(self):
        if self.size1 == self.size2:
            print("checkreplace" , checkreplace(self.string1, self.string2))
            return  checkreplace(self.string1, self.string2)

        elif self.size1 > self.size2:
            print("checkremove" , checkremove(self.string1 , self.string2))
            return checkremove(self.string1 , self.string2)
        else:
            print("checkinsert" , checkinsert(self.string1 , self.string2))
            return checkinsert(self.string1 , self.string2)






a = OneAway("14", "1433456")

a.oneawayornot()


