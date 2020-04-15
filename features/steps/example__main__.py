"""
Main function is the entry point of any program.
Python main function is executed only when it’s being executed as a python program.
As you know, we can also import a python program as a module,
in that case python main method should not execute.

When a python program is executed, python interpreter starts executing code inside it.
It also sets few implicit variable values, one of them is __name__ whose value is set as __main__.

For python main function, we have to define a function and then use if __name__ == '__main__'
condition to execute this function.

If the python source file is imported as module, python interpreter sets the __name__ value
to module name, so the if condition will return false and main method will not be executed.

direct run:
__name__=__main__
if statement == True, and the script in _main_will be executed

import as a module:
__name__= module's filename
if statement == false, and the script in __main__ will not be executed

Python provides us flexibility to keep any name for main method, however it’s best practice
to name it as main() method. Below code is perfectly fine, however not recommended.

===
In Python "if__name__== "__main__" allows you to run the Python files either
as reusable modules or standalone programs.
"""

print("Guru98")
def main1(): #giving main() name is recommentded
    print("hello world!")

if __name__ == "__main__": # if this is not written only guru98 and guru98 are printed
    main1()

#main() # or just use main() if using python3 or above

print("Guru99")