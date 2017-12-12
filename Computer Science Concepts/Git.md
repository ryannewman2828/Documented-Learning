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
To save changes you first use the <code>git add</code> command to take changes from your local directory and add it to the staging area which signals to git that you want to update the file.
Once you have staged all the files you want to change, you can run <code>git commit -m "message"</code> to save a snapshot of the code to your local git repository. 
To save your local changes without commiting them you can also stash them.
To stash changes run the <code>git stash</code> command.
Running this command will stash both staged and unstaged changes, while not stashing gitignored and new files. 
Stashing your changes allows you save away the changes you've made without commiting them to work with a clean version of the project.
You can use <code>git stash apply</code> or <code>git stash pop</code> to reapply the changes from the stash to the working copy. 
Finally you can tell git to ignore files by declaring the file globs in your .gitignore file.

## Status & History
You can check the status of the git staging area by running the <code>git status</code> command. 
This can be used to check which files have been changed and which files have not been tracked by git yet. 
Files that have not yet been tracked by git fall into two main categories, they have either not been added yet or they have been git ignored.
Git will let you ignore files and directories by placing them in the <code>.gitignore</code> file.
Finally you can view the commited history with the <code>git log</code> command.
You can list project history, filter it and even search for specific changes.
This command has many option to allow for paged, filtered and formatted responses.
There is also a 40 character SHA-1 checksum issued with the commit which is a unique id specific to the commit that ensures its integrity.

## Undoing Changes
You can use the <code>git checkout</code> command to check out files and commits.
You can view an old state of the project without altering it in its current state.
This is essentially a way of loading a previous version of your project without altering the current version.
You can also undo a commited snapshot by performing a <code>git revert</code> which undoes your current changes and appends a new commit with the resulting content onto your git history.
You can also do something called resetting which goes back to a previous state and removes all subsequent commits, this can be accomplished by calling <code>git reset</code>.
Finally there exists a convencience command which removed all untracked files from your working directory and this command is <code>git clean</code>.
You can use <code>git clean</code> with <code>git reset --hard</code> to return the working state of the last particular commit. 

## Syncing
This section is dedicated to explaining how git can connect and be used with an external central repository.
You can use the <code>git remote</code> command is used for viewing, connecting and deleting remote repositories.
Remotes are key value pairs where the key is a code name for the repository and the value is a url.
The origin remote is automatically created when you first clone a repository.
This is also why most central repositories are called origin.
You can use the <code>git fetch</code> command to import commits and branches from a remote.
You can also merge upstream changes in your local branch by using the <code>git pull</code> command.
This is the same as <code>git fetch</code> followed by <code>git merge</code>.
Finally to transfer your changes to a remote repository you can use the <code>git push</code> command.

## Pull Requests

## Branching
