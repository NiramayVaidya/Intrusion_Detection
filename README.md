# Intrusion_Detection

The program sends a push notification to the Pushbullet Chrome Extension configured by the computer's user (ideally, instead of using the Pushbullet Chrome Extension, the Pushbullet mobile application should be used, but for proof of concept, the chrome extension is good enough)
<br/>
The push notification asks whether the person currently operating the computer is indeed the computer's user
<br/>
If the user responds with a no to the push notification, then the intrusion detection control function kicks in
<br/>
The control function displays an intruder suspected message
<br/>
It then captures a real time picture of the person who is currently operating the computer and sends it via another push notification to the user
<br/>
It finally logs off from the computer i.e. shuts it down
<br/>
On the other hand, if the user responds with a yes, then the program exits

------ 
![image](https://raw.githubusercontent.com/NiramayVaidya/Intrusion_Detection/blob/master/Intruder_Picture.png)