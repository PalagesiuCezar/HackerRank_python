

def avg(nrs):
    s = 0
    for i in range(0,len(nrs)):
        s += nrs[i]
    return s/len(nrs)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
