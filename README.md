# docker_cis_security_automation
# Docker Security CIS Benchmark Automation Tool
docker_cis_dashboard is a software that i build, to automate the process of securing Docker environments according to the Center for Internet Security (CIS) Docker Benchmark.
This tool includes a web interface built with Django and uses Ansible to automate checks against a set of machines.
This tool must be used on linux system, and it automate tests against docker installed on linux system. 

Please note: This tool is still under development and may not be fully functional.

# instalation manual
1- Install Python 3.7 or higher.
```apt-get install python3.7```

2- Install ansible
```apt-get install ansible```

3- Clone repository
```git clone https://github.com/your-username/docker-security-cis-benchmark.git```

4- Install requirements
```pip install -r requirements.txt```

5- execute run.sh
```bash run.sh```
The web interface can be accessed by visiting http://localhost:8000 in a web browser.

# Deployment using docker
Using the Dockerfile
1- Build the Docker image:
```docker build -t docker_cis_security_automation .```

2- Run the Docker image:
```docker run docker_cis_security_automation.```

# Objectives
The goals of this project are to:

Make the tool real-time, so that it can continuously monitor and enforce security best practices in Docker environments.
Make the tool configurable, so that users can configure it in the web site not manualy
Support other environments, including Windows.

# Contribution guidelines
We welcome contributions to this project! If you would like to contribute, please follow these guidelines:

Fork the repository and create a new branch for your changes.
Make your changes, and make sure to include tests for any new features.
Run the tests to ensure that everything is working correctly.
Submit a pull request, describing your changes and why they are needed.

# Contribution guidelines
We welcome contributions to this project! If you would like to contribute, please follow these guidelines:

Fork the repository and create a new branch for your changes.
Make your changes, and make sure to include tests for any new features.
Run the tests to ensure that everything is working correctly.
Submit a pull request, describing your changes and why they are needed.
