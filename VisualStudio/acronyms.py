"""""
acronyms =['BRB']
acronyms.append ('LOL')
acronyms.append ('IDK')
acronyms.append ('FUBAR')
acronyms.append ('SNAFU')

acronyms.remove('IDK')
del acronyms[1]
print(acronyms)

if 1 in [1, 2, 3,]:
    print('In the list')
"""

acronyms2 = ['LOL', 'IDK', 'SMH','TBH']
word = 'BFN'

if word in acronyms2:
    print(word + ' is in the list2')
else:
    print(word + ' is NOT in the list2')

for acronym in acronyms2:
    print(acronym)
