# Text Processing Decorator
A simple Text Processor that applies certain commands to lines of text implemented using Java and The Decorator Design Pattern

## Decorator Design Pattern
The Decorator Design Pattern falls under the set of structural patterns. The patterns main purpose is that it allows you to add new functionality to an object without altering its internal structure. This can be used to add a combination of features at runtime which is more dynamic than the static equivalent, which is configuring a static list using inheritance. This pattern is commonly used in designing user interfaces where the displayed features are specified by the client at the time of usage. 

## Usage
In the file 'input.txt' you enter the list of sentences you want to apply the decorators to</br>
In the file 'commands.txt' you enter the commands you want to be run on the words. Chain them like in the provided example</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allcaps - Converts all the lowercase letters of the word to capitals</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;double - Prints the word twice</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reverse - Prints out the reverse of the word</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop {n} - Prints the word with the first {n} characters dropped</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace {regex} {replacement} - Prints the word with the first set of characters that match the regex string {regex} replaced by {replacement}</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grep {regex} - Prints the first set of characters in the word that match {regex}</br>
