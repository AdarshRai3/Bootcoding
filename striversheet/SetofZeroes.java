public class SetofZeroes {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length; //row length
        int n = matrix[0].length; //column length
 
 //Take intersection(0,0) as col0=1;     
      int col0=1;
    
 //Mark first row and column as zero
      for(int i =0;i<m;i++){
        for(int j=0;j<n;j++){
           if(matrix[i][j]==0){
             matrix[i][0]=0;
             if(j!=0){
               matrix[0][j]=0;
             }else{
               col0=0;
             }    
           }
        }
      }

 //Use the mark to set values as 0
 for(int i=1;i<m;i++){
  for(int j=1;j<n;j++){
    if(matrix[0][j]==0 || matrix[i][0]==0){
       matrix[i][j]=0;
    }
  }
 }

//Update the first row if needed
  if(matrix[0][0]==0){
    for(int j =0;j<n;j++){
       matrix[0][j]=0;
    }
  }

//Update the column if need 
  if(col==0){
   for(int i=0;i<m;i++){
      matrix[i][0]=0;
   }
  } 
   System.out.println(matrix);   
 }
}