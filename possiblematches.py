import re
def possibleMatchs(txt, pat):
	s = pat
	s = s.replace('+', '{2}.*?')
	replaced = s.replace('-', '{4}.*?')
	matches = 0
	m = re.search(replaced, txt)
	print m
	return replaced

print possibleMatchs('aa','bb')