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
