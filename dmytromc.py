from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton, QButtonGroup,
        QPushButton, QLabel)
from random import shuffle
from random import randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []


question_list.append(Question("Як звати персонажа Тачки?","Меквін", "Метр", "Бас", "Петро"))
question_list.append(Question("Яка мова в Україні?","українська", "англ", "нім", "польська"))
question_list.append(Question("Скільки днів у тижні?","7", "5", "6", "8"))
question_list.append(Question("Столиця України?","Київ", "Львів", "Одеса", "Харків"))
question_list.append(Question("2 + 2 = ?","4", "3", "5", "22"))
question_list.append(Question("Якого кольору небо?","синє", "зелене", "червоне", "жовте"))
question_list.append(Question("Скільки місяців у році?","12", "10", "11", "13"))
question_list.append(Question("Яка планета найближча до Сонця?","Меркурій", "Земля", "Марс", "Венера"))
question_list.append(Question("Хто написав 'Кобзар'?","Шевченко", "Франко", "Леся", "Котляревський"))
question_list.append(Question("Скільки лап у кота?","4", "2", "3", "5"))
question_list.append(Question("Який океан найбільший?","Тихий", "Атлантичний", "Індійський", "Північний"))
question_list.append(Question("Яка тварина гавкає?","Собака", "Кіт", "Корова", "Кінь"))
question_list.append(Question("Скільки букв в українському алфавіті?","33", "32", "30", "35"))
question_list.append(Question("Яка пора року після весни?","літо", "осінь", "зима", "весна"))
question_list.append(Question("Який фрукт червоний?","яблуко", "банан", "груша", "ківі"))




app = QApplication([])


btn_OK = QPushButton('Відповісти')
lb_Question = QLabel('Найскладніше питання світу')
RadioGroupBox = QGroupBox("Варіанти відповідей")


rbtn_1 = QRadioButton('Відповідь 1')
rbtn_2 = QRadioButton('Відповідь 2')
rbtn_3 = QRadioButton('Відповідь 3')
rbtn_4 = QRadioButton('Відповідь 4')


layout_ans1 = QHBoxLayout()  
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат")
lb_Result = QLabel('Чи ви праві чи ні?')
lb_Correct = QLabel('Відповідь буде тут')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)




layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()




layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)  
layout_line2.addWidget(AnsGroupBox)  
RadioGroupBox.hide()


layout_line3.addStretch(1)  
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


def show_results():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):                       #NEW
    shuffle(answers)                        #NEW
    answers[0].setText(q.right_answer)      #NEW
    answers[1].setText(q.wrong1)            #NEW
    answers[2].setText(q.wrong2)            #NEW
    answers[3].setText(q.wrong3)            #NEW
    lb_Question.setText(q.question)         #NEW
    lb_Correct.setText(q.right_answer)      #NEW
    show_question()


def show_correct(result):
    lb_Result.setText(result)
    show_results()


def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        print("Статистика:\nКіс-ть питань:", window.total, "\nПравильних відповідей", window.score)
        window.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked:
            show_correct("Не правильно!")
            print("Статистика:\nКіс-ть питань:", window.total, "\nПравильних відповідей", window.score)


#NEW
def next_question():
    window.total += 1
    print("Статистика:\nКіс-ть питань:", window.total, "\nПравильних відповідей", window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


#NEW
def click_OK():
    if btn_OK.text() == "Відповісти":
        check_answer()
    elif btn_OK.text() == 'Наступне питання':
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')


#NEW
window.cur_question = -1
btn_OK.clicked.connect(click_OK)


window.score = 0
window.total = 0


next_question()
window.show()
app.exec()





