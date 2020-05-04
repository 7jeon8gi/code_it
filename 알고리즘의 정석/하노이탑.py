def move_disk(disk_num, start_peg, end_peg): #원판번호,시작,끝
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg): #원판수,시작,끝
    if num_disks ==0:
        return
    
    elif num_disks ==1:
        move_disk(num_disks, start_peg, end_peg) #BASE CASE
    
    else:
        hanoi(num_disks-1, start_peg, end_peg=6-start_peg-end_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks-1, 6-start_peg-end_peg , end_peg)
        

hanoi(3,1,3)
