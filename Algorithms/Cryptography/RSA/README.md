# RSA
RSA is a public key crptosystem in which a public encrpytion key is distributed for encrpyting messages while the decrpytion (private) key is kept secret. Anyone can use this public key to encrypt messages but these messages can only be decrypted with usage of the private key. The four main components of RSA include key generation, distribution, encryption and decryption. The key generation component is comprised of randomly selecting two large prime numbers, computing there product, computing the Carmichael's totient function of said product, represented by lambda. A random value is selected from one up to the lambda and is released with the product of the two primes as the public key pair. The modular multiplicative inverse of this random number modulo lambda is released with the product as the private key pair. The distribution component works by having the public key pair transmitted to anyone who wants to send a message. The encryption stage works by calculating the ciphertext by resolving c(m) ≡ m<sup>e</sup> (mod n), where m is the message, n is the product of the 2 randomly selected primes and e is the public key exponent. similarly the plaintext can be computed by solving m(c) ≡ c<sup>d</sup> (mod n), where d is the private key exponent.

### Example
choose p = 257 and q = 337<br>
so n = 257 * 337 = 86609<br>
then λ(n) = (p - 1) * (q - 1) = 256 * 336 = 86016<br>
let e be 17, since 1 < 17 < 86016<br>
e * d ≡ 1 mod λ(n)<br>
17 * d ≡ 1 mod 86016<br>
so d = 65777<br>
Public Key = (17, 86609)<br>
Private Key = (65777, 86609)<br>
<br>
Encryption:<br>
let m be 18537<br>
c(m) ≡ m<sup>e</sup> (mod n)<br>
c(18537) ≡ 18537<sup>17</sup> (mod 86609)<br>
c(18537) ≡ 12448<br>
<br>
Decryption: <br>
m(c) ≡ c<sup>d</sup> (mod n)<br>
m(12448) ≡ 12448<sup>65777</sup> (mod 86609)<br>
m = 18537<br>

### Security
#### Faulty Key Generation
Since the prime numbers p and q have to be quite large, usually they are chosen with a probabilistic primality test algorithm. This can be problematic since the numbers aren't guarenteed to be prime. If p and q are too close to each other, then solving for them is trivial. Also the private key can be calculated quite efficiently if it is not suffeciently large.
#### Timing Attacks
The private key can be deduced if the attacker has access to several decryption time measurements and the hardware information of the decrypter. Another type of attack takes advantage of the Chinese remainder theorem optimization, an optimization put inplace to reduce computing time, by recovering RSA factorizations. To fend off against these types of attacks a technique called cryptographic blinding is used. This works by instead computing (r<sup>e</sup>c)<sup>d</sup> (mod n), where r is a random value. Using Eulers Theorem the effects of r can be removed and thus by picking a new r for every encryption, the attack fails. 
#### Padding Schemes
Some things can render plain RSA open to attacks. One of these things is that if the plaintext is sent to e or more recipients with the same exponent e, then it is possible using the Chinese remainder theorem to decrypt the ciphertext. Another possible attack is the guess and check method where the plaintext is guessed, decrypted and then compared to the encryption. One last attack is based on a property of RSA which, if you can get the private key owner to decrypt a message, allows you to use the fact that the product of the encryption of the plaintext is equivalent to the product of the two ciphertexts. These attacks are solved by adding a padding scheme into the encryption. This works by adding padding into the message which gives it the property of encrypting to a large number of different possible ciphertexts.
