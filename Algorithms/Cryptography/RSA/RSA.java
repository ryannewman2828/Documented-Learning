package com.algo.rsa;

import java.math.BigInteger;
import java.util.Random;

public class RSA {

	private BigInteger e;
	private BigInteger p;
	private BigInteger q;
	private BigInteger n;
	private BigInteger d;
	private BigInteger lambda;

	// Public key = (n, e)
	// Private key = (n, d)

	public RSA(int bits) {
		Random r = new Random();
		p = BigInteger.probablePrime(bits, r);
		q = BigInteger.probablePrime(bits, r);
		while (p.equals(q)) {
			q = BigInteger.probablePrime(bits, r);
		}
		n = p.multiply(q);
		lambda = ((p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE)))
				.divide((p.subtract(BigInteger.ONE)).gcd(q.subtract(BigInteger.ONE)));
		e = BigInteger.probablePrime(bits / 2, r);
		while (!lambda.gcd(e).equals(BigInteger.ONE)) {
			e.add(BigInteger.ONE);
		}
		d = e.modInverse(lambda);
	}

	public byte[] encrypt(byte[] message) {
		BigInteger m = new BigInteger(message);
		BigInteger c = m.modPow(e, n);
		return c.toByteArray();
	}

	public byte[] decrypt(byte[] message) {
		BigInteger c = new BigInteger(message);
		BigInteger m = c.modPow(d, n);
		return m.toByteArray();
	}
}
