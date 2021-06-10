import sys, pygame # Graphics
pygame.init()
import re # Regular expressions
import os # Indentify file directory
import time # Suspends execution

# Objects are used to reduce variable carryover through subroutines
# Methods are split into 4 categories: get, set, add, append
# The Song class is short and the Cursor class is long
# Consider splitting variables related to music into another class

class Song(): # Stores constants related to song metadata, and thus only uses get
    def __init__(self, filename, tja_directory, offset, current_font, game_directory):
        self.filename = filename # Stores name of the file
        self.tja_directory = tja_directory # Stores the directory of the tja file provided
        self.offset = offset # Stores the amount of time before the first beat in the music
        self.current_font = current_font # Stores the font used when drawing text
        self.game_directory = game_directory # Stores where the exe is located


    def get_filename(self):
        return self.filename


    def get_tja_directory(self):
        return self.tja_directory

    
    def get_offset(self):
        return self.offset


    def get_current_font(self):
        return self.current_font


    def get_first_line_1(self): # Could be used for difficulty changing
        return self.first_line_1


    def get_game_directory(self):
        return self.game_directory

    
class Cursor(): # This stores variables related to the "cursor", a position in the file that is used to draw notes
                # Furthermore, this will take values from commands, such as bpm changes, as the program runs
                # The cursor also relates to its position inside directory folders, hence the inclusion of the current image
                # Music position is also based on the cursor's position
    def __init__(self, line_pos, note_pos, hori_pos, vert_pos, note_centre, note_value, note_ending, current_image, current_directory, key_pressed, music_pos, current_bpm, bpm_list, bpm_list_pos, lines, first_line_1, first_line_2, first_line_3, first_line_4, first_line_5):
        self.line_pos = line_pos # Stores the literal line number of the cursor in the file; should be from where notes start
        self.note_pos = note_pos # Stores the column of the cursor in the file
        self.hori_pos = hori_pos # Stores the value of the first half of note_centre's tuple
        self.vert_pos = vert_pos # Stores the value of the second half of note_centre's tuple
        self.note_centre = note_centre # Stores the (vert, hori) position of the cursor
        self.note_value = note_value # Stores the amount of notes the cursor will move in per scroll (48/note_value)
        self.note_ending = note_ending # Stores the gramatical term for the ending of the note value (th, rd, nd)
        self.current_image = current_image # Stores the current image loaded
        self.current_directory = current_directory # Stores the current directory address to navigate image and song folders
        self.key_pressed = key_pressed # Stores the number when a key is pressed and place_note is called
        self.music_pos = music_pos # Stores the playback position of the music
        self.current_bpm = current_bpm # Stores the bpm at the cursor position
        self.bpm_list = bpm_list # Stores a list of every bpm that has been passed by the cursor
        self.bpm_list_pos = bpm_list_pos # Stores the position of the current bpm in the bpm list
        self.lines = lines # Stores the entire tja file, and removes the fps drops caused by reading the file
        self.first_line_1 = first_line_1 # Stores the first line of the first difficulty
        self.first_line_2 = first_line_2 # Stores the first line of the second difficulty
        self.first_line_3 = first_line_3 # Stores the first line of the third difficulty
        self.first_line_4 = first_line_4 # Stores the first line of the fourth difficulty
        self.first_line_5 = first_line_5 # Stores the first line of the fifth difficulty


    def get_line_pos(self):
        return self.line_pos


    def get_note_pos(self):
        return self.note_pos


    def get_hori_pos(self):
        return self.hori_pos


    def get_vert_pos(self):
        return self.vert_pos

    
    def get_note_centre(self):
        return self.note_centre

    
    def get_note_value(self):
        return self.note_value


    def get_note_ending(self):
        return self.note_ending


    def get_current_image(self):
        return self.current_image


    def get_current_directory(self):
        return self.current_directory

    
    def get_key_pressed(self):
        return self.key_pressed


    def get_music_pos(self):
        return self.music_pos


    def get_current_bpm(self):
        return self.current_bpm


    def get_bpm_list(self):
        return self.bpm_list


    def get_bpm_list_pos(self):
        return self.bpm_list_pos


    def get_lines(self):
        return self.lines


    def get_first_line_1(self):
        return self.first_line_1


    def get_first_line_2(self):
        return self.first_line_2


    def get_first_line_3(self):
        return self.first_line_3


    def get_first_line_4(self):
        return self.first_line_4


    def get_first_line_5(self):
        return self.first_line_5

    
    def set_line_pos(self, line_pos):
        self.line_pos = line_pos
        return self.line_pos


    def set_note_pos(self, note_pos):
        self.note_pos = note_pos
        return self.note_pos


    def set_hori_pos(self, hori_pos): # Setting or adding hori/vert pos also sets or adds to notecentre
        self.hori_pos = hori_pos 
        self.note_centre = (hori_pos, self.get_vert_pos())
        return self.hori_pos, self.note_centre


    def set_vert_pos(self, vert_pos):
        self.vert_pos = vert_pos
        self.note_centre = (self.get_hori_pos(), vert_pos)
        return self.vert_pos, self.note_centre

        
    def set_note_centre(self, hori_value, vert_value):
        self.set_hori_pos(hori_value)
        self.set_vert_pos(vert_value)
        return self.hori_pos, self.vert_pos, self.note_centre


    def set_note_value(self, note_value):
        self.note_value = note_value
        return self.note_value


    def set_note_ending(self, note_ending):
        self.note_ending = note_ending
        return self.note_ending

    
    def set_current_image(self, current_image):
        self.current_image = current_image
        return self.current_image


    def set_current_directory(self, current_directory):
        self.current_directory = current_directory
        return self.current_directory

    
    def set_key_pressed(self, key_pressed):
        self.key_pressed = key_pressed
        return self.key_pressed


    def set_music_pos(self, music_pos):
        self.music_pos = music_pos
        return self.music_pos

    
    def set_current_bpm(self, current_bpm):
        self.current_bpm = current_bpm
        return self.current_bpm

    
    def set_bpm_list(self, bpm_list):
        self.bpm_list = bpm_list
        return self.bpm_list

    
    def set_bpm_list_pos(self, bpm_list_pos):
        self.bpm_list_pos = bpm_list_pos
        return self.bpm_list_pos
    

    def set_line(self, line_to_set, new_line):
        self.lines[line_to_set] = new_line
        return self.lines


    def set_first_line_1(self, line_num):
        self.first_line_1 = line_num
        return self.first_line_1

    def set_first_line_2(self, line_num):
        self.first_line_2 = line_num
        return self.first_line_2

    def set_first_line_3(self, line_num):
        self.first_line_3 = line_num
        return self.first_line_3

    def set_first_line_4(self, line_num):
        self.first_line_4 = line_num
        return self.first_line_4

    def set_first_line_5(self, line_num):
        self.first_line_5 = line_num
        return self.first_line_5

        
    def add_line_pos(self, line_pos):
        self.line_pos += line_pos
        return self.line_pos


    def add_note_pos(self, note_change):
        self.note_pos += note_change
        return self.note_pos

      
    def add_hori_pos(self, hori_change):
        self.hori_pos += hori_change
        self.note_centre = (self.get_hori_pos(), self.get_vert_pos())
        return self.hori_pos, self.note_centre


    def add_vert_pos(self, vert_change):
        self.vert_pos += vert_change
        self.note_centre = (self.get_hori_pos(), self.get_vert_pos())
        return self.vert_pos, self.note_centre


    def add_note_value(self, note_value_change):
        self.note_value += note_value_change
        return self.note_value

        
    def add_music_pos(self, music_pos_change):
        self.music_pos += music_pos_change
        return self.music_pos


    def add_bpm_list_pos(self, bpm_list_pos_change):
        self.bpm_list_pos += bpm_list_pos_change
        return self.bpm_list_pos

    
    def append_to_bpm_list(self):
        self.get_bpm_list().append(self.get_current_bpm())
        return self.bpm_list

        
