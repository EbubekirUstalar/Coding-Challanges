
## a simple line equation is like: y = ax + b
## slope can be found by taking derivative of y
## in this case we could safely say the slope is equal to coefficient of a


def convert(slope):
    arctan = lambda x: 2 * arctan(x / (1 + ((1 + x**(2))**(1/2)))) if abs(x) > 0.0001 else x ## arctan(x) = 2arctan(x/(1+(1+x^2)^1/2))
                                                                                             ## In small value of x we can say that arctan(x) = x, So I wanted to lower degree over time
    return 90-round(arctan(slope) * 180 /  3.14159265359)                                    ## The result return radian we need to change it to degree

print(convert(-20))


## I wanted to write it in a more less code way, but i did not know that we can import libraries
## everybody besides me imported library
