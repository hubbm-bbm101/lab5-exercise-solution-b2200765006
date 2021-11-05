N=int(input("Please enter your end number:"))
eventotal = 0
oddtotal = 0
even_len = 0
for i in range(1,N+1):
    if i %2==0:
        eventotal += i
        even_len += 1
    elif i %2==1:
        oddtotal += i
average_of_even = eventotal/even_len
print("Average of even numbers is : {}\n Total of odd numbers is {}".format(average_of_even,oddtotal))