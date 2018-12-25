# Docker

Docker is a container platform that makes it easier to run, create and deploy applications.
By utilizing containers, a developer can package an application with all it dependencies and ship it as needed.
This allows the appliocation to run on any linux based platform regardless of the settings.
By using docker a developer can reduce the time between finishing an application and running it in production.

## Containers

Image - An exectuable package that contains the code, env variables, configuration files and libraries needed to run the application.
<br>
Container - A runtime instance of an image.
<br>
Virtual Machine - An emulation of a computer system.
<br>
<br>
The difference between a container and a Virtual Machine is that a container is lightweight, 
runs natively on linux and shares the kernel with the host system and other containers.
A virtual Machine runs an operating like system on the host system with virtual access to the resources.
<br><br>
A portable image file, called a dockerfile, can be written with the application to make sure every component travels together.
This allows developers to make sure the development environment matches the production environment for the application.
A dockerfile defines the environment for the container. 

You can use the following command to build the image:
<br>
<center><code>docker build -t <image-name> .</code></center>
<br>
You can run the docker image by using the command (-d to run detached):
<br>
<center><code>docker run -d <image-name></code></center>
<br>
Finally you can view the list of running containers by running:
<br>
<center><code>docker container ls</code></center>
<br>

## Services

Services represent the difference components of an application that are running in production.
These services are really just containers in production.
We can make use of a <code>docker-compose.yml</code> file to define, scale and run these services.
By running the 
<br>
<center><code>docker swarm init</code></center><br>
<center><code>docker stack deploy -c docker-compose.yml <service-name></code></center>
<br><br>
you will run however many instances of the image you defined in the configuration file on one host.
By changing the replicas field in the file you can either scale up or down the number of application instances.
Finally you need to teardown the application and the swarm using the following commands:
<br>
<center><code>docker stack rm <service-name></code></center><br>
<center><code>docker swarm leave --force</code></center>

## Swarms
todo
## Stacks
todo
## Deploys
todo
