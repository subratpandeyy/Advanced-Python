def default_arg(name, age="20"):
    print(f'Hi my name is: {name} and I am {age} years old!'.format(name, age))

default_arg("Subrat") # default args

default_arg("Sonam", 19) # positional args

default_arg(name="Aditya", age=25) # keyword argument