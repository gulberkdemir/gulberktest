# install git on Ubuntu

##Step 1 # Install git
```
sudo apt-get update
sudo apt-get install git
```
Confirm Git the installation . run the following command to verify which version of git is installed.
```
git --version
```

To get help run the following command in command line: (where verb = config, add, commit, etc.) 

```
git help verb 
```

## Step 2 # Set Up and configure Git
After the installation of git it is advisable to do some basic git configuration. This configuration will be helpful when you will commit your code. After this basic git configuration helps to generate the infomation about the person who have commited the code.

By running the following commands you can set these config options in Git.
```
git config --global user.name "your name"
git config --global user.email "your.email@example.com"
```
Quick trick about line endings:
Windows:     ```git config --global core.autocrlf true```

Mac/Linux:    ```git config --global core.autocrlf input ```

We can view all the configuration that have been done by providing following commands:
```
git config --list
```

## Creating our first repository and Commit code using git.
Creating our first repository:
```

    mkdir git_test

    cd git_test

    git init 
```
you will observe the .git directory is created


Let's Add a file, make some changes, and run git status

```
touch HelloWorld.java
```

To check the status of git provide the following command
```

    git status 
```

Let's commit a file into the repo:

```
    git add HelloWorld.java

    git commit -m "My very first commit"

    git status 
```


    
