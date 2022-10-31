"""
CP1404/CP5632 languages

estimate time to complete: 30 mins
actual time: 28 mins

start time: 12:15
finish time: 12:43

"""
from Pracs.prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in programming_languages:
    if ProgrammingLanguage.is_dynamic(language):
        print(language.name)