def run_game():
    win = pygame.display.set_mode((1280, 720)) # Tuple
    filename, filepath = get_file_info(win)
    file = open(filepath + filename +".tja","r")
    lines = file.readlines()
    file.close()
    current_bpm = get_initial_bpm(lines)
    offset = get_offset(lines)
    song_data, cursor = initialise_objects(filename, filepath, current_bpm, offset, lines)
    fix_file(song_data, cursor, win)
    cursor = find_first_lines(cursor)
    cursor.set_line_pos(cursor.get_first_line_1())
    win = display_notes(song_data, cursor, win)
    take_inputs(song_data, cursor, win)
    

def get_file_info(win):
    directory = os.listdir(os.getcwd() + "\Song") # Directory is the user's program location
    found = False # Used as a flag for whether any tja files have been given
    for item in directory:
        if item.endswith(".tja"):
            filename = item.replace(".tja","")
            filepath = os.getcwd() + "\Song\\"
            found = True
            break
        
    if not found:
        display_file_error(win, "No .tja file has been provided.")
        
    return filename, filepath

def display_error_message(win, error_text): # Objects are assumed to not be created
    text = pygame.font.SysFont('ＤＦＰ勘亭流', 50).render(error_text, True, (0, 0, 0))
    win.fill((255,255,255))
    win.blit(text, (100, 300))
    image = pygame.image.load(os.getcwd()+"\Images\Characters\Don\chara_don_error.png")
    win.blit(image, (100,50))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    raise SystemExit
    # Program execution ends after displaying the error
    

