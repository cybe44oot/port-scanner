## 🔍 Python Port Scanner

A lightweight and efficient command-line tool developed in Python to scan target hosts for open TCP ports. This utility is designed for network administrators, security professionals, and developers aiming to assess network security and identify open ports on target systems.

## 📌 Features
1- User-Friendly Interface: Simple command-line prompts for ease of use.

2- Customizable Scanning: Input target IP addresses and define port ranges.

3- Real-Time Feedback: Displays open ports as they are discovered.

4- Modular Codebase: Structured for easy understanding and modification.

5- CI/CD Integration: Includes a Jenkinsfile for automated testing and deployment pipelines.

## 🛠️ Prerequisites
Python 3.6 or higher

pip (Python package manager)

## 🚀 Getting Started
1. Clone the Repository

   git clone https://github.com/cybe44oot/port-scanner.git
   
cd port-scanner

2. Install Dependencies
If there are any external dependencies, install them using:


pip install -r requirements.txt

Note: Ensure that the requirements.txt file lists all necessary packages.

## 🧪 Running the Scanner
Execute the port scanner script using:

python port_scanner.py

Follow the on-screen prompts to input the target IP address and specify the port range.

## ⚙️ Jenkins Integration
This project includes a Jenkinsfile to facilitate Continuous Integration and Continuous Deployment (CI/CD). The pipeline automates the following steps:

## Dependency Installation: 

Installs all required Python packages.

Code Linting: Checks code quality and style guidelines.

Unit Testing: Runs tests to ensure code reliability.

## Deployment: Deploys the application to the specified environment.

To set up the Jenkins pipeline:

Install Jenkins on your local machine or server.

Create a new pipeline job.

Point it to this GitHub repository.

Jenkins will automatically detect the Jenkinsfile and execute the defined stages.

📁 Project Structure

.
├── port_scanner.py 


├── code_explained.py      


├── jenkinsfile            


└── README.md              


## 🌐 Future Enhancements
Web Interface: Develop a GUI using frameworks like Flask or Django to allow users to input target IPs via a web form.

## Deployment: Host the application on a Linux server using Apache or Nginx for broader accessibility.

Advanced Scanning: Incorporate features like UDP scanning, service detection, and OS fingerprinting.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

