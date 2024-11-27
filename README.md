Automated Message Sender Using pynput


This Python script utilizes the pynput library to automate the process of sending messages through a keyboard controller. It types out pre-defined messages and simulates pressing the Enter key to send them.

Key Features:

•	Automated Typing: The script uses the pynput library to control the keyboard and type messages.

•	Customizable Messages: You can modify the nickNames list and message sequence to automate different text inputs.

•	Timed Delays: Includes a customizable delay between messages for a more natural typing effect.

•	Repeated Execution: The script repeats the message sequence multiple times (set to 10 in this case).


How It Works:

1.	The script starts with a 1-second delay before beginning to type.

2.	It iterates through the list of nickNames, typing out a set of messages like "You there ??", the nickname, and emoticons in sequence.

3.	After each message is typed, the Enter key is pressed, and a small time delay is introduced between messages to simulate a real typing experience.


Usage:

1.	Install the pynput library with the following command:

  	 pip install pynput

3.	Run the script to simulate automated typing.


Customization:

•	You can modify the list nickNames to include different names or text messages.

•	Adjust the time interval by changing the value of t to speed up or slow down the message flow.

