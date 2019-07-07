## @file testCalc.py
#  @author Zihao Chen
#  @brief A simple test method
#  @date 20/01/2019
import ReadAllocationData
import CalcModule

def test_sort(students):
    print ("***Testing sort function***")
    print ("Student list before sorting: ")
    print (students)
    print ("Student list after sorting: ")
    sort_list = CalcModule.sort(students)
    print (sort_list)

def test_average(students, gender):
    print ("***Testing average function***")
    avg = CalcModule.average(students, gender)
    print ("The average of " + str(gender) + " students is: " + str(avg))

def test_allocate(students, free_choice, dept):
    print ("***Testing allocate function***")
    allocate_list = CalcModule.allocate(students, free_choice, dept)
    print ("List after allocating: ")
    print (allocate_list)

    
def main():
    students = ReadAllocationData.readStdnts('s.txt')
    free_choice = ReadAllocationData.readFreeChoice('free_choice.txt')
    dept = ReadAllocationData.readDeptCapacity('departments.txt')
    
    test_sort(students)
    test_average(students, "Male")
    test_average(students, "Female")

    test_allocate(students, free_choice, dept)
        
        
