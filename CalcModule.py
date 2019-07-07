## @file CalcModule.py
#  @author Zihao Chen
#  @brief Provides the calculation on the list using ReadAllocationData
#  @date 18/01/2019

import ReadAllocationData 
from operator import itemgetter

  ## @brief Take a input txt file and return the list of student sorted by GPA.
  #  @param S the input value correspond to a file name.
  #  @return The sorted list of the students.
def sort(S):
    sort_list = sorted(S, key=lambda k: k['gpa']) 
    return sort_list
	
	
	
  ## @brief Take a input txt file and return the list of student sorted by GPA.
  #  @param L the list of ditionaries of students.
  #  @param g a string that represented male or female.
  #  @return The average gpa of selected gender.
def average(L,g):
    s = 0.0
    count = 0
    for i in range(len(L)):
        if L[i]['gender'] == g:
            count = count + 1
            s+=float(L[i]['gpa'])
    print (s/count)
	
	
  ## @brief Take a input txt file and return the list of student sorted by GPA.
  #  @param S the list of ditionaries of students.
  #  @param F a list of students with free choice.
  #  @param C a dictionary of department capcacities
  #  @return A dictionary of allocated student.    
def allocate(S,F,C):
    
    sorted_list = sort(S) 
    sorted_list.reverse() 
  
    mech_count = 0
    engphys_count = 0
    mat_count = 0
    soft_count = 0
    elec_count = 0
    chem_count = 0
    civ_count = 0

    
    mech_max_count = float(C['mechanical'])
    engphys_max_count = float(C['engphys'])
    mat_max_count = float(C['Materials'])
    soft_max_count = float(C['software'])
    elec_max_count = float(C['electrical'])
    chem_max_count = float(C['chemical'])
    civ_max_count = float(C['civil'])

   
    soft_list = []
    mech_list = []
    mat_list = []
    civ_list = []
    engphys_list = []
    elec_list = []
    chem_list = []
    s_list = []
    
    for free in F:
        for i in range(len(S)):
            if S[i]['macid'] == free:
                for j in range(3):
                    
                    if S[i]['choices'][j] == 'software' and soft_count!=soft_max_count and free not in s_list:
                        soft_count+=1
                        soft_list.append(free)
                        s_list.append(free)
                    if S[i]['choices'][j] == 'mechanical' and mech_count!=mech_max_count and free not in s_list:
                        mech_count+=1
                        mech_list.append(free)
                        s_list.append(free)
                    if S[i]['choices'][j] == 'Materials' and mat_count!=mat_max_count and free not in s_list:
                        mat_count+=1
                        mat_list.append(free)
                        s_list.append(free)
                    if S[i]['choices'][j] == 'civil' and civ_count!=civ_max_count and free not in s_list:
                        civ_count+=1
                        civ_list.append(free)
                        s_list.append(free)
                    if S[i]['choices'][j] == 'engphys' and engphys_count!=engphys_max_count and free not in s_list:
                        engphys_count+=1
                        engphys_list.append(free)
                        s_list.append(free)
                    if S[i]['choices'][j] == 'chemical' and chem_count!=chem_max_count and free not in s_list:
                        chem_count+=1
                        chem_list.append(free)
                        s_list.append(free)
                    if S[i]['choices'][j] == 'electrical' and elec_count!=elec_max_count and free not in s_list:
                        elec_count+=1
                        elec_list.append(free)
                        s_list.append(free)
    
    for k in range(len(S)):
        if S[k]['macid'] not in s_list:
            for j in range(3):
                    if S[k]['choices'][j] == 'software' and soft_count!=soft_max_count and S[k]['gpa'] > 4.0:
                        soft_count+=1
                        soft_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
                    if S[k]['choices'][j] == 'mechanical' and mech_count!=mech_max_count and S[k]['gpa'] > 4.0:
                        mech_count+=1
                        mech_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
                    if S[k]['choices'][j] == 'Materials' and mat_count!=mat_max_count and S[k]['gpa'] > 4.0:
                        mat_count+=1
                        mat_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
                    if S[k]['choices'][j] == 'civil' and civ_count!=civ_max_count and S[k]['gpa'] > 4.0:
                        civ_count+=1
                        civ_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
                    if S[k]['choices'][j] == 'engphys' and engphys_count!=engphys_max_count and S[k]['gpa'] > 4.0:
                        engphys_count+=1
                        engphys_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
                    if S[k]['choices'][j] == 'chemical' and chem_count!=chem_max_count and S[k]['gpa'] > 4.0:
                        chem_count+=1
                        chem_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
                    if S[k]['choices'][j] == 'electrical' and elec_count!=elec_max_count and S[k]['gpa'] > 4.0:
                        elec_count+=1
                        elec_list.append(S[k]['macid'])
                        s_list.append(S[k]['macid'])
    allocate_dic = {}
    allocate_dic['civil'] = civ_list
    allocate_dic['mechanical'] = mech_list
    allocate_dic['electrical'] = elec_list
    allocate_dic['software'] = soft_list
    allocate_dic['materials'] = mat_list
    allocate_dic['engphys'] = engphys_list
    allocate_dic['chemical'] = chem_list
    return allocate_dic                        
	
	
  ## @brief Calling the functions in this module in Main.    
def main():
    student_dic = ReadAllocationData.readStdnts('s.txt')
    free_choice_dic = ReadAllocationData.readFreeChoice('free_choice.txt')
    dept_dic = ReadAllocationData.readDeptCapacity('departments.txt')
    average(student_dic, 'Male')
    allocate(student_dic, free_choice_dic, dept_dic)
