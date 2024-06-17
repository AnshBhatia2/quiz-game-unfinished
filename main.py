import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

score = 0
time_left = 10
marquee_message = ""
is_game_over = False
question_file_name = "questions.txt"
questions = []
question_index = 0
question_count = 0
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    global marquee_message
    screen.clear

def update():
    pass

def read_question_file():
    global question_count, question_file_name, questions
    #writing down the code for reading a text file in python
    q_file = open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count += 1
    q_file.close()

pgzrun.go()