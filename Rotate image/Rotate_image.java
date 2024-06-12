class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        for (int i = 0; i < n; ++i) {
            reverseRow(matrix[i]);
        }
    }
    
    private void reverseRow(int[] row) {
        int m = row.length;
        for (int j = 0; j < m / 2; ++j) {
            int temp = row[j];
            row[j] = row[m - j - 1];
            row[m - j - 1] = temp;
        }
    }
}