def my_func(x1 , x2 , x3) :
    if x1+x2+x3 == 0 :
        print('Not a number – denominator equals zero')    
    elif ((isinstance(x1, int)) or (isinstance(x2, int)) or
        (isinstance(x3, int))) :
        print('Error: parameters should be float')
    elif ((not isinstance(x1, float)) or (not isinstance(x2, float)) or
        (not isinstance(x3, float))) :
        return None
    else :
        return (((x1 + x2 + x3) * (x2 + x3) * x3)/(x1 + x2 + x3))