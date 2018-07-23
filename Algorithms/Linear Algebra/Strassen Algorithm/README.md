# Strassen
The Strassen algorithm is a linear algebra divide and conquer algorithm for matrix multiplication.
The algorithm works by dividing the matrix into 4 sub matrices and then performing 7 smaller multiplications
before combining the matrices to arrive at the answer. 
The naive approach has a runtime of O(n<sup>log<sub>2</sub>8</sup>) but the algorithm utilizing 7 
which is implemented here has a runtime of O(n<sup>log<sub>2</sub>7</sup>).
