from python.objects.HardDisk import HardDisk

harddisk1=HardDisk()
list1=[]
for i in range(5):
    file_size1=int(input("enter file size: "))
    list1.append(file_size1)
    harddisk1.addfile(file_size1)

file_size=int(input("enter file size: "))
harddisk1.delfile(file_size)

harddisk1.show()