# decorators(before/after) are advised to put under environment.py
# decorator are similar to hooks in cucumber. annotations in testNG

# all/feature/tag/scenario/step:

#
# def before_all(context):
#     print('Before All')
#
#
# def after_all(context):
#     print('After All')
#
#
# def before_feature(context, feature):
#     if 'Showing off behave' in str(feature):
#         print('====Before Feature====' + str(feature))
#
#
# def after_feature(context, feature):
#     if 'Showing off behave' in str(feature):
#         print('====After Feature====' + str(feature))
#
#
# def before_scenario(context, scenario):
#     if 'Run a simple test' in str(scenario):
#         print('===Before Scenario===' + str(scenario))
#
#
# def after_scenario(context, scenario):
#     if 'Run a simple test' in str(scenario):
#         print('===After Scenario===' + str(scenario))
#
#
# def before_step(context, step):
#     if 'we have behave installed' in str(step):
#         print('==Before Step==' + str(step))
#
#
# def after_step(context, step):
#     if 'we have behave installed' in str(step):
#         print('==After Step==' + str(step))
#
#
# def before_tag(context, tag):
#     if 'smoke' in str(tag):
#         print('=Before Tag=' + str(tag))
#
#
# def after_tag(context, tag):
#     if 'smoke' in str(tag):
#         print('=After Tag=' + str(tag))