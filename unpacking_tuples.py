def calc(x):
    perimeter = 4 * x
    area = x ** 2
    result_tuple = (perimeter, area)
    return result_tuple
    

side = int(input("Enter side length :"))
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))