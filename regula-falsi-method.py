def f(x):
    return (x*x - x - 1);

def searchroots():
    a=float(input())
    b=float(input())
    
    e = 0.00001
    i = 0
    m=(a*f(b)-b*f(a))/(f(b)-f(a))
    if (f(a) * f(b)) > 0:
        print "Invalid index"
    else:
        while abs(f(m)) > e:
            
            m=(a*f(b)-b*f(a))/(f(b)-f(a))
            i += 1
            if abs(f(m)) < e:
                print "root = %3.5f"%m
            else:
                print "%3d %3.5f %3.5f %3.5f "%(i,a,b,f(a)*f(m))
                if f(a)*f(m) > 0:
                    a=m
                else:
                    b=m
                
                print "%3.5f %3.5f %3.5f "%(a,b,f(a)*f(m))
    
