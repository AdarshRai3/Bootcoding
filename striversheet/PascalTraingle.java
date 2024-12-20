public class PascalTraingle {
    public List<List<Integer>> generate(int numRows) {
        //Initialise 2D list as return type
        List<List<Integer>> ans = new ArrayList<>();
        
        if(numRows<=0){
            return ans;
        }

        //as we know first element of ans list is 1 that means i,j =0,0 is 1
        ans.add(Arrays.asList(1));
        
        //currently we have {{1}} in the ans arraylist 
        for(int i =1;i<numRows;i++){
           // prev row that we need to find the current row in pascal traingle
           // prev row is intislialised with ans.get(i-1); 
           List<Integer>prev = ans.get(i-1);

           //this is the current row which we want to add values
           List<Integer>curr = new ArrayList<>();
           
           // we know that the first and last value of every row of pascal traingle is 1
           curr.add(1);

           //this for loop starts from 1 to i since pascal triangle the number of elements in a row is equal to number of columns in a row 
           // In this we have sum which is equal to sum = prev.get(j-1) + pre.get(j);
           // then add that sum to the curr
           //Suppose we have prev{1,3,3,1}
           // now in curr we have 1+3 = 4 , 3+3 = 6 , 3+1=4 
           // then we have to add them in curr we will get {1,4,6,4}
           for(int j=1;j<i;j++){
             int sum = prev.get(j-1)+prev.get(j);
             curr.add(sum);
           }

           //currently we have {1,4,6,4} we know Pascal traingle also ends up with 1
           // therefore we have to curr.add(1) so we get {1,4,6,4,1}
           curr.add(1);

           //then we will add curr to ans 
           ans.add(curr);
        }
        
         
         return ans;

    }
}