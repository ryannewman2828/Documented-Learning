# Git
Git is the most widly used version control system in the world.
Git's performance is optimized by using real knowledge about source code file tree common attributes.
It also uses a SHA1 hash to secure the code and change history from malicious/accidental edits.
Finally Git offers flexibility in the form of offering branching and tagging to support multiple non-linear workflows.

## Setup
To start you either clone or initialize a git repository.
Initializing a git project means you have an existing project you would like to start version controlling.
To do this you run the <code>git init</code>.
You can also clone a git repository using the <code>git clone</code> command.
This gives the developer a local copy of the remote project from a central repository.
You also will want to  setup the git global configuration to include your username and email. 
The global config makes it so the configuration is on a user basis while local is for repository specific settings. 

## Saving changes
To save changes you first use the <code>git add</code> command to take changes from your local directory and add it to the staging area which signals to git that you want to update the file. Once you have staged all the files you want to change, you can run <code>git commit -m "message"</code> to save a snapshot of the code to your local git repository. 
