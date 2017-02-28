package com.algo.rsa;

public class Main {

	public static void main(String[] args) {
		RSA encrypter = new RSA(512);
		String message = "Hello World, This is an encryption test!";

		byte[] encrypted = encrypter.encrypt(message.getBytes());
		System.out.println(new String(encrypted));

		byte[] decrypted = encrypter.decrypt(encrypted);
		System.out.println(new String(decrypted));
	}

}
