Scratch Hue Extension
=====================

The Scratch Hue Extension is a helper app which allows you to control a set of 
Philips Hue lights using Scratch. My students can now write programs to 
[control the lights in our classroom](http://mrproctor.net/media/hue_demo.mp4).

Installation & Setup
--------------------

1. Install the Scratch 2 Offline Editor. Instructions are here:
   http://scratch.mit.edu/scratch2download/
   (If OS X tells you it cannot be installed because it's from an unidentified
   developer, open System Preferences and select the "Security and Privacy" 
   pane.)

2. Install the Scratch Hue Extension by running these commands in Terminal.
   When you are asked to enter your password, you will not see the letters
   you type appear on the screen. This is normal.

        sudo easy_install pip
        sudo pip install scratch_hue_extension

4. Start the Scratch Hue Helper by running this command in Terminal. Right
   before you run this for the first time, press the button on the Hue Base
   Station in Room 6.

        scratch_hue_helper

5. Start the Scratch 2 Offline Editor. Then, holding down the shift key, click 
   on the "File" menu and select "Import Experimental HTTP Extension." You will 
   be asked to select a file; choose the file called "Scratch Hue Extension.s2e"
   on your Desktop.

6. Now you can write programs that interact with the lights in Room 6! Look in
   the "More Blocks" pane to see the available commands.


About
-----

This package provides a helper app to allow the Scratch 2 Offline Editor to 
control a set of Philips Hue lights. Instructions for implementing 
a helper app are at http://wiki.scratch.mit.edu/w/images/ExtensionsDoc.HTTP-9-11.pdf.

This extension was written by [Chris Proctor](http://chrisproctor.net), who taught 6th and 7th grade 
Computer Science at the Girls' Middle School in Palo Alto, CA from 2013 to 2015. 
