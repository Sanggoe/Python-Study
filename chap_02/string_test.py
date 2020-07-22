PhoneNum = "01091098806"
len = len(PhoneNum);
str = "*" * (len-4) + str(PhoneNum[len-4:])
print str