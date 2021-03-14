import os

print("LVM Automation using Python")
print("Developed by Shobhit Sharma")
print()
print("Please select an option")
lvm_option = int(input("""
0. List Available Disk(s)
1. List PV
2. Create PV
3. List VG
4. Create VG
5. List LV
6. Create LV
"""+"Select your option\n"))

print("You've selected: ",lvm_option)
print()
if lvm_option == 0:
  print("Listing all the disk(s)")
  os.system("fdisk -l")

if lvm_option == 1:
  print("Listing Current Physical Volumes")
  os.system("pvdisplay")

if lvm_option == 2:
  pass

if lvm_option == 3:
  print("Listing Current Volume Group(s)")
  os.system("vgdisplay")

if lvm_option == 4:
  pass

if lvm_option == 5:
  print("Listing Current Logical Volume(s)")
  os.system("lvdisplay")

if lvm_option == 6:
  pass
