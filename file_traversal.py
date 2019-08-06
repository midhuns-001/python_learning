import os

def traverse_dir(path):
    for r, d, f in os.walk(path):
        for files in f:
                        
            stat_info = os.stat(os.path.join(r,files))
            file[os.path.join(r,files)] = stat_info
            '''
            if not os.path.islink(os.path.join(r,files)):
                size+=os.path.getsize(os.path.join(r,files))
            '''
    print (file)     
    print ("*"*300)
    
def getTotalNoOfFiles(path, file):
    print ("Total no of files present in the folder '{0}'             = {1}".format(path, len(file)) + '\n\n')

def getTotalFileSize(path, file):
    t_size = 0
    for f in file.keys():
        t_size += os.path.getsize(f)
    t_size = t_size/1024
    print ("Total file size of folder '{0}'                         = {1}".format(path, str(t_size)+' KB') + '\n\n')
    
def getLargestFile(path, file):
    
    files = sorted(file.keys(), key=os.path.getsize, reverse=True)
    print ("Files: ", files)
    print ("Largest File/s: ", files[0])
    largest_file_size = os.path.getsize(files[0])
    
    for f in range (1, len(files)-1):
        if os.path.getsize(files[f]) ==  largest_file_size:
            print ('\t', files[f])

def getOldestFile(path, file):

    files = sorted(file.keys(), key=os.path.getctime)
    print("Files: ", files)
    oldest_file = os.path.getmtime(files[0])
    
    print ("Oldest file/s: ", files[0])
    for f in range (1, len(files)-1):
        if os.path.getmtime(files[f]) == oldest_file:
            print ('\t', files[f])
      
'''      
def get_duplicate_file_by_name(path, file):
    
    all_files = {}
    dup_files = {}
    for f in file.keys():
        file_name = os.path.basename(f)
        if file_name in dup_files.keys():
            dup_files[file_name] += 1
        else:
            dup_files[file_name] = 1
        dup_files['path'] = f
    
        all_files.update({'result':dup_files})
    
    #files = sorted(dup_files.items(), key=lambda item: item[1])
    print (all_files)
'''
'''  
{'result': {'decorator1.file1': 1, 'path': '/Users/msreekum/Pgms/python/dir2/dir3/e', 'f': 1, 'hai.txt': 1,
             'decorator3.file1': 1, 'd': 1, 'e': 2, 'a.txt': 1, 'str.file1': 1, 'dict1.file1': 1, 'midhun.file1': 1, 'validate.file1': 1, 'today.file1': 1, 
             'dict2.file1': 1, 'divit.file1': 1, 'rajani.file1': 1, 'file2.file1': 1, 'file.file1': 1, 'midhun.txt': 1}}
'''
    
def get_most_recently_modified_files(path, file):
    files = sorted(file.keys(), key=os.path.getmtime, reverse=True)
    print (files[:5])
    
    
def get_files_created_in_one_week(path, file, days=7):
    from datetime import datetime, timedelta
    files = sorted(file.keys(), key=os.path.getctime)
    now = datetime.now()
    print ("Crrent date & time: ", now)
    start_date = now - timedelta(days=days)
    print ("Start date : ", start_date)
    print("Files created in last {0} days : ".format(days))
    for f in files:
        t  = os.path.getctime(f)
        date_to_verify = datetime.fromtimestamp(t)

        if date_to_verify > start_date:
            print (f )

path = "/Users/msreekum/Pgms/python/dir2/dir4/dir5"
file = {}

traverse_dir(path)

'''
Attributes to read for each file
    1. File path
    2. File Name
    3. Creation time
    4. Size in kb
    5. Modified time
    
'''
'''
    1. Get total no of files in the folder

'''
getTotalNoOfFiles(path, file)
'''
    2. Total of the file size in the folder

'''
#getTotalFileSize(path, file)

'''

    3. Largest file/s present in any folder
'''
#getLargestFile(path, file)
'''
    4. Oldest created file 
'''
#getOldestFile(path, file)

'''
    5. All duplicate files
'''
#TODO
#get_duplicate_file_by_name(path, file)
'''
    6. 5 most recently modified files in sorted order according to modified time (descending)
    
'''
#get_most_recently_modified_files(path, file)

'''
    7. Files created in last 1 week

'''
get_files_created_in_one_week(path, file)
