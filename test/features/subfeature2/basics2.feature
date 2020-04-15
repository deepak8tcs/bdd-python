Feature: Showing off behave2

#  Background: this to be executed before each scenario

  @smoke
  Scenario: Run a simple test2
    Given we have behave installed
    #parameterization
    And I pass integer 9
    And I pass float 8.88
    And I pass boolean "False"
    And I pass string "deepakv"
    #dataTable
    And I update "<item>" and "<value>"
    |item   |value|
    |address|USA |
    |name   |Deepak|
    When we implement 5 tests
    Then behave will test them for us!

#
#  Scenario Outline: Run a simple test2
#    Given we have behave installed on "<os>"
#    When we implement 5 tests on "<browser>"
#    Then behave will test them for us!
#    Examples:
#        |os   |browser|
#        |mac  |chrome|
#        |windows|ie|