string ="hello world"
print([i for i in string])


symbols ='$^*ù!'
codes =[]
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

[ord(i) for i in symbols]

