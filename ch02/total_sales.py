def total_sales(*args):
   total = 0
   for arg in args:
       total = total + arg
   return total
print(total_sales(200,100,100,100))
print(total_sales(800,500,400))  



