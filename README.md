# ROS2
Introduction for ros2-humble 

what is ROS? 
Robot Operating System 

version of ros?
Ros1: 1st version
Ros2 humble: 2nd version (is now stable)

installation link: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html


Set locale
Make sure you have a locale which supports UTF-8. 

locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

Setup Sources
You will need to add the ROS 2 apt repository to your system.

First ensure that the Ubuntu Universe repository is enabled.

sudo apt install software-properties-common
sudo add-apt-repository universe

Now add the ROS 2 GPG key with apt.

sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

Then add the repository to your sources list.

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null


Install ROS 2 packages

Update your apt repository caches after setting up the repositories.

sudo apt update
ensure your system is up to date before installing new packages.

sudo apt upgrade

Desktop Install (Recommended): ROS, RViz, demos, tutorials.
sudo apt install ros-humble-desktop


Environment setup
Sourcing the setup script

# Replace ".bash" with your shell if you're not using bash
# Possible values are: setup.bash, setup.sh, setup.zsh
source /opt/ros/humble/setup.bash

3 de julio 
ros 2 communications 
command for run a package
ros2 run (name of package)
the packages can have different programs 

rqt_graph see the graph its the representation of all the nodes are running 

we have 2 nodes (talker y listener)
in the graphic the talker noe is talking to listener node

examples 
ros2 run demo_nodes_cpp listener
ros2 run demo_nodes_cpp talker


turtlesim 

is a package to start experimenting with robots in two dimensions 
ros2 run turtlesim

to control the turtle with keyboard
ros2 run turtlesim turtle_teleop_key - responsable for send the information
ros2 run turtlesim turtlesim_node - is responsable for create the interface and to recive and execute the instruction 

