#The function below returns True if two either two integers between a,b and c are greater than 0
# all inputs are integers
def positive_numbers(a,b,c):
    if a > 0 and b > 0:
        return True
    elif a > 0 and c > 0:
        return True 
    elif b > 0 and c > 0:
        return True
    elif c > 0 and a > 0:
        return True
    else: 
        return False

print(positive_numbers(-2,3,4))
print(positive_numbers(1,-5,-6))

