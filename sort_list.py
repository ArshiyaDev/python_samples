x = ['Babak','mike','4li','Bijan','2raj','1iam','Mori','Rose','3rah','0mid','00_after_0mid']
strs = list(filter(lambda x : type(x) ==str,x))
ints = list(filter(lambda x: type(x) == int, x))

output = sorted(strs) + sorted(ints)
print(output)









