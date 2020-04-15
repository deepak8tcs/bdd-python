import glob
from json2html import *
import sys
from behave import __main__ as runner
import shutil

# pythonic runner

if __name__ == '__main__':
    sys.stdout.flush()
    json_report_folder_name = 'reports/json'
    html_report_folder_name = 'reports/'

    # remove if any reporting folder exists
    shutil.rmtree(json_report_folder_name, ignore_errors=True)
    #
    # allure reporting related command line arguments
    reportArgs = ' -f allure_behave.formatter:AllureFormatter -o ' + json_report_folder_name + '  '

    # run Behave + BDD + Python code
    featureFilePath = ' test/features '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    tagList1 = "--tags=smoke"  # run all scenarios having this tag
    file1 = "test/features/subfeature2/basics.feature"
    fullRunnerOptions = featureFilePath + reportArgs + commonRunnerOptions + tagList1

    runner.main(fullRunnerOptions)
    #
    # read resultant json file
    listOfJson = glob.glob(json_report_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJson)):
        listOfJson[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJson[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJson)):
            listOfJson[cnt] = listOfJson[cnt] + ','
        finalJson = finalJson + listOfJson[cnt]
    finalJson = '[ ' + finalJson + ' ]'
    #
    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(html_report_folder_name + 'reports.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()