class Search:
    def search(self,string,alphabet):
        x=0
        while x<len(alphabet)  and len(string)>0 :
            
            if str(alphabet[x])==str(string[0]):
                string.pop(0)
                if len(alphabet)>1:
                    x=0
            else:
                x+=1
        return string
