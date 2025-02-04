public class Solution36 {
    public boolean isValidSudoku(char[][] board) {
        //Since it is given the suduko will be always be of (9x9)
        int N = 9;

        //Since the condition demands there has to be no duplicaton of elements in the rows,cols and boxes of the suduko 
        //We know that we need to check the duplication we need to check duplication we need hashSet 
        //We need Array of Character HashSet of Size = N in this case
        HashSet<Character> rows [] =  new HashSet[N];
        HashSet<Character> cols [] =  new HashSet[N];
        HashSet<CHaracter> boxes [] = new HashSet[N];
        
        //for each rows , cols and boxes we have proper hashSet to check the duplication
        for(int i =0;i<N;i++){
            rows[i] = new HashSet<Character>();
            cols[i] = new HashSet<Character>();
            boxes[i] = new HashSet<Character>();
        }
        
        //For checking each position we have traverse through the loop therefore we have to iterate over the rows , cols and boxes
        for(int r = 0;r<N;r++){
            for( int c=0;c<N;c++){
               
                //First thing we do is store the value of the string present at the board[r][c] of the matrix in the variable
                Character val = board[r][c];
                if(val == '.'){
                    continue;
                }    

                //Now we have to check the duplication in the rows , cols and boxes
                if(rows[i].contains(val)){
                    return false;
                }
                  rows[i].add(val);

                if(cols[i].contains(val)){
                    return false;
                }
                  cols[i].add(val);
                  
                  // To check in the boxes we need an index and for that we need to find the index of the box in which the element is present 
                  // For that we have to derive a formula 
                  int idx = r/3*3 + c/3;

                if(boxes[idx].contains(val)){
                    return false;
                }
                  boxes[idx].add(val);

            } 
        }
        //After the iteration if we dont find duplication of element we simply return true.
        return true;
    }
}
//Time Complexity : O(N^2)
//Space Complexity : O(3N)->O(N)->O(1)(if the matrix will always be of (9x9)); 
// -------------------------------------------------------------------------
// More Optimised Approach
