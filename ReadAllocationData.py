## @file ReadAllocationData.py
#  @author Zihao Chen
#  @brief Provides the function that returns the list of dictionary data.
#  @date 18/01/2019

  ## @brief Take a input txt file and return the list of dictionaries of student data.
  #  @param s the input value correspond to a file name.
  #  @return The list of the students.
def readStdnts(s):
    input_file = open(s, 'r')
    lines = input_file.readlines()
    student_dict = {}
    Student = []
    line = []
    for i in range(len(lines)):
        line.append(lines[i].split(','))
    for j in range(len(line)):
        student_dict['macid'] = line[j][0]
        student_dict['fname'] = line[j][1]
        student_dict['lname'] = line[j][2]
        student_dict['gender'] = line[j][3]
        student_dict['gpa'] = float(line[j][4])
        student_dict['choices'] = (line[j][5],line[j][6], line[j][7])
        Student.append(student_dict)
        student_dict = {}
    return Student

	
  ## @brief Take a input txt file and return the list of free choice.
  #  @param s the input value correspond to a file name.
  #  @return The list of free choice.

def readFreeChoice(s):
    input_file = open(s, 'r')
    lines = input_file.readlines()
    line = []
    free_choice = []
    for i in range(len(lines)):
        line.append(lines[i].split(','))
    for j in range(len(line)):
        if line[j][1][:3] == "Yes":
            free_choice.append(line[j][0])
    return free_choice
	
  ## @brief Take a input txt file and return the list of department capacity.
  #  @param s the input value correspond to a file name.
  #  @return The list of department capacity.
def readDeptCapacity(s):
    input_file = open(s, 'r')
    lines = input_file.readlines()
    dept_dict = {}
    dept = {}
    line = []
    for i in range(len(lines)):
        line.append(lines[i].split(','))
    for j in range(len(line)):
        dept_dict[line[j][0]] = line[j][1]
    return dept_dict
    
  ## @brief Calling the functions in this module in Main.
def main():
    readStdnts('s.txt')
    readFreeChoice('free_choice.txt')
    readDeptCapacity('departments.txt')


