import matplotlib.pyplot as plt
import csv
import matplotlib

matplotlib.rcParams['font.family'] = 'Malgun Gothic'

student_dist_by_subject = "20231231.csv"

# 우선 큰 과목 영역(국수탐) 정하기
subject_areas = []

with open(student_dist_by_subject, mode='r', encoding='cp949') as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        if row[0] not in subject_areas:
            subject_areas.append(row[0])  


print("과목 영역:")
for idx, subject in enumerate(subject_areas, start=1):
    print(f"{idx}: {subject}")

while True:
    try:
        subject_area_choice = int(input("과목 영역에 해당하는 번호를 선택하세요: "))
        if 1 <= subject_area_choice <= len(subject_areas):
            selected_subject_area = subject_areas[subject_area_choice - 1]
            break
        else:
            print(f"1부터 {len(subject_areas)} 사이의 번호를 입력해주세요.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        
# 그 후, 과목 영역 중 자세한 과목 유형 선택하기
        
subject_types = []
        
with open(student_dist_by_subject, mode='r', encoding='cp949') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        if row[0] == selected_subject_area:
            if row[1] not in subject_types:
                subject_types.append(row[1])
                
print("과목 유형:")
for idx, subject in enumerate(subject_types, start=1):
    print(f"{idx}: {subject}")

while True:
    try:
        subject_type_choice = int(input("과목 유형에 해당하는 번호를 선택하세요: "))
        if 1 <= subject_type_choice <= len(subject_types):
            selected_subject_type = subject_types[subject_type_choice - 1]
            break
        else:
            print(f"1부터 {len(subject_areas)} 사이의 번호를 입력해주세요.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
                
                
# 그래프 출력하기

standard_scores = []
male_student_counts = []
female_student_counts = []

with open(student_dist_by_subject, mode='r', encoding='cp949') as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        if row[1] == selected_subject_type:
            standard_scores.append(int(row[2]))  
            male_student_counts.append(int(row[3]))        
            female_student_counts.append(int(row[4]))      


sorted_data = sorted(zip(standard_scores, male_student_counts, female_student_counts))
sorted_standard_scores, sorted_male_student_counts, sorted_female_student_counts = zip(*sorted_data)


plt.figure(figsize=(10, 6))

x_values = sorted_standard_scores
y_male = sorted_male_student_counts
y_female = sorted_female_student_counts

plt.plot(x_values, y_male, label='남자', color='royalblue', linestyle='-', linewidth=2)
plt.plot(x_values, y_female, label='여자', color='lightpink', linestyle='-', linewidth=2)

plt.title(f'2024학년도 수능 {selected_subject_type} 성적 분포')
plt.xlabel('표준점수')
plt.ylabel('학생 수')

plt.legend()
plt.show()