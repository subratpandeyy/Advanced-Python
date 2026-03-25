try:
    a = 10
    b = 4
    print(a+b)

except ValueError as e:
    print(e)

else:
    print("Program Execute")

finally:
    print("Program Finished")
