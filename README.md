# Udacity FullStack Nanodegree Item Catalog Project

This is project for Udacity FullStack Nanodegree Program which aims to familiarize students with relational database structure and establishing connection with those database by using related libraries.

In this project, Vagrant and Virtual Machine is used. Before going any further please follow the links below to install those programs.

1. Download [Virtual Box] (https://www.virtualbox.org/wiki/VirtualBox)
2. Download [Vagrant] (https://www.vagrantup.com/)


# How to run the project

1. You have to options for how to download the project
  1. You can download the project as zip and extract the desired location.
  2. You can use git clone via terminal and run the following command  ```git clone https://github.com/ernsnl/Item-Catalog.git```
2. After the you done installing the project, please navigate to directory you have just installed.
3. Run vagrant via command:  ```vagrant up```
4. Connect vagrant via command :```vagrant ssh```
5. Command above will allow you to connect vagrant virtual machine. After connecting vagrant, you will able to utilize its Linux environment.
6. All of the files that are present in repository is also present in the vagrant machine.
7. Navigate to tournament folder by using the command: ```cd /vagrant```
8. To install required python libraries, please run the following command: ``` pip install -r requirements.txt ```
9. You can test the project by running ```python run.py ```
10. Open ```localhost:5000``` in your browser.
11. Enjoy.
