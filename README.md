# GenerateSeqDiagram

Generates basic sequence diagram using Python, which are rendered using PlantUML plugin in PyCharm.

# Steps

- Import the decorator seq() from gen_seq_diagram.py, in your code.
- Decorate each function that will be executed, with @seq().
- Run your code.
- A sample_sequence_diagram.puml will be generated.
- Append @startuml and @enduml at start and end of the generated file.
- Render sample_sequence_diagram.puml in PlantUml plugin in PyCharm. 

# Example

from gen_seq_diagram import seq

@seq()
def func1():
    print("func1 called")
	func2()
  
  
@seq()
def func2():
	print("func2 called")
