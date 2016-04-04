largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done": break
        if largest is None:
            largest = int(num)
        if smallest is None:
            smallest = int(num)
        if int(num) > largest:
            largest = num
        if int(num) < smallest:
            smallest = num
    except ValueError:
        print "Invalid input"
print "Maximum is", largest
print "Minimum is", smallest
