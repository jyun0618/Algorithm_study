colors = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
color1 = input()
color2 = input()
color3 = input()

resist = int(str(colors.index(color1)) + str(colors.index(color2)))*(10**colors.index(color3))
print(resist)