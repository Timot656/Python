#Get rid of the duplicates
student_data = {'id1':{'name':['Sara'], 'class':['V'], 'subject_integration':['English,math,science']}
                'id2':{'name':['David'], 'class':['V'], 'subject_integration':['English,math,science']}
                'id3':{'name':['Tim'], 'class':['V'], 'subject_integration':['English,math,science']}}

result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
    print(result)