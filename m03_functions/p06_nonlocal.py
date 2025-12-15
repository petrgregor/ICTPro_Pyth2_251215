global_count = 0

def outer_function():
    print("Inside outer function")

    def inner_function():
        nonlocal count
        count += 1
        print("Inside inner function")

    def inner_function2():
        global global_count
        global_count += 1

    count = 0
    for i in range(5):
        inner_function()
    print(f"count = {count}")

    for i in range(10):
        inner_function2()
    #print(f"global_count = {global_count}")


outer_function()
print(f"global_count = {global_count}")