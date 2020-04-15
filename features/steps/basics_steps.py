from behave import given, when, then, step


@given('we have behave installed')
def step_impl(context):
    pass

@given(u'I pass integer {age:d}')
def step_impl(context, age):
    print("age +1 is:", age+1)


@given(u'I pass float {percentage:f}')
def step_impl(context, percentage):
    print("percentage +1 is:", percentage+1)


@given(u'I pass boolean "{sample_boolean}"')
def step_impl(context, sample_boolean):
    print("sample_boolean is:", bool(sample_boolean))


@given(u'I pass string "{name}"')
def step_impl(context, name):
    print("name is:", name)

@given(u'I update "<item>" and "<value>"')
def step_impl(context):
    pass


@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    print("hello deepak varma")
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0

@given(u'we have behave installed on "{os}"')
def step_impl(context, os):
    pass

@when(u'we implement {number:d} tests on "{browser}"')
def step_impl(context, number, browser):
    assert number > 1 or number == 0
    context.tests_count = number
