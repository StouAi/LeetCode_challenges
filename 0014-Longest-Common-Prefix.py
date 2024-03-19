def longestCommonPrefix(strs):
   prefix = strs[0][0]
   for i in range(0,len(strs)):
       for j in range(0,len(strs[0])):
           if prefix!=strs[i][:j+1]:
               print(strs[i][0:j])
               return prefix
       prefix=prefix+strs[i][j]
if __name__ == '__main__':
    list = ["flower","flow","flight"]
    prefix = longestCommonPrefix(list)
    print(prefix)
