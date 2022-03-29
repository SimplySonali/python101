#Find the nth highest and nth lowest numbers in a list
#Find the frequency of each element in a list
#Sort a given list
#Remove duplicate elements from an array
li = [31,2,34,4,34,2,6,5,21,34,34,34,6,5,35,12,6,1,10,34,21]
#li = [1,1,1,2,2,0,-5,-1,3]
#li = ['cat','dog','cow']

def nth (li,h,l) :
#Sorting the array in descending order
   for i in range(1,len(li)) :
       for j in range(i) :
           if li[i] > li[j] :
              li[i],li[j] = li[j],li[i]
   print('The sorted array is {}'.format(li))
   #Creating a new list newli to sort unique values of the list. We will use this list to find the h (highest) and l(lowest)
   newli = []
   #Creating a new dictionary D to store the frequency of occurence of each element in the list
   D = {}
   cnt = 0
   for i in range(0,len(li)) :
       if li[i] not in newli :
          newli.append(li[i])
          cnt = 1
          counted = li[i]
       elif li[i] == counted :
           cnt += 1
       D[li[i]] = cnt
   print ('The sorted array with distinct element is {}'.format(newli))
   if h > len(newli)-1 :
       print ('The {} highest element doesnot exist'.format(h))
   else :
      print ('The {} highest element is {}'.format(h,newli[h-1]))
   if l > len(newli)-1 :
       print('The {} lowest element doesnot exist'.format(l))
   else :
       print ('The {} lowest element is {}'.format(l,newli[len(newli)-l]))
   print ('The dictionary is {}'.format(D))

   # Pass the list, h highest and l lowest elements. @nd highest and 5th lowest
nth (li,2,5)
