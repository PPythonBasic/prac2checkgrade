"""
	ออกแบบโปรแกรมคำนวณเกรด โดยรับข้อมูลจากผู้ใช้งานเข้ามา หรือ input โดยมีเงื่อนไขดังนี้

	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 80 และ ไม่เกิน 100 แสดงผล Grade A
	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 75 และ ไม่เกิน 79 แสดงผล Grade B+
	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 70 และ ไม่เกิน 74 แสดงผล Grade B
	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 65 และ ไม่เกิน 69 แสดงผล Grade C+
	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 60 และ ไม่เกิน 64 แสดงผล Grade C
	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 55 และ ไม่เกิน 59 แสดงผล Grade D+
	-	ถ้าคะแนนมากกว่าหรือเท่ากับ 50 และ ไม่เกิน 54 แสดงผล Grade D
	-	ถ้าน้อยกว่า 50 แสดงผล Grade F

"""

score =  int(input("Enter number : "))

if score >= 80 and score <= 100:
  print("A")
elif score >= 75 and score <= 79:
  print("B+") 
elif score >= 70 and score <= 74:
  print("B") 
elif score >= 65 and score <= 69:
  print("C+") 
elif score >= 60 and score <= 64:
  print("C")
elif score >= 55 and score <= 59:
  print("D+") 
elif score >= 50 and score <= 54:
  print("D") 
else:
  print("F")