# Postfix Expression Interpreter
A program that reads, prints and evaluates a mathematical expression in postfix expression using Java and The Interpreter Design Pattern

## Interpreter Design Pattern
The Interpreter Design Pattern falls under the set of behavioral patterns. The patterns main purpose is that it provides a solution to the problem of evaluating grammars or expressions. It functions by mapping a domain to a language, this language to a grammar and this grammar to a hierarchical object structure. This pattern is used heavily in SQL parsing and in symbol processing engines. 

## Usage
In the file 'input.txt' you enter the postfix expression you want the program to interpret</br>
In the file 'instructions.txt' you enter the commands you want to be run on the expression</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eval - evaluates the expression (unset variables have a value of 0)</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set {name} {value} - sets the variable with {name} to have {value}</br>
