import math

def MidCrossCompare(Arr,mid,low,high):
    sum_left=-(math.inf)
    sum=0
    for i in range(mid,low-1,-1):
        sum=sum + Arr[i]
        if sum>sum_left:
            sum_left=sum
            max_left=i
    sum=0
    sum_right=-(math.inf)
    for i in range(mid+1,high+1):
        sum=sum+Arr[i]
        if sum>sum_right:
            sum_right=sum
            max_right=i
    return (max_left,max_right,sum_right+sum_left)


def Find_Maximum_subarray(Arr,low,high):
    if low==high:
        return (low,high,Arr[low])
    else:
        mid=int(((low+high)/2)-1)
        left_high, left_low, left_sum = Find_Maximum_subarray(Arr, low, mid)
        right_high,right_low,right_sum=Find_Maximum_subarray(Arr,mid+1,high-1)
        cross_high, cross_low, cross_sum = MidCrossCompare(Arr, mid, low,high)

        if right_sum>left_sum and right_sum>cross_sum:
            return (right_low,right_high,right_sum)
        if left_sum>right_sum and left_sum>cross_sum:
            return (left_low,left_high,left_sum)
        else:
            return (cross_low,cross_high,cross_sum)

Find_Maximum_subarray([2,-4,32,-33,43,4,-3,2,-45,34,-5,32,34,44,-4,-54,33,57,87,-4,-86],0,20)