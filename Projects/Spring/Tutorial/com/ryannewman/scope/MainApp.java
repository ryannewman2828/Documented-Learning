package com.ryannewman.scope;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
	   public static void main(String[] args) {
	      ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");

	      HelloWorld objA = (HelloWorld) context.getBean("helloWorld2");

	      objA.setMessage("I'm object A");
	      objA.getMessage();

	      HelloWorld objB = (HelloWorld) context.getBean("helloWorld2");
	      objB.getMessage();
	      
	      HelloWorld objA2 = (HelloWorld) context.getBean("helloWorld3");

	      objA2.setMessage("I'm object A");
	      objA2.getMessage();

	      HelloWorld objB2 = (HelloWorld) context.getBean("helloWorld3");
	      objB2.getMessage();
	   }
	}
