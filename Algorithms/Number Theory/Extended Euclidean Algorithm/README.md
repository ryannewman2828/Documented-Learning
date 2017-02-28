# Extended Euclidean Algorithm
The Extended Euclidean Algorithm is an extension on the Euclidean Algorithm. This algorithm calculates the GCD of two numbers, the coefficients of Bézout's identity and the quotient of the two numbers. This algorithm plays a crucial role in the field of cryptography, a specific example of this is calculating the modular multiplicative inverse in RSA cryptosystems. The algorithm works by first calculating the quotient of the two previous remainders. A new remainder is then calculated using this quotient. The previous s and t variables are then subtracted from the current s and t variables which are first multiplied by the current quotient respectively. This process is repeated until the remainder that is obtained is 0, the previous remainder is the GCD of the two original numbers, the coefficients of Bézout's identity are the previous s and t and finally the coeffecients of the GCD are the current s and t variables. 

### Example

| Index i | Quotient q<sub>i-1</sub> | Remainder r<sub>i</sub> | s<sub>i</sub>     | t<sub>i</sub>     |
|---------|--------------------------|-------------------------|-------------------|-------------------|
| 0       |                          | 246                     | 1                 | 0                 |
| 1       |                          | 144                     | 0                 | 1                 |
| 2       | 246 / 144 = 1            | 246 - 144 * 1 = 102     | 1 - 0 * 1 = 1     | 0 - 1 * 1 = -1    |
| 3       | 144 / 102 = 1            | 144 - 102 * 1 = 42      | 0 - 1 * 1 = -1    | 1 - (-1) * 1 = 2  |
| 4       | 102 / 42 = 2             | 102 - 42 * 2 = 18       | 1 - (-1) * 2 = 3  | -1 - 2 * 2 = -5   |
| 5       | 42 / 18 = 2              | 42 - 18 * 2 = 6         | -1 - 3 * 2 = -7   | 2 - (-5) * 2 = 12 |
| 6       | 18 / 6 = 3               | 18 - 6 * 3 = 0          | 3 - (-7) * 3 = 24 | -5 - 12 * 3 = -41 |