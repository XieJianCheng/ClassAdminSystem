import os
work = f'{os.getcwd()}'
work_dir = f'{work}\\Data'
work_file1 = f'{work}\\Data\\UserList.txt'
work_file2 = f'{work}\\Data\\StudentList.txt'
work_file3 = f'{work}\\Data\\StudentInformation.txt'
if not os.path.exists(work_dir):
    os.makedirs(f'{os.getcwd()}\\Data\\')
    with open(work_file1, 'a+') as fo1:
        pass
    with open(work_file2, 'a+') as fo2:
        pass
    with open(work_file3, 'a+') as fo3:
        pass
