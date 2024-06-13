class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        int n = students.length;
        Arrays.sort(students);
        Arrays.sort(seats);
        int res = 0;
        for (int i = 0 ; i<n ; i++){
            res+=Math.abs(students[i]-seats[i]);
        }
        return res ;
        
    }
}