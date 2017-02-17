# Conway's Game of Life
An Implementation of Conway's Game of Life using Java and The Observer Design Pattern

## Observer Design Pattern
The Observer Design Pattern falls under the set of behavioral patterns. The patterns main purpose is that it provides a solution to the problem of notifying dependent objects when the state of the current object is modified. It can be used to allow the scaling of large applications without the need for too much uncoupling of the components. This pattern is used in things such as notyfing friends on social media websites and comprises the view component of Model-View-Controller.

## Usage
new {n} - makes a new grid with dimensions n x n</br>
init - enters initialization mode</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enter the row and the column to toggle that cell (0 indexed)</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-1 -1 to exit initialization mode</br>
step {n} - generates the next n moves in the game</br>
time {n} - the time in miliseconds between steps</br>
