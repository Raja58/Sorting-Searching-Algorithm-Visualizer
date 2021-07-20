# // <!--
# //  ============================
# //  @Author  :        Raja Durai M
# //  @Version :        1.0
# //  @Date    :        20 Jul 2021
# //  @Detail  :        Linear Search
# //  ============================
# //  -->

import time

def linear_search(data, search, drawData, timeTick):
    for i in range(len(data)):
        if(data[i]==search):
            color=[]
            for x in range(len(data)):
                if(x==i):
                    color.append('green')
                elif(x<i):
                    color.append('blue')
                else:
                    color.append('red')
            drawData(data, color)
            time.sleep(timeTick)
            for x in range(len(data)):
                if(x==i):
                    color[x]='green'
                else:
                    color[x]='red'
            drawData(data, color)
            time.sleep(timeTick)
            break
        else:
            drawData(data, ['blue' if x<=i else 'red' for x in range(len(data))] )
            time.sleep(timeTick)
    


