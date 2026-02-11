marks={
    "Math": 95,
    "Science": 90,
    "English": 88,
    "History": 92
}

print(max(marks, key=marks.get))
print(min(marks, key=marks.get))
total_marks=sum(marks.values())
print("Total Marks:", total_marks)
average_marks=total_marks/len(marks)    
print("Average Marks:", average_marks)