Logs Analysis

Udacity Log Analysis Project

Project Overview

In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

Prerequisites:

• Python3

• Vagrant

• VirtualBox


Virtual Environment Setup:

1. Ensure Vagrant, Virtual Box and Python are installed on your machine.
2. Clone the Udacity fullstack-nanodegree-vm -> https://github.com/udacity/fullstack-nanodegree-vm
3. Clone (or download) this repo into the /vagrant directory -> 
4. Download and unzip the newsdata.sql data file -> https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5. Extract zip contents into cloned /vagrant/logs-analysis directory
6. Launch the VM:
  • $ vagrant up
7. SSH into the VM:
  • On Mac/Linux - $ vagrant ssh
  • Windows use Putty or similar SSH client
8. In the VM navigate to the /vagrant/logs-analysis directory:
  • $ cd /vagrant/logs-analysis
9. Load the data into the news database already in the VM:
  • $psql -d news -f newsdata.sql
10. Run python report script:
  • $ python logs_analysis.py

