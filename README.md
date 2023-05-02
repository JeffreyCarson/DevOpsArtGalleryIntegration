# DevOpsArtGalleryIntegration

Jeffrey Carson
April 25, 2023
Course: CS333 Testing and DevOps 
Instructor: Erin Keith
Final Project


# Build and Test infastructure

To automatically build and test, I am using a GitHub action to automate running my tests when I push to main.


# Build and Deploy Infastructure

To automatically build and deploy, I have a separate GitHub Action to automate building a docker image and pushing it to GitHub Packages. This also happens when I push to main.


# To Run Docker Image (On MacOS)

Note: Although it is possible, I do not recommend trying to run this image, as it is a Tkinter GUI. On MacOS it is very difficult to set this up [see below]. I have no idea how this would be done on another OS.

(Need: XQuartz, socat) [If on mac, idek what you would do on windows.]

    - make sure XQuarts is closed and not running (First enable "Allow connections from network clients" in the security tab in XQuartz.)

    - run socat (in a separate terminal)

        socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"

    - open XQuartz

        open -a XQuartz

    - Pull Docker image from github

        docker pull ghcr.io/jeffreycarson/devopsartgalleryintegration:main

    - Containerize

        docker run -d -e DISPLAY=<your ip>:0 ghcr.io/jeffreycarson/devopsartgalleryintegration:main

# Final Project Design Document

Project’s existing functionality and technologies used

The software application I will be using for the final project is a personal project that I completed in the summer of 2022. The technologies that I used include Python and Tkinter. My project visualizes the art gallery problem through interactive software. The art gallery problem is a well-studied visibility problem in computational geometry. The premise is given a 2D polygon, where should you place guards that would theoretically have “vision” of the entire gallery? A mathematical definition is given below.

“The art gallery problem is formulated in geometry as the minimum number of guards that need to be placed in an n-vertex simple polygon such that all points of the interior are visible. A simple polygon is a connected closed region whose boundary is defined by a finite number of line segments. Visibility is defined such that two points u and v are mutually visible if the line segment joining them lies inside the polygon.” -Nicole Chesnokov

The art gallery problem can be applied in fields such as robotics and artificial intelligence, where movement around an environment is crucial. My project is interactive as it allows the user to input their own polygon and then visualizes each step of the algorithm. It is used as an educational tool. Below are photos of the software depicting the various steps used to solve the art gallery problem.



Test Plan

In order to increase the unit test coverage to at least 75%, I plan on reconfiguring my code to be object oriented and more modular. Currently the project’s architecture only uses functions, and this current layout will prove difficult to reach such high code coverage. To measure test coverage I will be using coverage.py, which measures code coverage during test execution. My plan for including at least 5 integration tests is to test combinations of my code and its interactions with the methods from the Tkinter library.



Plan for centralizing source code and automating the build and testing process.

My plan for centralizing source code is to use git, which is a popular open source distributed version control system. Although I am working alone, having a central repository in the cloud is especially useful for managing my code. I will be using GitHub workflows to automate the build and testing process whenever I push my code to the central repository. This is the most convenient technology to use due to the experience gained from using it within class.



Plan for automating the build and deployment of finished software.

In order to automate the build and deployment of my software, I plan on using Docker. Docker allows you to configure automated builds for easy deployment. I am using Docker due to my familiarity with the software and its extensive documentation, making this my best choice for deployment.