"""int=%d or %i
float=%f
"""
#~ is used to open/close terminal(ctrl+~)

a=5;b=6.9;c='heyy'
print(a)
print('%d' %a)
print('%i' %a)
print('%f' %a)
print('%.1f' %a)
print('%.2f' %a)
print('%.3f' %a)
print('%.4f' %a)
print('%.1f' %b)
print('%.2f' %b)

x='7'
y=int(x)
print(y)
a=float(x)
print(a)

g='6.9'
d=float(g)
print(g)
"""rules of variables
variables cannot start with a number and should not have space in between the variable
_ is the only character used in variables"""
"""isidentifier() is a method
help us to know the variable declared is valid or not"""
""" if a variable is correct the answer is True if it is wrong it is false"""
print('a'.isidentifier())
print('3zb'.isidentifier())
print('_ab'.isidentifier())
