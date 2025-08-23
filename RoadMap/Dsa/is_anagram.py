class isAnagram:
    def isAnagramFunc(s:str , t:str)->bool:
        if len(s)!=len(t):
            return False
     
        map:List[int]=[0]*26
        
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')]+=1
            hash[ord[t[i]]-ord('a')]-=1
        
        for val in hash:
            if val != 0:
                return False
        
        return True