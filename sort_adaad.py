
array = []
tedad_daryaft_adad = int (input("tedad adad ha ro vared konid:\n"))

for i in range (0,tedad_daryaft_adad):
    adad = int (input("adad vared konid:\n"))
    array.append(adad)
arraye_sort = sorted(array)
if arraye_sort == array:
    print('(sort)')
else:
    print('(not sorted)','--and then sort: ',arraye_sort)
    

