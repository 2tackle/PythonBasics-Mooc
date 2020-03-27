#TempConvert.py
TempStr = input('please key in the temperature with unit:')
if TempStr[-1] in ['f' , 'F']:
	C = (eval(TempStr[0,-1]) - 32)/1.8
	print('converted value is {:.2f} '.format(C))
elif TempStr[-1] in ['c', 'C']:
	F = 1.8 * eval(TempStr[0,-1]) + 32
	print('converted value is {:.2f} '.format(F))
else:
	print('error')