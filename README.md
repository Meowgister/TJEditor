# TJEditor

Overview


TJEditor is a file editor that adds notes to a tja file. Provide a tja file in the following format with data added:

TITLE:

SUBTITLE:--

BPM:
WAVE:.ogg
OFFSET:
DEMOSTART:

COURSE:
LEVEL:
BALLOON:
SCOREINIT:
SCOREDIFF:

#START

,

#END

and so on for more courses. Up to 5 courses are supported: Edit, Oni, Hard, Normal and Easy.

The program will add blank lines automatically upon reaching the end of the file.

The program's skin uses images from the simulator TJAP3. These can be switched out but, since animations use fixed loops, don't change their names or the amount of images.

Add a .ogg file and .tja file to the inside of the song folder to allow the program to start. These cannot be in a folder.


Controls


1: Don
2: Ka
3: Big don
4: Big ka
5: Roll head
6: Big roll head
7: Balloon
8: Roll tail
9: Delete

Placing a note over an existing note will either replace or delete it depending on its type.

Spacebar: Play or pause music

Playing music doesn't cause notes to scroll.

Up: Increase note value
Down: Decrease note value

Note values: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48

Right: Scroll right
Left: Scroll left

Scrolling will move the current note value in the given direction. The current note position out of 48 is not displayed as it is unintuitive, such as the 5th 16th being the 15th note.


To be added:


+: Move 4 bars right
-: Move 4 bars left

S: Add a #SCROLL command
B: Add a #BPMCHANGE command
