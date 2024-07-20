"""
SCI 33 Project 1
Part3: Emulate Python namespace
"""


class NamespaceManager:
    """
    Emulate Python namespace
    """

    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        """
        Set a variable in the namespace
        :param name: name of the variable
        :param value: value of the variable
        :return: None
        """
        if name in self.namespace:
            raise KeyError(f"Variable {name} already exists.")
        self.namespace[name] = value

    def get_variable(self, name):
        """
        Get a variable from the namespace
        :param name: name of the variable
        :return: value of the variable
        """
        if name not in self.namespace:
            raise KeyError(f"Variable {name} does not exist.")
        return self.namespace[name]

    def delete_variable(self, name):
        """
        Delete a variable from the namespace
        :param name: name of the variable
        :return: None
        """
        if name not in self.namespace:
            raise KeyError(f"Variable {name} does not exist.")
        del self.namespace[name]

    def list_variables(self):
        """
        List all variables in the namespace
        :return: list of variables
        """
        if not self.namespace:
            return []
        return list(self.namespace.keys())

    def execute_function(self, code):
        """
        Execute a function in the namespace
        :param code: code of the function
        :return: None
        """
        exec(code, {}, self.namespace)


def main():
    """
    Main function
    :return: None
    """
    my_namespace = NamespaceManager()
    my_namespace.set_variable("x", 10)
    my_namespace.set_variable("y", 20)
    my_namespace.set_variable("z", 30)
    print(f"Variables are: {my_namespace.list_variables()}")
    print(f"x = {my_namespace.get_variable('x')}")
    print(f"y = {my_namespace.get_variable('y')}")
    print(f"z = {my_namespace.get_variable('z')}")

    my_namespace.delete_variable("y")
    print(f"After deleting y, variables are: {my_namespace.list_variables()}")
    code_str = """
def my_add(a, b): 
    return a + b 
print(f'my_add(x, z) = {my_add(x, z)}')
"""

    print(f'\nExecuting code:\n""" {code_str}')
    print('"""\nExecuting result:')
    my_namespace.execute_function(code_str)

    print('\nExecuting code: \n"""\nprint(f"x + z = {x + z}")\n"""')
    print("Executing result:")
    my_namespace.execute_function("print(f'x + z = {x + z}')")


if __name__ == "__main__":
    main()
