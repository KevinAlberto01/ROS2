with the workspaces you can organize your code through differents package, you can build and install your custom code in your workspace

install the build tool for ros2 
sudo apt update
sudo apt install python3-colcon-common-extensions

we need to put this command in the bashrc, if we dont put this, we have to write this command every we open a new terminal 


cd /usr/share/colcon_argcomplete/hook/
colcon-argcomplete.bash 

source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source .bashrc - to reload the terminal and save the change of the bashrc file 


continue with the workspace 

first we need to create a folder in home 
cd

mkdir catkin_ws - you can use any name 

go to the workspace

create a src folder inside of the workspace

mkdir src 

in de workspace 

colcon build - fetch the code that is inside the source folder 

we go into the install folder 
then we need to source the setup.bash 
source ~/catkin_ws/install/setup.bash

