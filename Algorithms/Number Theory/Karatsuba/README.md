# Karatsuba
The Karatsuba is a divide and conquer algorithm for multiplying two large numbers together. 
The runtime of this algorithm is O(n<sup>log3</sup>). 
This is asymptotically faster than the algorithm taught in grade school for multiplying numbers together which is O(n<sup>2</sup>).
The algorithm works by basically applying the following formula <br>
x = x<sub>1</sub>B<sup>m</sup> + x<sub>0</sub><br>
y = y<sub>1</sub>B<sup>m</sup> + y<sub>0</sub><br>
<br>
xy = (x<sub>1</sub>B<sup>m</sup> + x<sub>0</sub>)(y<sub>1</sub>B<sup>m</sup> + y<sub>0</sub>)<br>
xy = pHigh * B<sup>2m</sup> + pMid * B<sup>m</sup> + pLow<br>
where: <br>
pHigh = x<sub>1</sub>y<sub>1</sub><br>
pLow = x<sub>0</sub>y<sub>0</sub><br>
pMid = (x<sub>1</sub> + x<sub>0</sub>)(y<sub>1</sub> + y<sub>0</sub>) - pHigh - pLow
