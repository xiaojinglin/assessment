# Problem: You are given a list of zips and their contents, along with the size of each file within the zip.
# Each element in the list is a 3-tuple with the following format:
# (zip_name, pdf_name, pdf_size)

# The function generate_zip_data() below creates a randomized list of tuples and store it into an identifier called "data".

# Your task is to write an algorithm to produce the list of pdfs associated with the largest zip file.
# The output should simply be a list of pdfs. For example, if the initial list were the following:
# [(zip1.zip, file1.pdf, 10)
# , (zip1.zip, file2.pdf, 25)
# , (zip2.zip, fileA.pdf, 5)
# , (zip2.zip, fileB.pdf, 15)
# , (zip2.zip, fileC.pdf, 10)]

# The algorithm should return:
# [file1.pdf, file2.pdf]

# During the interview, we will focus on the following:
# - correctness: does it return the correct result?
# - efficiency: does it achive the reuslt efficiently? Be ready to talk through what improvements could be made. If You
# started with a brute force algorithm, but later improved it, please keep notes on that so we can discuss it.
# - readability: Is the code easy to read? Feel free to use helper functions if they will increase readability.

############################# Do not change the code in the box below ####################################
##########################################################################################################
from random import randint

def generate_zip_data():
    zip_data = []
    
    min_file_size = 100
    max_file_size = 1000
    
    min_num_zips = 10
    max_num_zips = 20
    
    min_files_per_zip = 30
    max_files_per_zip = 50
    
    num_zips = randint(min_num_zips, max_num_zips)
    for z in range(num_zips):
        num_files = randint(min_files_per_zip, max_files_per_zip)
        for f in range(num_files):
            zip_data.append(('zip_%s.zip' % z, 'z%s_file_%s.pdf' % (z, f), randint(min_file_size, max_file_size)))
    
    return zip_data

data = generate_zip_data()

############################################################################################################

########################################## Implement your algorithm here ###################################
def func(zip_data):
    '''
    This function uses a dictionary to store zip names and and zip sizes of the zip_data, 
    and get the zip name of the largest zip file and loop through the zip_data to get the 
    pdf files belong to the zip file. 
    The return value is:
    1. If there is only one largest zip file, the function will return a list of pdf names belong
    to the largest zip file.
    2. If there are more than one largest zip file, the function will return a dictionary
    with zip_name as the key, and a list of pdf files belong to the zip file as the value
    '''
    
    dict_zip = {}   #A dictionary to save the zip name and zip size
    
    for tup in zip_data:    #Loop through the zip_data to get the total size of each zip file, and save them in the dictionary
        zip_name = tup[0]
        pdf_size = tup[2]
        dict_zip[zip_name] = dict_zip.get(zip_name,0) + pdf_size  
                                                                                                                                 
    ###############################################
    #Python dictionary method get() returns a value for the given key. 
    # If key is not available then returns default value.
    #Syntax: dict.get(key, default = None)
    #Parameters
    #key: This is the Key to be searched in the dictionary.
    #default : This is the Value to be returned in case key does not exist.
    ###############################################
   
    list_zip_size = list(dict_zip.values())    #Get the values of all the zip size and save them in a list
    max_size = max(list_zip_size)       #Get the largest size of all the zip files
   
    max_zip_name = []       #A list to store the name of the largest zip file, in case there are more that one zip file having the same largest size
    for zip_name,zip_size in dict_zip.items(): #Loop through the dictionary to get the zip file name of the largest size
        if zip_size == max_size:
            max_zip_name.append(zip_name)
    
    ################################################
    #Another way to get the max_zip_name list: List comprehension which uses less code and run faster but is not as readable 
    #max_zip_name = [zip_name for zip_name,zip_size in dict_zip.items() if zip_size==max_size]
    #####################################################
   
    dict_file = {}   #A dictionary to store the largest zip name and its pdf names, the key of dictionary is zip name, value is a list of pdf names belong to the zip
    for m_zip in max_zip_name:
        list_pdf = [] #A list to store the pdf names
        for tup in zip_data:    #Loop through the zip_data to get the pdf name belongs to the zip file
            zip_name = tup[0]
            pdf_name = tup[1]
            if zip_name == m_zip:
                list_pdf.append(pdf_name)
        dict_file[m_zip] = list_pdf
    
    if len(max_zip_name) == 1:    #If there is only one largest zip file, return the list of the pdf names belongs to the largest zip file
        zip_name = max_zip_name[0]
        return dict_file[zip_name]
    else:   #If there are more that one largest zip file, return the dictionary with the zip name and pdf name
        return dict_file
        
print(func(data))
    
