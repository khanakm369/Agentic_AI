Agenda:

Whats the type of Promots
    - Zero-Shot Prompting
    - One-Shot Prompting
    - Few-Shot Prompting
    - Instruction-Based Prompting
    - Role-Based Prompting
    - Chain of Thought Prompting (IMPORTANT)


we can give 
    "role" : "system" , "content": "you are an expert in Maths and only and only ans maths related question"
    {"role" : "user". "content": "Hey, Can you write a python code to translate the word hello to hindi"}

    we should be giving first the context and only related to that it should answer not like any one asking relationship advice in ecommerce


zero shot Prompting: Directly giving the Instruction to the model
ex:
System_Promit = "You should only and only Answer the coding related stuff, your name is alexa , Do not ans any other question and if they ask say sorry"

2. Few Shot Prompting: Directly giving the instruction to the model and few examples

System_Promit = """You should only and only Answer the coding related stuff, your name is alexa , Do not ans any other question and if they ask say sorry 

Rule: 
-Strictly follow the output in JSON format

output format: {{
    "code" : "string" or null,
    "isCodingQuestion" : boolean
}}
Examples:
Q: Can you explain the a + b whole sum?
A: Sorry, I can only help with coding related questions,

Q: Hey, Write a code in python for adding two numbers.
A: def add(a, b):
    return a + b

"""

generally you give around 50-60 types of sucj QandA to make y6+874our models 50x more better and effectient- we can bing the output quality as well


Chain of Thoughts Prompting:

    -Deepseek or O3 models - they thing before they act
     
     Chain of thought is the process where an LLM generates intermediate reasoning steps before producing a final answer, improving performance on complex reasoning tasks.

""" 
Example:
Question: If 2 pens cost $4, what do 5 pens cost?
Reasoning:
- Cost per pen = 2
- 5 pens cost 10
Answer: $10

Now solve similarly:
If 8 workers build a wall in 6 days, how long for 4 workers?

"""