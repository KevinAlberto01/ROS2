Topic is a named bus over which nodes exchange messages
we used if often when you need to send a data stream  (uni directional)
is anonymous for the nodes 


in the topic you can have many subscribes and publisher

you can write a note in multiple languagues with the library 

with the topics doesn´t matter if only publish to no body, it still works 

a node can contain many publishers and subscribers for many different topics 

has a message that all publishers and subscribers to the topic must use the same message type 


a subscriber or is not aware of the other subscrubers and is not aware of who is publishing the data 

/chatter is simply wat to communicate betweeen nodes /talker publish to the /chatter /listener gona subscribe to the topic /chatter

ros2 topic list - with that we can see all the topic we are using,

ros2 topic info /chatter - we can see the information about the topic

ros2 interface show std_msgs/msg/String - we can see the properties of what the talker send to the listener

ros2 topic echo /chatter - we can see the information what its send

the topic is the way to communicate between different nodes nodes dont directly talk to each other they just publish or subscribe to a topic only publish or subscribe to a topic

its can have multiples notes publishing on the same topic ando mulitple nodes subscribing to the same topic

it can have the address of the topic so the nodes know where publish or where to subscribe and they have a data type so they know what to send and what to receives

