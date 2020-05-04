def trapping_rain(buildings):
    water = 0
    for index in range(1,len(buildings)-1):
        left_up = max(buildings[:index])
        right_up = max(buildings[index+1:])
        min_val = min(left_up, right_up)
        water+= max(0, min_val - buildings[index])
    return water

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))


def trapping_rain(buildings):
    water =0
    height =0
    for i in range(len(buildings)-1):
        print("i번째는",i,"높이는",buildings[i],"height는",height)
        delete = 0
        if buildings[i] > height:
            height = buildings[i]
            second_height = 1
            
            for j in range(i+1,len(buildings)):
                print("지금 j는", j,"j의 높이는",buildings[j])
                # 같은 높이나, 더 높은 빌딩 나올 때
                if buildings[j] >= buildings[i]:
                    length = j-i-1                    
                    cal_height = height
                    break
                
                # 중간 높이 빌딩이 나올 때..
                if buildings[j] >= 1:
                    print("중간")
                    if second_height > buildings[j]:
                        second_height = buildings[j]
                    
                    if second_height < buildings[j]:
                        delete += buildings[j] # 중간 높이 빼주자
                    print("delete",delete)
                    length = j-i-1 # length는 개선
                    cal_height = second_height
                
                # 아무것도 안나와 (물 찰 공간 없음)
                else:
                    pass
                    
            pour = cal_height * length
            print("더 들어갈 물",pour,"-", delete)
            water += (pour - delete)
            print("현재 물의 양은",water)
    return water

print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
