def print_hello():
    print("Hello World!")


print_hello()


def print_hello(name):
    print(f"----Hello, {name}---")


print_hello("Adam")


#from p03_module_hello import print_hello
import p03_module_hello as p03

print_hello("Bedřich")
p03.print_hello("Cyril")
