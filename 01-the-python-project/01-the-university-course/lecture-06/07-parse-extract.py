data = "From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008"
# find the at sign
atpos = data.find("@")
print(atpos)
# look for the next space after the at sign
sppos = data.find(" ", atpos)
print(sppos)
# slicing
host = data[atpos + 1 : sppos]
print(host)