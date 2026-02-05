
if __name__ == "__main__":
    is_python_fun = True
    is_sky_green = False
    print("is_python_fun =", is_python_fun)
    print("is_sky_green =", is_sky_green)

    print("bool(1) =", bool(1))           
    print("bool(0) =", bool(0))           
    print("bool(-5) =", bool(-5))         

    print("bool('hello') =", bool("hello")) 
    print("bool('') =", bool(""))           

    print("bool([]) =", bool([]))        
    print("bool([1,2]) =", bool([1, 2]))  

    print("bool(None) =", bool(None))    
    
    text = "data"
    if text:
        print("Строка не пустая")
    else:
        print("Строка пустая")
