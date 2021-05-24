# In-order-pipeline-architecture
## Authors
 * Suraj Mukhia
 * Jatin Singh

## Project Description
In 5 stages in order pipeline architecture, the names of the stages are Instruction Fetch(IF), Instruction Decode(ID), Execute(EX), Memory Access(MEM) and Write Back(WB). The individual stages take one cycle to complete it. But in one cycle multiple stages of multiple instructions can be completed if the instructions are independent. So, our task is to build a simulator which shows the multiple stages of instructions per cycle of in order pipeline architecture. At last the simulator should give how many instructions it read and how many clock cycles it took to complete it.

## Experiment Setup
The input the code will be trace file. The format of trace file can be found in input.trace file.
The simulator.py will have following functions:
* fetchInstruction(instruction_id ): It is called when the pipeline is in the instruction fetch stage. It takes one parameter called instruction_id.
* decodeInstruction(instruction_id): It is called when the pipeline is in the instruction decode stage. It takes one parameter called instruction_id.
* execute(instuction_id): It is called when the pipeline is in the execute stage. It takes one parameter called instruction_id.
* memoryAccess(instruction_id): It is called when the pipeline is in the memory access stage. It takes one parameter called instruction_id.
* writeBack(instruction_id): It is called when the pipeline is the write back stage. It takes one parameter called instruction_id.
* inOrderStages(): It is called whenever the instruction is read from the input tracer file. Then it calls the relevant 5 stages pipeline functions that I have defined above.

The program code has two important variables called program_counter and clock_cycle. The program_counter holds the instruction to be executed and the clock_cycle holds the clock cycle count value.

**All the instructions are independent, it can run without any data hazards**


## Output
The output of pogram will be saved in the stats.txt file. 
The output file will contains the following:
* instuction 
* clock cycle number
  * instruction stage
  * instruction_id
  * completed instruction_id

At last total number of clock cycles and instructions executed.
