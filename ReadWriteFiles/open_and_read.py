with open('about_me.txt', 'r') as f:
    #print(f.read())
    print(f.read(50))
    print(f.readline(1))
    print(f.readline())
    for i in range(1, 5): 
        print(f.readline())

with open('about_me.txt', 'r') as f:
    print(f.readlines())
    print(f.readlines(1))
    print(f.readlines(10))
    print(f.readlines(100))
    print(f.readlines(-1))

var1 = ''
var2 = ''
var3 = ''

with open('about_me.txt', 'r') as f:
    var1 = f.read(50)
    for i in f.readline():
        var2 += i
    var3 = f.readline(100)

print(var1)
print(var2)
print(var3)


var4 = ''
var5 = ''
var6 = ''
with open('about_me.txt', 'r') as f:
     var4 = f.read(5)
     for i in range(4):        #readlines()[0:4] seemed to read all lines but only return the first 4
          var5 += f.readline() #That casues var6 to be empty
     var6 = f.readline(100)


print(var4)
print(var5)
print(var6)
