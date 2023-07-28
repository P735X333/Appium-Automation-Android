def case1():
    print("This is case 1")


def case2():
    print("This is case 2")


def case3():
    print("This is case 3")

def switch_case(case):
    switch = {
        1: case1,
        2: case2,
        3: case3
    }
    return switch.get(case)()


# Example usage:
switch_case(1)  # Output: "This is case 1"
switch_case(2)  # Output: "This is case 2"
switch_case(3)  # Output: "This is case 3"
#switch_case(4)  # Output: "This is the default case"