def get_initial_bpm(lines):
    bpm_line = False
    i = -1
    while not bpm_line:
        i += 1
        if re.match("[B]",str(lines[i])):
            current_bpm = lines[i][4:len(lines[i])-1]
            current_bpm = float(current_bpm)
            bpm_line = True

    return current_bpm


def get_offset(lines):
    i = -1
    offset_line = False
    while not offset_line:
        i += 1
        if re.match("[O]",str(lines[i])):
            offset = lines[i][7:len(lines[i])-1]
            offset = 0-float(offset) # Music_pos needs to be the opposite of offset
            offset_line = True
    return offset


def initialise_objects(filename, filepath, current_bpm, offset, lines):
    current_font = pygame.font.SysFont('ＤＦＰ勘亭流', 24)
    song_data = Song(filename, filepath, offset, current_font, os.getcwd())
    cursor = Cursor(0, 0, 0, 0, (0, 0), 12, "ths", "temp", filepath, 0, offset, current_bpm, [], 0, lines, 0, 0, 0, 0, 0)
    return song_data, cursor


def fix_file(song_data, cursor, win): # Applies formatting rules to the file
    j = 0 # Stores the amount of lines skipped
    try: # Catch index out of range error and break
        for i in range(len(cursor.get_lines())): # Loops for every line
            current_line = str(cursor.get_lines()[i+j])
            if re.match("[,]",current_line): # Prevents zero division error
                current_line = ("0"*48) + ",\n"
                
            if re.match("[0-9]+",current_line): # If song notation
                if not re.match("[0-9]+[,]",current_line): # If line is missing comma
                    j= merged_count(cursor, win, current_line, i, j) # Checks if separated lines contain 48 notes
                else: 
                    current_line = fix_song_notation(current_line, win)
                    cursor.set_line((i+j), current_line)
                
            elif re.match("[#][MEASURE]{7}",current_line): # MEASURE is a time signature command
                display_error_message(win, "File is not supported: it contains a #MEASURE command.")
                
    except IndexError: # File is read
        pass


def merged_count(cursor, win, current_line, i, j):
    comma = False
    while not comma: # Not having a comma will break fix_song_notation
        j += 1
        next_line = str(cursor.get_lines()[i+j])
        if not re.match("[0-9]+",next_line):
            pass
            
        elif not re.match("[0-9]+[,]",next_line):
            current_line += next_line
            j += 1
            
        elif re.match("[0-9]+[,]",next_line):
            current_line = current_line[0:(len(current_line)-1)]
            current_line += next_line
            comma = True
            j += 1
            
    divisibility_check(current_line, win)
    return j


def divisibility_check(current_line, win):
    if 48 % (len(current_line) - 2) != 0: # Checks 48 divisibility
        display_error_message(win, "File is not supported: a line is not divisible into 48.")

    
def fix_song_notation(current_line, win):
    if re.match("[0-9]*[,][/]", current_line): # Removes ending comments
        temp = current_line.split("/")
        current_line = temp[0] + "\n"
        
    divisibility_check(current_line, win)
    blank_to_add = (int(48 / (len(current_line) - 2))-1)
    current_line = add_notes(blank_to_add, current_line)
    return current_line


def add_notes(blank_to_add, current_line):
    new_line = ""
    for i in range((len(current_line))-2): # Account for ,\n
        new_line += current_line[i] + ("0"*(blank_to_add))
    new_line += ",\n"
    current_line = new_line
    return current_line


