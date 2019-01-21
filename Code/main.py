# This is my first python on github.
# Mastering PEP8 styling.
# Using 78 characters for code and 72 characters for comments.


# Initialization
var_one = 0
var_two = 0
var_three = 0
var_four = 0


def long_function_name(a, b, c, d):
    pass


# More indentation included to distinguish this form the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Hanging indents should add a level.
boo = long_function_name(
        var_one, var_two,
        var_three, var_four)


# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)


def long_function_name2(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Arguments on first line forbidden when not using vertical
# alignements.
def long_function_name3(var_one, var_two,
                        var_three, var_four):
    print(var_one)


def main():
    print('Hello World, Github!')
    print(foo)
    print('This is from Linux')
    long_function_name2(1, 2, 3, 4)
    long_function_name3(1, 2, 3, 4)


if __name__ == '__main__':
    main()

