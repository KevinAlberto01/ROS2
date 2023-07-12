# ROS2
## 1.Introduction for ros2-Humble Hawksbill

### what is ROS? 
Robot Operating System 

### version of ros?
**Ros** : 1st version. 

**Ros 2**: 2nd version (is now stable).
 - In this tutorial, we use Humble Hawksbill version

### why ros?
- Provided a standard for robotic application 
- Use on any robot
- Code separation and communication tools 
- Save you a huge amount of time and prevent you from reinventing the wheel 
- Is a language agnostic, so we can program in diferents languages like python or c++

### when to use ROS2?

Help you develop powerful and scalable robot applications, so when you need a lot of communicaction 

## 2.Tools we use 

**Terminal window**
 - Command prompt

**Visual studio**
- Code editor redefined and optimized for building and debugging modern web and cloud applications
- You can also install Microsoft Visual Studio Code from your Ubuntu's GUI
  
**Terminator**
- Its a improved terminal where you can split easily in four any layout
- To install it `sudo apt install terminator`

**Pip3**
- The official package manager and pip command for Python 3
- To install it `sudo apt install python3-pip`

**Colcon**
- Is a build tool and was created specify for ros2 
- To install it `sudo apt install python3-colcon-common-extensions`
- Put this line in your bashrc file

```
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```


language libraries 
rclpy - python
rclcpp - c++

rlc is a ros library and it means Ross Client Library also is a  library which contains all the functionalities 
