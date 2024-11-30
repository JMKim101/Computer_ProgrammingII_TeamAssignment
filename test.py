import matplotlib.pyplot as plt
import csv
import matplotlib


matplotlib.rcParams['font.family'] = 'Malgun Gothic'

data = r"C:\Users\uniba\Downloads\과제 6. 팀프로젝트\20231231.csv"

available_subjects = []

with open(data, mode='r', encoding='cp949') as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        if row[0] not in available_subjects:
            available_subjects.append(row[0])  


print("과목:")
for idx, subject in enumerate(available_subjects, start=1):
    print(f"{idx}: {subject}")

while True:
    try:
        subject_choice = int(input("과목 번호를 선택하세요: "))
        if 1 <= subject_choice <= len(available_subjects):
            selected_subject = available_subjects[subject_choice - 1]
            break
        else:
            print(f"1부터 {len(available_subjects)} 사이의 번호를 입력해주세요.")
    except ValueError:
        print("올바른 숫자를 입력해주세요.")

standard_scores = []
male_num = []
female_num = []

with open(data, mode='r', encoding='cp949') as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        if row[0] == selected_subject:
            standard_scores.append(int(row[2]))  
            male_num.append(int(row[3]))        
            female_num.append(int(row[4]))      


sorted_data = sorted(zip(standard_scores, male_num, female_num))
sorted_standard_scores, sorted_male_scores, sorted_female_scores = zip(*sorted_data)


plt.figure(figsize=(10, 6))

plt.plot(sorted_standard_scores, sorted_male_scores, label='남자', color='blue', linestyle='-', linewidth=2)
plt.plot(sorted_standard_scores, sorted_female_scores, label='여자', color='pink', linestyle='-', linewidth=2)

plt.title(f'2024학년도 수능 {selected_subject} 성적 분포')
plt.xlabel('표준점수')
plt.ylabel('학생 수')

plt.legend()
plt.show()







