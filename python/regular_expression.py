import re

text = 'ashish Ashishhello my name is ashish dixit'

# Search for a pattern
'''
match = re.search('ashish', text)
print(match)

if match:
    print('match found')
    print('start index number:', match.start())
    print('end index number:', match.end())


    #find all the occurances of the word '''
"""matches=re.findall('ashish',text,re.IGNORECASE)
print("matches:",matches)"""
new_text=re.sub('ashish','asd',text)
print('new text:',new_text)