# bounce.py
#
height= 100
factor= 0.6
for i in range(10):
    height= round(height*factor, 4)
    print(height)

bounce = 1
height = 100
while bounce <= 10:
    height = round(height * 0.6 , 4)
    print(bounce, height)
    bounce += 1
