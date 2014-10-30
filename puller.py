import re
import urllib2

charged_file = open("charged.html", 'r')
charged_text = charged_file.read()
charged_file.close()

val = re.compile("/catalog/.*\d\"")

results = val.findall(charged_text)

v = 0

for i in results:
	search_url = "http://search.library.wisc.edu" + i[:-1] + ".ris"

	# if v > 2:
	# 	break

	citation = urllib2.urlopen( search_url ).read()

	# print citation

	new_filename = str(v) + ".ris"
	new_ris = open(new_filename, "w")

	new_ris.write(citation)
	new_ris.close()

	v += 1