public class RotateArrayByNinty {
    public void swap(int[][]matrix , int i , int j){
        
        matrix[i][j] = matrix[i][j]^matrix[j][i];
        matrix[j][i] = matrix[i][j]^matrix[j][i];
        matrix[i][j] = matrix[i][j]^matrix[j][i];
      
  }

  public void swap2(int[][]matrix , int i , int j){
      
        matrix[i][j] = matrix[i][j]^matrix[i][matrix.length-1-j];
        matrix[i][matrix.length-1-j] = matrix[i][j]^matrix[i][matrix.length-1-j];
        matrix[i][j] = matrix[i][j]^matrix[i][matrix.length-1-j];
      
  }


  public int[][] transpose(int[][] matrix){
   
   for(int i=0;i<matrix.length;i++){
      for(int j=0;j<i;j++){
          swap(matrix,i,j);
      }
   }
         return matrix;
  }
  public int[][] reverseRows(int[][] matrix){
      for(int i=0;i<matrix.length;i++){
          for(int j =0; j<(matrix.length>>1);j++){
             swap2(matrix,i,j);
          }
      }
      return matrix;
  }
  public void rotate(int[][] matrix) {
      transpose(matrix);
      reverseRows(matrix);
      System.out.println(matrix);
  }
}
