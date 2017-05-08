import re
re.match('ab*', 'aaaa')
re.match('ab*', 'cccc')

re.match('', '7-Mar-16')
match = re.match('\d+-\d+', '7-Mar-16')