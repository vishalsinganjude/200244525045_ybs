# Q2 Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

def appendMid(s1,s2):
    len_s1 = len(s1)//2
    appendMid = s1[:len_s1-1]+s2+s1[len_s1-1:]
    return appendMid
s1 = "Chrisdem"
s2 = "IamNewString"
print("Original string:")
print("s1 = ",s1)
print("s2 = ",s2)
print("After append in middle : ",appendMid(s1,s2))