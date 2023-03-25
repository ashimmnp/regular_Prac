import java.util.*;//importing util from java
public class MergeSort_np03cs4a220208 {
    //For input
    ArrayList getInput(ArrayList<Integer> al) {
        Scanner in = new Scanner(System.in);//Adding the scanner for user input 
        System.out.print("Enter the number of lenght for array list:");
        int l = in.nextInt();//user selects the length for array list
        //Creating the loop for user input array elements
        for (int i=0; i<l; i++){ 
            System.out.print("Enter Array's element:");
            int ele = in.nextInt();
            //user input value for elements
            al.add(i,ele);//input is added to al
        }
        return al; 
        //returns al
    }
    //For Output
    void getOutput(ArrayList<Integer> al) {
        System.out.println("Sorted Array list is: ");
        //Prints the final value of sorted array
        System.out.println(al); 
    }
    
    void merge(ArrayList<Integer> al, int beg, int mid, int end) {
        int p = beg, q = beg , r =mid+1 ;
        //Creating one array to include the elements from array list.
        ArrayList<Integer> ary = new ArrayList<Integer>();
        ary.addAll(al);// includes list values to array ary
        
        while ( q <= mid && r<=end){
            //Comparing array list to get the greatest array number 
            if(al.get(q) < al.get(r)){
                ary.add(p++, al.get(q++));
            }
            //Sorted numbers are stored in temporary ary array.
            else {
                ary.add(p++, al.get(r++));
            }
        }
        //Remaining elements are at another side
        for (;q<=mid; q++){
            ary.add(p++, al.get(q));
        }
        // Copies the remaining array elements from one side.
        for(;r<=end; r++){
            ary.add(p++,al.get(r));
        }
        // Copies the remaining elements from another side.
        for (q=beg; q<=end; q++){
            al.set(q,ary.get(q));
        }
    }
    
    void sort(ArrayList<Integer> al, int beg, int end) {
        int li = beg;
        int hi = end-1;
        MergeSort_np03cs4a220208 firstlist = new MergeSort_np03cs4a220208();
        //Creating loop to divide the array list
        for (int m = 1; m<= hi -li ; m = m*2){
            
            //Creating loop to split elements in array
            for (int d = li ; d < hi; d+= m*2){
                int strt = d; 
                //finding mid value from divided array list also the min value in array
                int mid = d + m -1;
                int last = Integer.min(d + m * 2 -1 , hi);
                //Calling the function to merge the divided array list in sorted form
                firstlist.merge(al, strt , mid ,last);
                
            }
        }
    }
    //static class of the program
    public static void main(String[] args) { 
     MergeSort_np03cs4a220208 firstlist = new MergeSort_np03cs4a220208();
     //Creating the new array list
     ArrayList<Integer> arrayele = new ArrayList<Integer>();
     //calls getinput method retriving input and stores the returned value to arrayele.
     arrayele= firstlist.getInput(arrayele);
     System.out.println("Initial Array List: ");
     System.out.println(arrayele);
     //Using sort method to order array list, first is array list and second is its length. 
     firstlist.sort(arrayele,0,arrayele.size());
     //Prints the final result calling getoutput metyod  
     firstlist.getOutput(arrayele); 
    }
}
/*End of Merge-sort program.. */ 