def write_to_file(song_data, cursor):
    file = open(song_data.get_tja_directory() + song_data.get_filename() + ".tja", "w")
    for i in range(len(cursor.get_lines())):
        file.write(cursor.get_lines()[i])
    file.close()


def find_first_lines(cursor): # Finds the first line per difficulty
    first_line_list = []
    for line in range(len(cursor.get_lines())):
        song_notation = False # Temp, loop variable
        extra_lines = 0 # Temp, amount of lines past #START the next song notation line is
        if re.match("[#][S][T]", cursor.get_lines()[line]):
            while not song_notation:
                extra_lines += 1
                if re.match("[0-9]*[,]", cursor.get_lines()[line+extra_lines]):
                    first_line_list.append(line+extra_lines)
                    song_notation = True
    try:         
        cursor.set_first_line_1(first_line_list[0])
        cursor.set_first_line_2(first_line_list[1])
        cursor.set_first_line_3(first_line_list[2])
        cursor.set_first_line_4(first_line_list[3])
        cursor.set_first_line_5(first_line_list[4])
        
    except IndexError:
        pass # Ignore difficulties that don't exist

    return cursor

    
def display_notes(song_data, cursor, win):
    temp_note_pos = cursor.get_note_pos() # Store original pos
    temp_line_pos = cursor.get_line_pos()
    cursor, win = refresh_window(song_data, cursor, win)
    cursor.set_note_centre(1252, 222) # 388, 222 is the note cursor, 1270 is the last note, -62 is the first note
    cursor.set_current_directory(song_data.get_game_directory() + "\\Images\\Notes\\")
    notes_placed = 0
    cursor.add_note_pos(49) # 388+"49"*18 = 1270
    
    if cursor.get_note_pos() >= 96:
        cursor.add_note_pos(-96)
        valid = False
        while not valid:
            if not re.match("[0-9]+[,]",str(cursor.get_lines()[cursor.get_line_pos()+2])):
                cursor.add_line_pos(3)
            else:
                cursor.add_line_pos(2)
                valid = True
        
    elif cursor.get_note_pos() >= 48:
        cursor.add_note_pos(-48) # If next line isn't song notation
        valid = False
        while not valid:
            if not re.match("[0-9]+[,]",str(cursor.get_lines()[cursor.get_line_pos()+1])):
                cursor.add_line_pos(2)
            else:
                cursor.add_line_pos(1)
                valid = True
            
    while notes_placed < 74: # 1270 to -62 in increments of 18 = 74 steps
        if cursor.get_line_pos() < cursor.get_first_line_1():
            cursor.set_vert_pos(191)
            cursor.add_hori_pos(52)
            cursor.set_current_image("note_barline.png")
            win = draw_image(cursor, win)
            # Print line number
            cursor.add_hori_pos(-52)
            cursor.set_vert_pos(222)
            
            text = create_text(song_data, "#START", 1, (255, 255, 255))
            cursor.add_vert_pos(109)
            cursor.add_hori_pos(48)
            win.blit(text, cursor.get_note_centre())
            cursor.add_vert_pos(-109)
            break
         
        current_line = str(cursor.get_lines()[cursor.get_line_pos()])
        if re.match("[0-9]+", current_line):
            cursor.add_note_pos(-1)
            current_note = str(cursor.get_lines()[cursor.get_line_pos()][cursor.get_note_pos()])
            if current_note == "0":
                cursor.add_hori_pos(-18)
                cursor.set_vert_pos(222)
                notes_placed += 1 

            elif current_note == "1":
                cursor.set_current_image("note_don.png")
                notes_placed, cursor, win = draw_note(notes_placed, cursor, win)
                
            elif current_note == "2":
                cursor.set_current_image("note_ka.png")
                notes_placed, cursor, win = draw_note(notes_placed, cursor, win)

            elif current_note == "3":
                cursor.set_current_image("note_big_don.png")
                notes_placed, cursor, win = draw_big_note(notes_placed, cursor, win)
                
            elif current_note == "4":
                cursor.set_current_image("note_big_ka.png")
                notes_placed, cursor, win = draw_big_note(notes_placed, cursor, win)
                
            elif current_note == "5":
                cursor.set_current_image("note_roll_head.png")
                notes_placed, cursor, win = draw_note(notes_placed, cursor, win)
                
            elif current_note == "6":
                cursor.set_current_image("note_big_roll_head.png")
                notes_placed, cursor, win = draw_big_note(notes_placed, cursor, win)

            elif current_note == "7":
                cursor.set_current_image("note_balloon.png")
                notes_placed, cursor, win = draw_note(notes_placed, cursor, win)
            
            elif current_note == "8":
                cursor.set_current_image("note_roll_tail.png")
                notes_placed, cursor, win = draw_note(notes_placed, cursor, win)

            elif current_note == "\n": # Blank line, or the end (start) of the current line
                cursor.add_hori_pos(52) # Place inside previous note
                cursor.set_vert_pos(191)
                cursor.set_current_image("note_barline.png")
                win = draw_image(cursor, win)
                # Print line number
                cursor.add_hori_pos(-52)
                cursor.set_vert_pos(222)
                cursor.add_line_pos(-1)
                cursor.set_note_pos(48)
                
        elif re.match("[#]", current_line):
            text = create_text(song_data, current_line.split("\n")[0], 1, (255, 255, 255))
            cursor.add_vert_pos(109)
            cursor.add_hori_pos(48)
            win.blit(text, cursor.get_note_centre())
            cursor.add_vert_pos(-109)
            cursor.add_hori_pos(-48)
            cursor.add_line_pos(-1)
            cursor.set_note_pos(48)
            
        else:
            cursor.add_line_pos(-1)
            cursor.set_note_pos(48)

    cursor.set_note_pos(temp_note_pos)
    cursor.set_line_pos(temp_line_pos)
    return win
            

