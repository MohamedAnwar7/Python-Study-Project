try:
    print(x)
except NameError:
    print("variable is not defined")
except:
    print('An Exception Occured')
finally:
    print('what happened here')
    
