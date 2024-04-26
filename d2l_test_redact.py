import fitz
import re
import os
from docopt import docopt

class Redactor:

	def get_redact_data(self, lines):
	
		STUDENT_AND_ID_REGEX = r"([\w]+ [\w]+ \(Id: [\d\w]+\))"
		for line in lines:
		
			# matching the regex to each line
			if re.search(STUDENT_AND_ID_REGEX, line, re.IGNORECASE):
				search = re.search(STUDENT_AND_ID_REGEX, line, re.IGNORECASE)
				print(search.group(1))
				
				# yields creates a generator
				# generator is used to return
				# values in between function iterations
				yield search.group(1)

	# constructor
	def __init__(self, path):
		self.path = path

	def redaction(self):
	
		doc = fitz.open(self.path)
		redacted = False
		for page in doc:
			# getting boxes which contain regex matches
			redactions = self.get_redact_data(page.get_text().split('\n'))
			for data in redactions:
				redacted = True
				areas = page.search_for(data)
				
				# Mark redaction areas
				[page.add_redact_annot(area, fill = (0, 0, 0)) for area in areas]
				
			# applying the redaction
			page.apply_redactions()
			
		extension_idx = self.path.rfind(".")
		redacted_filename = self.path[:extension_idx] + "-redacted" + self.path[extension_idx:]
		if redacted:
			doc.save(redacted_filename)

		return redacted
		


def main():
	usage = ''' 
	Usage: 
	  d2l_test_redact.py FILENAME 
	  d2l_test_redact.py (-d|--dir) DIR
 	  d2l_test_redact.py (-h|--help)

	Options: 
	  -d --dir          Process all files in a driectory 
	  -h --help      Show this screen. 
	'''

	# replace it with name of the pdf file
	args = docopt(usage)

	files = []
	if args["-d"] or args["--dir"]:
		files = os.listdir(args['DIR'])
		os.chdir(args['DIR'])
	else:
		files.append(args["FILENAME"])

	number_files = 0
	redacted_files = 0
	for f in files:
		number_files += 1
		redactor = Redactor(f)
		if redactor.redaction():
			redacted_files += 1
            
	print(f"{redacted_files} of {number_files} were redacted")



if __name__ == "__main__":
    main()

