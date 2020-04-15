# Python behave:

behave is a behavior-driven (BDD) test framework that is very similar to Cucumber, Cucumber-JVM, and SpecFlow. 
This is very different from more traditional frameworks like unittest and pytest.
Although behave is not an official Cucumber variant,
it still uses the Gherkin language (“Given-When-Then”) for behavior specification.

# Installation:
pip install -r requirements.txt

or Individually:

pip install behave

pip install -U behave # To update an already installed behave version, use:

Reporting:

pip install allure-behave

pip install json2html

# how to run:

Inside pycharm, Right click on runner file & run

or 

(venv) C:\GitCode\pycharm-projects\api-bdd-python>py runner.py

or we can also use behave command:

(venv) C:\GitCode\pycharm-projects\api-bdd-python>behave

# Folder structure: 
1. We can use structure just like inside "features" folder or 

2. split between main & test and put runner file at root level.

# Notes:

1. environment.py and behave.ini file should be inside features folder at root level.

2. by default, python behave looks for steps file inside features folder.

"pip freeze" command: Output installed packages in requirements.txt format.
"pip list" command: List installed packages


To find the steps directory behave will look in the directory containing the feature file.
If it is not present, behave will look in the parent directory, and then its parent, 
and so on until it hits the root of the filesystem. The “environment.py” file, 
if present, must be in the same directory that contains the “steps” directory (not in the “steps” directory).

# Context Attributes
A context object (Context) is handed to:

1. step definitions (step implementations)
2. behave hooks (before_all(), before_feature(), …, after_all())

Behave Attributes:
The behave runner assigns a number of attributes to the context object during a test run.

https://behave.readthedocs.io/en/latest/context_attributes.html

# classbehave.runner.Context(runner)
Hold contextual information during the running of tests.

This object is a place to store information related to the tests you’re running. 
You may add arbitrary attributes to it of whatever value you need.


# Runner with options:

    commonOptions = "--no-capture --no-capture-stderr -f plain " #behave.ini can also be used for common command line options
    file1 = "basics.feature"
    file2 = "basics2.feature"
    folder = "subfeature1/folder1"

    tagList1 ="--tags=smoke" #run all scenarios having this tag
    tagList2 = "--tags=-smoke" #Run all scenarios except not having this tag
    tagList3 = "--tags=smoke --tags=automated" #AND: scenarios having both tags
    tagList4 = "--tags=smoke,automated" #OR: scenarios having any one of both tags
    forJsonReport = ' -f allure_behave.formatter:AllureFormatter -o reports/json '
    #runner.main() # by default runs all the feature files(including in subfolders) under "features" folder,if runner file is inside features folder.
    #runner.main(commonOptions) #CL arguments to print all the print statements in step def files
    #runner.main(file1+' '+file2) #multifiles run
    #runner.main(folder)  # folder run
    #runner.main(tagList4)  # tag run
    #runner.main(commonOptions+folder+tagList1)  # multiple command line arguments
    #runner.main(forJsonReport)  # for json report
    
## Pros and Cons: 
Like all BDD test frameworks,it works best for black box testing due to its behavior focus. 
Web testing would be a great use case because user interactions can easily be described using plain language.
Reusable steps also foster a snowball effect for automation development.


However, behave would not be good for unit testing or low-level 
integration testing – the verbosity would become more of a hindrance than a helper.    
