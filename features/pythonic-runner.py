import sys
from behave import __main__ as runner

if __name__ == '__main__':
    sys.stdout.flush()
    runner.main()

    # runner with options:
    commonOptions = "--no-capture --no-capture-stderr -f plain " #behave.ini can also be used for common command line options
    file1 = "basics.feature"
    file2 = "basics2.feature"
    folder = "subfeature1/folder1"

    tagList1 ="--tags=smoke" #run all scenarios having this tag
    tagList2 = "--tags=-smoke" #Run all scenarios except not having this tag
    tagList3 = "--tags=smoke --tags=automated" #AND: scenarios having both tags
    tagList4 = "--tags=smoke,automated" #OR: scenarios having any one of both tags
    forJsonReport = ' -f allure_behave.formatter:AllureFormatter -o reports/json '
    #runner.main() # by default runs all the feature files(including in subfolders) under "features" folder
    #runner.main(commonOptions) #CL arguments to print all the print statements in step def files
    #runner.main(file1+' '+file2) #multifiles run
    #runner.main(folder)  # folder run
    #runner.main(tagList4)  # tag run
    #runner.main(commonOptions+folder+tagList1)  # multiple command line arguments
    #runner.main(forJsonReport)  # for json report