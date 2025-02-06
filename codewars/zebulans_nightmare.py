'''

Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischievous hacker that has set out to sabotage all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

"camel_case" --> "camelCase"
"zebulans_nightmare" --> "zebulansNightmare"
"get_string" --> "getString"
"convert_to_uppercase" --> "convertToUppercase"
"main" --> "main"

'''

def zebulans_nightmare(function):
    words = function.split('_')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


print(zebulans_nightmare("camel_case"))