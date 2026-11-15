class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmax = 0
        rightmax = 0
        lrm = []
        llm = []
        water = 0


        for i in range(len(height)-1, -1, -1):
            if height[i] > rightmax:
                rightmax = height[i]
                lrm.append(height[i])
               
              
            elif height[i] <= rightmax:
                lrm.append(rightmax)

        lrm.reverse()
        
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
                llm.append(height[i])
            elif height[i] <= leftmax:
                llm.append(leftmax)

        for i in range(len(height)):
            if min(lrm[i], llm[i]) > height[i]:
                minheight = min(lrm[i], llm[i])
                water += minheight - height[i]

        return water



                


                
                    

        

                
