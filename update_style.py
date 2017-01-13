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
stringSpacing = r"(['|\"])\s*(\.)\s*(\$[a-zA-Z]+)(\.)\s*(['|\"])"
publicVars = r"([public|private])(\s+)(?!\$this)\$([a-zA-Z]{1})"
publicVarsComplete = r"[public|private]\s*\$([a-zA-Z]+);"
classAttributeCamel = r"\$this->([a-zA-Z]+)"


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

# Fix string concat spacing
content = re.sub(stringSpacing, lambda pat: pat.group(1) + " " + pat.group(2) + " " +
                 pat.group(3) + " " + pat.group(4) + " " + pat.group(1), content)

# Captitalise references to public variables
for result in re.findall(classAttributeCamel, content):
	if result in re.findall(publicVarsComplete, content):
		 content = re.sub(r"(\$this->)(?=" + result + ")(\w{1})", lambda pat: pat.group(1) + pat.group(2).upper(), content)


# Captitalise all public variables
content = re.sub(publicVars, lambda pat: pat.group(1) + " $" + pat.group(3).upper(), content)

f.seek(0)
f.write(content)
f.close()
