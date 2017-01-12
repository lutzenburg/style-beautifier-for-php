import re
import sys


fileToParse = None
if len(sys.argv) < 2:
    fileToParse = input('Enter file you wish to parse: ')
else:
    fileToParse = sys.argv[1]


f = open(fileToParse, 'r+')
content = f.read()

underScoreVariables = r"(\$[a-zA-Z]+)_([a-zA-Z]{1})([a-zA-Z]+)"
classAttributeVariables = r"->([a-zA-Z]+)_([a-zA-Z]{1})([a-zA-Z]+)"
bracketSpaces = r"([\S]*)[\s]*\([\s]*(.*)[\s]*\)"

#  Convert underscore separated variables with camelcase
content = re.sub(underScoreVariables, lambda pat: pat.group(1).lower() +
                 pat.group(2).upper() + pat.group(3), content)

while len(re.findall(underScoreVariables, content)) > 0:
    content = re.sub(r'(\$[a-zA-Z]+)_([a-zA-Z]{1})([a-zA-Z]+)',
                     lambda pat: pat.group(1) + pat.group(2).upper() +
                     pat.group(3), content)

# variables after ->
content = re.sub(classAttributeVariables,
                 lambda pat: "->" + pat.group(1).lower() +
                 pat.group(2).upper() + pat.group(3), content)

while len(re.findall(classAttributeVariables, content)) > 0:
    content = re.sub(classAttributeVariables,
                     lambda pat: "->" + pat.group(1) + pat.group(2).upper() +
                     pat.group(3), content)

# If statements
content = re.sub(r'([\t]*)(if).*\((\$[a-zA-Z]+)\)\s*({)([\s]{1})?',
                 lambda pat: pat.group(1) + pat.group(2).lower() + " (" +
                 pat.group(3) + ") " + pat.group(4) +
                 '\n' + pat.group(1) + '\t', content)

# ( test )
content = re.sub(bracketSpaces, lambda pat: pat.group(1) +
                 "(" + pat.group(2).strip() + ")", content)

f.seek(0)
f.write(content)
f.close()
