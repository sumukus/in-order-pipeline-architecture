'''
Authors:
	- Suraj Mukhia
	- Jatin Singh

This is the 5 stages inorder pipleline architecture simulation. 
The input to the program is a tracer file which contains instruction to be executed.
Input file name used in code: input.trace
	Instruction format given in the teacer file is as follows
		- operation register, memory 				eg. mov R1, #223 
		or
		- operation register, register(s) 			eg. mov R2, R1 or add R3, R2, R1	

In simulation part, we have assumed instuction are independent and only loaded instructions in code. It is not executed.
Different phases of each instructions are recoreded for per cycle.
	- Pipeline Phase Instruction ID

At last, total cycles and instructions are recorded as well.
More details of output can be found in stats.txt file

'''

import csv,time

def fetchInstruction(instruction_id):
	pipeline[instruction_id].remove("IF")
	file_write.write(f"\tIF phase of instruction id: {instruction_id}\n")
	print(f"\tIF phase of instruction id: {instruction_id}")

def decodeInstruction(instruction_id):
	pipeline[instruction_id].remove("ID")
	file_write.write(f"\tID phase of instruction id:{instruction_id}\n")
	print(f"\tID phase of instruction id:{instruction_id}")

def execute(instruction_id):
	pipeline[instruction_id].remove("EX")
	file_write.write(f"\tEX phase of instruction id:{instruction_id}\n")
	print(f"\tEX phase of instruction id:{instruction_id}")

def memoryAccess(instruction_id):
	pipeline[instruction_id].remove("MEM")
	file_write.write(f"\tMEM phase of instruction id:{instruction_id}\n")
	print(f"\tMEM phase of instruction id:{instruction_id}")

def writeBack(instruction_id):
	pipeline[instruction_id].remove("WB")
	file_write.write(f"\tWB phase of instruction id:{instruction_id}\n")
	print(f"\tWB phase of instruction id:{instruction_id}")

	file_write.write(f"\t<----Instrution id:{instruction_id} completed at clock cycle:{clock_cycle}---->\n")
	print(f"\t<----Instrution id:{instruction_id} completed at clock cycle:{clock_cycle}---->")

def inOrderStages():
	global clock_cycle
	clock_cycle += 1
	flag = True
	file_write.write(f"  Different phase of instructions in clock cycle:{clock_cycle}\n")
	print(f"  Different phase of instructions in clock cycle:{clock_cycle}")
	for key, value in pipeline.items():
		if len(value) > 0:
			if value[0] == "IF":
				fetchInstruction(key)
				
			elif value[0] == "ID":
				decodeInstruction(key)
				
			elif value[0] == "EX":
				execute(key)
				
			elif value[0] == "MEM":
				memoryAccess(key)
				
			else:
				writeBack(key)
	
		else:
			delete_instructions = key
			flag = False

	if flag == False:
		pipeline.pop(delete_instructions)
	time.sleep(1)




#The program starts from here
pipeline = {}
clock_cycle = 0
program_counter = 1
file_read = open("input.trace", 'r')
file_write = open("stats.txt", 'w')
instructions = file_read.readlines()

for instruction in instructions:
	file_write.write(f"Fetching instrution {[instruction.strip()]} with instruction id:{program_counter}\n")
	print(f"Fetching instrution {[instruction.strip()]} with instruction id:{program_counter}")
	pipeline[program_counter] = ["IF", "ID", "EX", "MEM", "WB" ]
	inOrderStages()
	program_counter += 1
	

file_read.close()

while True:
	if pipeline:
		inOrderStages()
	else:
		break

file_write.write(f"\nIn order pipeline simulation completed with total clock cycle:{clock_cycle-1}\n")
print(f"\nIn order pipeline simulation completed with total clock cycle:{clock_cycle-1}")
file_write.write(f"Total number of instruction executed is:{program_counter-1}\n")
print(f"Total number of instruction executed:{program_counter-1}")



