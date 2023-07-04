
/chatter is simply wat to communicate betweeen nodes 
/talker publish to the /chatter
/listener gona subscribe to the topic /chatter

ros2 topic list - with that we can see all  the topic we are using, 

ros2 topic info /chatter - we can see the information about the topic 

ros2 interface show std_msgs/msg/String - we can see the properties of what the talker send to the listener

ros2 topic echo /chatter - we can see the information what its send 

the topic is the way to communicate between different nodes
nodes dont directly talk to each other they just publish or subscribe to a topic only publish or subscribe to a topic

its can have multiples notes publishing on the same topic  ando mulitple nodes subscribing to the same topic

it can have the address of the topic so the nodes know where publish or where to subscribe and they have a data type so they know what to send and what to receives 
