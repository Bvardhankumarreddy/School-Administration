
#Project :- "School Administration Program"
#The Project will consist of the following milestones

#Entering or asking user to enter Student information.
#Pre-processing the collected data. ie. Converting the data into a different format that will be easier for us to process.
#Writing all the pre-processed data into a File.

#Student Information - Student_name,Age, Phno etc -> Vardhan, 21, 8919573936

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(info_list)

condition = True

while (condition):
    student_info = input("Enter student information in the following format (Name age contact_number Email_id):- ")
    
    print("Entered student information" +student_info)
    
    #split
    student_info_list = student_info.split(' ')
    print("Entered split up information is: " + str(student_info_list))
    
    condition_check = input("Enter (Yes/No) if you want enter the information of another student:- ")
    
    if (condition_check == "yes" or condition_check == "Yes" or condition_check == "YES"):
        condition = True
    elif (condition_check == "no" or condition_check == "No" or condition_check == "NO"):
        condition = False
