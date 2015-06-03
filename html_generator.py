# coding: utf-8
sample = '''
TITLE: Project 2 Notes

TITLE: Breaking Problems into Smaller Pieces

DEFINITION:Computers
Computer Programs
Computer Science is how to solve problems, by breaking them into smaller pieces and making a procedure for the computer.
Programming is the core of computer science.

TITLE:Programming Tips
TIPS:
Computer:
Designed to do anything, universal machine, it can do any program.
Program:
Tells computer what to do
I is a series of instructions
Use precise sequence of steps
Computation (use rules of 3, convert units and consider Hz)
High-level language:
Python
Instead of running on computer , it runs on interpreter

TITLE:Why not English?
DEFINITION: We have to use computer language, since it is less ambiguous. Verbosity is also a factor, since we need less lines to describe a step.


TITLE:Variables
TIPS:
1.What is a variable?
A variable can change value within the program. We can make it represent whatever the programming language allows us to. 
IE strings, int, lists, dictionaries, etc.
2.What does it mean to assign a value to a variable?
To assing a value to a variable, is to make the variable represent something 
3.What is the difference between what the equals = means in math versus in programming. What's the difference between this: 2 + 3 = 5 and this: my_variable = 5?
The difference between = in math versus python is that python assigns a value, in math it shows an equality. In Python we can EVALUATE the values with == and it will tell us if the equality is True or False


TITLE: Inputs and Outputs
DEFINITION: Inputs are all the data that we are getting into our system
DEFINITION: Outputs are all the data that we pretend to get out of our system
DEFINITION: The system si the series of procedures we make to turn the input into the output
	
TITLE:Functions
DEFINITON:
What is a function?
A function is a series of procedures within our program that will (intendedly) be used more than once.
The purpose of programming is to avoid repetition, with Functions, we can use the same procedure several times without repeating code.
DEFINITION:How to make a function?
in python we use: 
def function(input):
	pass
	return output
		
DEFINITION:When you should write a function?
Whenever we need to repeat a procedure.
DEFINTITION:Why are functions so valuable.
They will help us to reduce our programming time, they avoid code repetition.



TITLE:Loops
DEFINITION:Loops help us repeat procedures. Useful for iterative purposes.
IMAGE:https://pythonproject.files.wordpress.com/2014/02/recursion_for_while.jpg


TITLE:Procedural Thinking
DEFINITION: Procedural Thinking consists on thinking the steps to take to convert our input into output.
We should always reduce the problems, and think of them as small problems to be joined in the whole.



TITLE:Debugging
DEFINITION:Bugs happend



Debugging Strategy Recap
DEFINITION:
Examine error messages when programs crash in the last line of the Python Console.
Tracebacks will tell you what went wrong.
Reading backwards from there will tell you more about where the problem occurred. 
If your modified code doesn't work, comment it out and do step by step modifications to the example code until it does what you want. 
Make sure examples work Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect. 
Check (print) intermediate results When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly. 
Keep and compare old versions When you have a working version of your code, save it before you add to the code. This will give you something to go back to if you introduce too many new bugs. 
TIPS:Split big function in small pieces
Introduce print sequences to verify flow
Keep and Compare Functions
Comment out using hash or triple quotes

TITLE:Lists
DEFINITION: The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.


TITLE:Rules of Problems
TIPS:
0. Don’t Panic
1. What are the Inputs
2. What are the outputs?
3. Solve the problem
Defensive Programing, avoid errors checking in code

TITLE:Solve the Problem
TIPS:
Understand the Inputs
Understand the Outputs
Understand the Relationship (examples)
Consider how SYSTEMATICALLY how a human solves the problem
Simple mechanical solution
Use pseudocode
Use natural language instead of programming language
Write small bits of code, and test them , know what they do 
'''





# This function finds the start of the Definitions or Concepts 
def separate_concepts(text, text_to_find):
	concept_location = []
	i = 0
	while i <len(text):
		i = text.find(text_to_find,i)
		if i != -1:
			concept_location.append(i+len(text_to_find))
		else :
			break
		i = i + len(text_to_find)
	return concept_location



#Now we will form 2 new lists with the separate_concepts function

definition_list = separate_concepts(sample,'DEFINITION:')


title_list = separate_concepts(sample,'TITLE:')


tips_list = separate_concepts(sample,'TIPS:')

image_list = separate_concepts(sample,"IMAGE:")

#Now we have to find a way to "join" the 4 lists

def rename_lists(old_list,concept):
	#we will create a list of lists, to be later rearanged
	new_list = []
	for i in old_list:
		new_list.append([i,concept])
	return new_list


list_end = [len(sample)-1,'']

# list_end was made to get the end of the text

# we should join all the rename lists and later rearrange them in order

list_to_join = rename_lists(definition_list,'DEFINITION') + rename_lists (title_list,'TITLE') + rename_lists (tips_list, 'TIPS') +rename_lists(image_list,'IMAGE') + [list_end]


list_to_join.sort()

#every div should enclose a TITLE, a DEFINITION, a TIPS, an IMAGE and an external resource, if it doesnt it will be skipped





#this will generate our Div containers
def div_kind(kind):
	
	if kind != 'IMAGE':
		first_part = '<div class = "%s' %(kind)
		last_part = '''" >

'''
		
	else:
		first_part = '<div class = "%s" ><img src="' %(kind )
		last_part = ''

	return first_part+last_part


def div_end(kind):
	if kind !='IMAGE':
	 	return '''</div>

'''
	else:
		return '''"></div>


'''

def print_html(text,concept_list):
	html_out= ''
	x = 1 # 1 will be the enclosing div 
	for i in range(0,len(concept_list)-1):
		start = concept_list[i][0]
		end = concept_list[i+1][0]-len(concept_list[i+1][1])-1
		text_to_print = text[start:end]  #It separates the text or image
		html_out = html_out + div_kind(concept_list[i][1])+ text_to_print + div_end(concept_list[i][1])
		
	return html_out

#to simplyfiy the steps, we will find <div clas = image 

			


html_header = """<!DOCTYPE html>
 <html>

<head>
	<meta charset="UTF-8">
	<title>Luis Pinto's Notes</title>
	<link rel="stylesheet" href="main.css">

<body>

"""
html_footer = """</body>		

</html>"""




print html_header + print_html(sample,list_to_join) + html_footer