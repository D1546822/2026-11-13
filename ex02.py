
# 原始成績表
table = {
    "dept": ["AITA", "CSIE", "AITA", "CSIE", "AITA"],
    "ch": [95, 85, 96, 70, 88],
    "math": [65, 72, 83, 91, 60],
    "python": [90, 83, 75, 94, 79]
}

# 建立學生字典
students = {}

for i in range(5):
    students[i+1] = {
        "id": "d" + str(10+i),
        "dept": table["dept"][i],
        "ch": table["ch"][i],
        "math": table["math"][i],
        "python": table["python"][i]
    }

# 計算每位學生平均
for i in students:
    avg = (students[i]["ch"] +
           students[i]["math"] +
           students[i]["python"]) / 3

    students[i]["avg"] = round(avg, 2)

# 印出 students[1] 
print("students[1] =", students[1])

# 印出每位學生的學號、科系、平均
print("\n學生平均成績")

for i in students:
    print(
        students[i]["id"],
        students[i]["dept"],
        students[i]["avg"]
    )

# 建立科系統計資料
dept_data = {
    "AITA": {"count": 0, "total": 0},
    "CSIE": {"count": 0, "total": 0}
}

# 統計各科系人數及平均總和
for i in students:
    dept = students[i]["dept"]

    dept_data[dept]["count"] += 1
    dept_data[dept]["total"] += students[i]["avg"]

# 計算各科系平均
print("\n科系統計")

for dept in dept_data:
    avg = dept_data[dept]["total"] / dept_data[dept]["count"]

    dept_data[dept]["avg"] = round(avg, 2)

    print(
        dept,
        "人數：", dept_data[dept]["count"],
        "平均：", dept_data[dept]["avg"]
    )

# 找出平均最高的科系（不使用 max）
top_dept = ""

for dept in dept_data:
    if top_dept == "":
        top_dept = dept
    elif dept_data[dept]["avg"] > dept_data[top_dept]["avg"]:
        top_dept = dept

print("\n平均最高的科系：", top_dept)
