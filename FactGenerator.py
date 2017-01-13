import WikiScraper

def retrieve_fact(): #returns single entry dict with key=subject and value=content
	f=False
	while not f:
		WikiScraper.load_phrase()				#writes fact
		with open('paragraph.txt','r') as file:	#reads fact
			f=file.readlines()
			if f:
				f=f[0]
		with open('paragraph.txt','w') as file:	#erases fact
			file.write('')
	return eval(f)

def trim_fact(fact):
	sentence = ''
	for char in fact:
		sentence+=char
		if char == '.':
			break
	return sentence

def create_fact(topic=None):
	while not topic:
		topic = list(retrieve_fact().keys())[0]
	content= list(retrieve_fact().values())[0]
	fact = ''
	for tidbit in content:
		if tidbit == '[SUBJECT]':
			fact+=topic
		else:
			fact+=tidbit
	if len(fact) >120:
		fact=trim_fact(fact)
	if len(fact) >120:
		fact = create_fact()
	return fact
