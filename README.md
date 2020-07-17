# slack bot (A Python script to autopost to slack whenever you want)

Auto Post to different Slack channels all day long

Script to make it look like you're working 24/7. 
Just fill in the input fields and set the timer, and this will post interesting messages in various slack channels all day and night.

# Details of what this script does
1.) At an appointed time, the script opens slack with a keyboard hotkey. Until that time, it moves the mouse occasionally to prevent the computer from sleeping and killing the script

2.) Then, it navigates to a selected slack channel, and makes a post that you have precoded every thirty minutes (again moving the mouse in between)

3.) It repeeats this process for two other slack channels

4.) It shuts down your comupter

# NOTES:
this script uses the keyboard hotkeys for a Mac to work, leveraging pyautogui. To run on windows, simply replace the hotkeys with Windows hotkey commands.
this script is set to avoid an IT admin auto screen lock by moving the mouse every 9 minutes. You can adjust the sleep statements (or remove them) depending on your company's IT policy
this script posts a message roughly every 30 minutes. To post more or less frequently, just change the sleep timer

# Instructions:
you'll need to set up a few things first:
  - Pick three slack channels you want to post in (to add more, just copy and paste one of the functions)
  - You'll need to change the "name_of_first_channel", "name_of_second_channel", and "name_of_third_channel" fields to the actual channel names you want
  - the first posting function posts items in a list, surrounded by text. To change this, just remove the loop. It works like this:
            items = ["took care of those reports", "answerd those emails", "took care of that thing for you"]
            for item in items:
               print("Hey Boss, I " + item + " let me know if you have any questions!")   
  - The second function does the same as above, currently it is set up for links, but can be anything.
  - The third function just posts items in a list (currently links, but you can change that)
  - You'll also need to hardcode in your sudo password if you want your computer to shut down afterward. YES I KNOW IT'S A BAD IDEA TO HARDCODE YOUR PASSWORD, if you don't want to do that, just put it in a file and read the file, or set it so that you don't need sudo permissions to shut down (if your IT department allows this).
  - Don't forget to set the timer in the "main()" function. It runs on militar time, so hour=17, minute=5 means 5:05 PM.
