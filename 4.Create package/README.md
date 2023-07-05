go to our workspace in src directory

the package allows us to organize the code and dependecy in better way, 

ros2 pkg create (name)
ros2 pkg create my_robot_controller 

its recommenden for the name put the name of the robot and then the task that perform 

we need to specify if this is a python or c++ package, in thiws case we use python

ros2 pkg create my_robot_controller --build-type ament_  - we tap tab to see the diferrent amend

amend is the build system 

we need put the depencies  for the packages and functional that we are going to use in hte package

rclpy is the python library for ros2
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy

now we can use any text editor 

to open with the folder we use 

code . 

then we see that our package its with files, this generated automatically with the command 

inside the package we can found 

package.xml is in every in ros2 pacakge and cotains the name of the packages, dependecy is the library we declarated,

setup.cfg YOU NEVER GOING TO TOUCH IT its just to help the ros where the nodes are going to installed 

we can see a file with the same name of the principal package in this folder puts the nodes 

insidee we have a __init__.py you dont touch it 

we are going to create our rows to nodes 

we need to back to the workspace 

cd ..

and put colcon build

if you have a error like that relax, it have  a solution

we need to put in another terminal 
pip3 list 

if you have a error 

we need to install it 

sudo apt install python3-pip

after installed, we need to put in the terminal pip3 list to comprobate if the installation was successful

now we see all the package 

pip3 list | grep setutools 

if its works we can continuo but if it dont we need downgrade the version with 58.2.0

now we can see all the package has been built 


this works for fetch all the nodes and packages and is going to install it inside the install folder of the workspace

compile your package 
go to work space 
put 

colcon build 


colcon build --packages-select my_py_pkg - its works for a specific package if you want to make a few teste in one package 


C++

go to the work space, 
ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp

head of file in include directory 
if you new to add a depend you need to add in package.xml and CMakeList.txt
to compile this package
colcon build 
colcon build --packages-select my_cpp_pkg 
