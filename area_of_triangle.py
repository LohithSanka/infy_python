def area_of_triangle(height,base):
    if((type(height)!="int" and type(height)!="float") or (type(base)!="int" or type(base)!="float")):
        return "type error"
    elif(height<=0 or base<=0):
        return "value error"
    else:
        return 1/2*(height*base)
area=area_of_triangle(10.5,4)
print(area)        