def refresh_window(song_data, cursor, win):
    
    win.fill((255,255,255)) # Images in order of screen layer

    cursor.set_current_directory(song_data.get_game_directory() + "\Images\Background\\")
    cursor.set_current_image("bg_down.png") # Replace when clear = true (60% lines towards end)
    cursor.set_note_centre(0,360) # bg_down_scroll used when clear
    draw_image(cursor, win)

    cursor.set_current_directory(song_data.get_game_directory() + "\\Images\\Characters\\Namahage Red\\")
    cursor.set_current_image("chara_namahage_red_" + str(int(cursor.get_note_pos()/3)+1) + ".png")
    cursor.set_note_centre(50,431) # 1 animation per 16th
    draw_image(cursor, win)

    cursor.set_current_directory(song_data.get_game_directory() + "\\Images\\Characters\\Namahage Blue\\")
    cursor.set_current_image("chara_namahage_blue_" + str(int(cursor.get_note_pos()/3)+1) + ".png")
    cursor.set_note_centre(225,431)
    draw_image(cursor, win)

    cursor.set_current_directory(song_data.get_game_directory() + "\\Images\\Characters\\Namahage Green\\")
    cursor.set_current_image("chara_namahage_green_" + str(int(cursor.get_note_pos()/3)+1) + ".png")
    cursor.add_hori_pos(225)
    draw_image(cursor, win)

    cursor.set_current_directory(song_data.get_game_directory() + "\\Images\\Characters\\Namahage Red\\")
    cursor.set_current_image("chara_namahage_red_" + str(int(cursor.get_note_pos()/3)+1) + ".png")
    cursor.add_hori_pos(225)
    draw_image(cursor, win)

    cursor.set_current_directory(song_data.get_game_directory() + "\\Images\\Characters\\Namahage Blue\\")
    cursor.set_current_image("chara_namahage_blue_" + str(int(cursor.get_note_pos()/3)+1) + ".png")
    cursor.add_hori_pos(225)
    draw_image(cursor, win)
    
    cursor.set_current_directory(song_data.get_game_directory() + "\Images\Background\\")
    cursor.set_current_image("bg_footer.png")
    cursor.set_note_centre(0,676)
    draw_image(cursor, win)
    
    cursor.set_current_image("bg_up.png")
    cursor.set_note_centre(-328,1) # Less operations starting below 0
    for i in range(4): # Same as bg_down for clear graphic
        cursor.add_hori_pos(328)
        draw_image(cursor, win)
        
    cursor.set_current_directory(song_data.get_game_directory() + "\Images\Characters\Don\\")
    cursor.set_current_image("chara_don_" + str(int(cursor.get_note_pos()/3)+1) + ".png")
    cursor.set_hori_pos(0)
    draw_image(cursor, win)

    cursor.set_current_directory(song_data.get_game_directory() + "\Images\Frame\\")
