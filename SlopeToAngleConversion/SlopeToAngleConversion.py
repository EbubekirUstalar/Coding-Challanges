# def arctan(slope):
#     ## a simple line equation is like: y = ax + b
#     ## slope can be found by taking derivative of y
#     ## in this case we could safely say the slope is equal to coefficient of a
    
#     ## arctan(x) = 2arctan(x/(1+(1+x^2)^1/2))
    

#     if(slope < 0.00001):
#         return slope
#     else:
#         newSlope = 0.0
#         newSlope = slope / (1 + ((1 + slope**(2))**(1/2)))
#         return 2 * arctan(newSlope)

def convert(slope):
    arctan = lambda x: 2 * arctan(x / (1 + ((1 + x**(2))**(1/2)))) if abs(x) > 0.0001 else x
    return 90-round(arctan(slope) * 180 /  3.14159265359)

print(convert(-20))
