# Encapsulation

# Problem-1

class Order:
    def __init__(self,customer_name,items,total_amount,discount):
        self.customer_name = customer_name  #public
        self.items=items                    #public
        self.__total_amount=total_amount    #private
        self.__discount = discount          #private

    def __calculate_final_amount(self):   #private method
        return self.__total_amount - self.__discount

    def _get_admin_view(self):   #protect method
        return {
            "Customer":self.customer_name,
            "Items":self.items,
            "Total amount":f"{self.__total_amount}",
            "Discount Applied": f"{self.__discount}",
            "Final Bill" : f"{self.__calculate_final_amount()}"
        }

    def customer_view(self):   # public method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Final Bill": f"{self.__calculate_final_amount()}"

        }


class AdminPortal:
    def show_order(self,order):
        return order._get_admin_view()  # Allowed  this method but protected
class CustomerPortal:
    def show_order(self,order):
        return order.customer_view()    #Safe public method


order=Order("Jerry",["Biryani","Parotta"],700,120)
admin=AdminPortal()
customer=CustomerPortal()

print("\n Admin View :-")
print(admin.show_order(order))

print("\n Customer view:-")
print(customer.show_order(order))

# My TASK

class Assignment:
    def __init__(self,student_name,subjects,total_marks,bonus_mark):
        self.student_name = student_name   #public
        self.subjects = subjects           #public
        self.__total_marks = total_marks   #private
        self.__bonus_mark = bonus_mark     #private

    def __calculate_total_mark(self):  # private method
        return self.__total_marks + self.__bonus_mark

    def _get_teacher_view(self):   # Allowed this method but protected.
        return {
            "Student name":self.student_name,
            "Subjects" :self.subjects,
            "Total marks" : f"{self.__total_marks}",
            "Bonus mark" : f"{self.__bonus_mark}",
            "Final Total marks" : f"{self.__calculate_total_mark()}"
        }

    def student_view(self):
        return {
            "Student name": self.student_name,
            "Subjects": self.subjects,
            "Final Total marks": f"{self.__calculate_total_mark()}"

        }

class teacherPortal:
    def show_mark_view(self,Assignment):
        return Assignment._get_teacher_view()
class studentPortal:
    def show_mark_view(self,Assignment):
        return Assignment.student_view()

assign = Assignment("Jerry",["Maths","Science"],180,15)



teacher = teacherPortal()
student = studentPortal()


print("\n Teacher view the mark:-")
print(teacher.show_mark_view(assign))

print("\n Student view the mark:-")
print(student.show_mark_view(assign))