##    cursor.set_current_image("frame_player.png")
##    cursor.set_vert_pos(184)
##    draw_image(cursor, win)
    
    cursor.set_current_image("frame_lane.png")
    cursor.set_note_centre(332, 136)
    draw_image(cursor, win)

##    cursor.set_current_image("frame_drum.png")
##    cursor.set_note_centre(190, 188)
##    draw_image(cursor, win)

    cursor.set_current_image("frame_gauge.png")
    cursor.set_note_centre(495, 143)
    draw_image(cursor, win)

    cursor.set_current_image("frame_gauge_soul.png")
    cursor.set_note_centre(1190, 43)
    draw_image(cursor, win)

    cursor.set_current_image("frame_lane_main.png")
    cursor.set_note_centre(0, 192)
    draw_image(cursor, win)
    cursor.set_hori_pos(333)
    draw_image(cursor, win)

    cursor.set_current_image("frame_lane_bar.png")
    cursor.set_note_centre(-500, 136)
    draw_image(cursor, win)

    cursor.set_current_image("frame_hit_marker.png")
    cursor.set_note_centre(370, 204)
    draw_image(cursor, win)
##
##    text = create_text(song_data, "Change Note Value: Up & Down", True, (0,0,0))
##    cursor.set_note_centre(10, 193)
##    win.blit(text, cursor.get_note_centre())
##    
##    text = create_text(song_data, "Scroll: Left & Right", True, (0,0,0))
##    cursor.add_vert_pos(20)
##    win.blit(text, cursor.get_note_centre())
##
##    text = create_text(song_data, "Place Note: 0-9", True, (0,0,0))
##    cursor.add_vert_pos(20)
##    win.blit(text, cursor.get_note_centre())

    text = create_text(song_data, "Note value: " + str(48//cursor.get_note_value()) + cursor.get_note_ending(), True, (255, 255, 255))
    cursor.set_note_centre(90, 367)
    win.blit(text, cursor.get_note_centre())

    return cursor, win


def create_text(song_data, message, is_bold, colour): # Colour is a tuple
    text = song_data.get_current_font().render(message, is_bold, colour)
    return text


def draw_image(cursor, win):
    image = pygame.image.load(cursor.get_current_directory() + cursor.get_current_image())
    win.blit(image, cursor.get_note_centre())
    return win


def draw_note(notes_placed, cursor, win):
    win = draw_image(cursor, win)
    cursor.add_hori_pos(-18)
    notes_placed += 1
    return notes_placed, cursor, win


def draw_big_note(notes_placed, cursor, win):
    cursor.add_hori_pos(-18)
    cursor.set_vert_pos(204)
    win = draw_image(cursor, win)
    cursor.set_vert_pos(222)
    notes_placed += 1
    return notes_placed, cursor, win


def take_inputs(song_data, cursor, win): # Main input loop, code always returns here until termination
    cursor.append_to_bpm_list()
    gamestate = 0  # Prevents multiple commands overlapping and causing errors
    endloop = False
    while True: # Infinite loop until esc or x is pressed
        if endloop:
            write_to_file(song_data, cursor)
            pygame.quit()
            raise SystemExit
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_RIGHT:
                    if gamestate == 0:
                        gamestate += 1
                        song_data, cursor, win = scroll_right(song_data, cursor, win)
                        gamestate -= 1

                elif event.key == pygame.K_LEFT:
                    if gamestate == 0:
                        gamestate += 1
                        song_data, cursor, win = scroll_left(song_data, cursor, win)
                        gamestate -= 1

                elif event.key == pygame.K_UP:
                    if gamestate == 0:
                        gamestate += 1
                        cursor, win = increase_note_value(song_data, cursor, win)
                        gamestate -= 1

                elif event.key == pygame.K_DOWN:
                    if gamestate == 0:
                        gamestate += 1
                        cursor, win = decrease_note_value(song_data, cursor, win)
                        gamestate -= 1
  
                elif event.key == pygame.K_0:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(0)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1
                        
                elif event.key == pygame.K_1:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(1)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1
                        
                elif event.key == pygame.K_2:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(2)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1
                        
                elif event.key == pygame.K_3:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(3)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1
                        
                elif event.key == pygame.K_4:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(4)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1
                        
                elif event.key == pygame.K_5:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(5)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1
                        
                elif event.key == pygame.K_6:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(6)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1

                elif event.key == pygame.K_7:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(7)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1

                elif event.key == pygame.K_8:
                    if gamestate == 0:
                        gamestate += 1
                        cursor.set_key_pressed(8)
                        win = place_note(song_data, cursor, win)
                        gamestate -= 1

                elif event.key == pygame.K_SPACE:
                    if gamestate == 0:
                        gamestate += 1
                        play_music(song_data, cursor)
                        gamestate -= 1

                elif event.key == pygame.K_ESCAPE:
                    endloop = True

            elif event.type == pygame.QUIT:
                endloop = True
                
        pygame.display.flip()


def scroll_right(song_data, cursor, win):
    cursor.add_note_pos(cursor.get_note_value())
    bpm_change_music = False # Accounts for bpm changes mid-line

    file = open(song_data.get_tja_directory() + song_data.get_filename() + ".tja","r")
    lines = file.readlines()
    file.close()
    
    current_line = str(lines[cursor.get_line_pos()])
    if re.match("[0-9]+[,]",current_line) and len(current_line) == 50: # Standard lines filter out
        if cursor.get_note_pos() >= 48:
            bpm_change_music = True
            cursor.add_note_pos(-(cursor.get_note_value())) # Subtract note value
            cursor.add_music_pos((5/cursor.get_current_bpm())*(48-cursor.get_note_pos()))
            cursor.add_note_pos(cursor.get_note_value())
            cursor.add_note_pos(-48) # Reset to the correct note position
            cursor.add_line_pos(1) # and move the cursor to the right line
            
    valid = False # Loop until current line is song notation
    while not valid:
        current_line = str(lines[cursor.get_line_pos()])
        if not re.match("[0-9]", current_line):
            if re.match("[#][BPM]", current_line):
                cursor.set_current_bpm(float(current_line[11:len(current_line)-1]))
                try: # Tracks whether a bpm has been entered before
                    song_data.set_bpm_list(cursor.get_current_bpm, cursor.get_bpm_list_pos()+1)
                except IndexError: # If the next position doesn't exist, it's a new bpm
                    cursor.append_to_bpm_list()
                cursor.add_bpm_list_pos(1) # Tracks bpm position globally
                cursor.add_line_pos(1)
            elif re.match("[#][END]", current_line): # Infinitely add more blank lines
                if re.match("[\n]",str(lines[cursor.get_line_pos()-1])): # If new line before #END
                    lines[cursor.get_line_pos()-1] = ("0"*48) + ",\n\n" # Add a blank line for editing
                    cursor.add_line_pos(-1) # End moves forward 1, cursor needs to move back 1
                else:
                    lines[cursor.get_line_pos()-1] += ("\n" + ("0"*48) + ",\n\n")
                    cursor.add_line_pos(-1)
                write_to_file(song_data, lines)
            else:
                cursor.add_line_pos(1)
        else:
             valid = True
        
    win = display_notes(song_data, cursor, win)
    
    if bpm_change_music:
        cursor.add_music_pos((5/cursor.get_current_bpm())*cursor.get_note_pos())
    else:
        cursor.add_music_pos((5/cursor.get_current_bpm())*cursor.get_note_value())
    
    return song_data, cursor, win


def scroll_left(song_data, cursor, win):
    cursor.add_note_pos(-(cursor.get_note_value()))
    
    file = open(song_data.get_tja_directory() + song_data.get_filename() + ".tja","r")
    lines = file.readlines()
    file.close()
    
    if cursor.get_line_pos() == 0:
        valid = False
        while not valid:
            if not re.match("[0-9]", str(lines[cursor.get_line_pos()])):
                cursor.add_line_pos(1)
            else:
                valid = True

    bpm_change_music = False
    
    if cursor.get_note_pos() <= -1:
        bpm_change_music = True
        cursor.add_note_pos(cursor.get_note_value())
        cursor.add_music_pos(-(5/cursor.get_current_bpm())*cursor.get_note_pos())
        cursor.add_note_pos(-(cursor.get_note_value()))
        cursor.add_note_pos(48)
        cursor.add_line_pos(-1)

    change_music_pos = True # Whether to change music normally or to the first note
    
    if re.match("[#][START]", str(lines[cursor.get_line_pos()-1])) or re.match("[#][START]", str(lines[cursor.get_line_pos()])):
        change_music_pos = False 
        cursor.set_note_pos(0)
        if cursor.get_music_pos() != song_data.get_offset():
            cursor.set_music_pos(song_data.get_offset())
        cursor.add_line_pos(1)
    else:
        valid = False
        while not valid: # Needs to scroll back to previous song notation line
            current_line = str(lines[cursor.get_line_pos()])
            if re.match("[#]",current_line) or re.match("[\n]",current_line):
                if re.match("[#][BPM]",str(lines[cursor.get_line_pos()])):
                    cursor.add_bpm_pos(-1)
                    cursor.set_current_bpm(cursor.get_bpm_list()[cursor.get_bpm_list_pos()])
                cursor.add_line_pos(-1)
            else:
                valid = True

    win = display_notes(song_data, cursor, win)
    
    if not change_music_pos:
        pass # music_pos is now offset, lowering it further will make the value too low
    elif bpm_change_music:
        cursor.add_music_pos(-((5/cursor.get_current_bpm())*(48-cursor.get_note_pos())))
    else:
        cursor.add_music_pos(-((5/cursor.get_current_bpm())*cursor.get_note_value()))
    
    return song_data, cursor, win


def decrease_note_value(song_data, cursor, win): # Higher note value = more scroll
    if cursor.get_note_value() == 1: # Would be more efficient to use factors
        cursor.set_note_value(2)
        
    elif cursor.get_note_value() == 2:
        cursor.set_note_value(3)
        
    elif cursor.get_note_value() == 3:
        cursor.set_note_value(4)
        
    elif cursor.get_note_value() == 4:
        cursor.set_note_value(6)

    elif cursor.get_note_value() == 6:
        cursor.set_note_value(8)
        
    elif cursor.get_note_value() == 8:
        cursor.set_note_value(12)
        
    elif cursor.get_note_value() == 12:
        cursor.set_note_value(16)
        
    elif cursor.get_note_value() == 16:
        cursor.set_note_value(24)
        
    if cursor.get_note_value() == 16:
        cursor.set_note_ending("rds") # Ensures note ending follows gramatical rules
        
    elif cursor.get_note_value() == 24:
        cursor.set_note_ending("nds")
        
    else:
        cursor.set_note_ending("ths")

    win = display_notes(song_data, cursor, win)
        
    return cursor, win


def increase_note_value(song_data, cursor, win):  
    if cursor.get_note_value() == 24:
        cursor.set_note_value(16)
        
    elif cursor.get_note_value() == 16:
        cursor.set_note_value(12)
        
    elif cursor.get_note_value() == 12:
        cursor.set_note_value(8)
        
    elif cursor.get_note_value() == 8:
        cursor.set_note_value(6)
        
    elif cursor.get_note_value() == 6:
        cursor.set_note_value(4)
        
    elif cursor.get_note_value() == 4:
        cursor.set_note_value(3)

    elif cursor.get_note_value() == 3:
        cursor.set_note_value(2)
        
    elif cursor.get_note_value() == 2:
        cursor.set_note_value(1)

    if cursor.get_note_value() == 16:
        cursor.set_note_ending("rds")
    
    elif cursor.get_note_value() == 24:
        cursor.set_note_ending("nds")
        
    else:
        cursor.set_note_ending("ths")

    win = display_notes(song_data, cursor, win)
    return cursor, win


def place_note(song_data, cursor, win):
    current_line = cursor.get_lines()[cursor.get_line_pos()]
    if str(current_line[cursor.get_note_pos()]) == str(cursor.get_key_pressed()) or cursor.get_key_pressed() == 0: # If note is placed or note = none
        current_line = str(current_line[0:cursor.get_note_pos()] + "0" + current_line[cursor.get_note_pos()+1:])
    else: # Split line, place note in the gap and cut the note that was there before
        current_line = str(current_line[0:cursor.get_note_pos()] + str(cursor.get_key_pressed()) + current_line[cursor.get_note_pos()+1:])
    cursor.set_line(cursor.get_line_pos(), current_line)
    win = display_notes(song_data, cursor, win)
    
    return win
    

def play_music(song_data, cursor):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.load(song_data.get_tja_directory() + song_data.get_filename() + ".ogg")
        pygame.mixer.music.play(0, cursor.get_music_pos())


run_game()

