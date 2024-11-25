import java.util.*;

class DFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, List<Integer>> graph = new HashMap<>();

        System.out.println("Enter the number of nodes:");
        int nodes = sc.nextInt();

        System.out.println("Enter the adjacency list (e.g., '0 1 2' for node 0 with edges to 1 and 2):");
        for (int i = 0; i < nodes; i++) {
            int node = sc.nextInt();
            List<Integer> neighbors = new ArrayList<>();
            while (sc.hasNextInt()) {
                neighbors.add(sc.nextInt());
            }
            sc.nextLine(); // Clear the line
            graph.put(node, neighbors);
        }

        System.out.println("Enter the starting node for DFS:");
        int start = sc.nextInt();

        Set<Integer> visited = new HashSet<>();
        dfs(graph, start, visited);
    }

    public static void dfs(Map<Integer, List<Integer>> graph, int node, Set<Integer> visited) {
        if (visited.contains(node)) return;
        visited.add(node);
        System.out.print(node + " ");

        for (int neighbor : graph.getOrDefault(node, new ArrayList<>())) {
            dfs(graph, neighbor, visited);
        }
    }
}import java.util.*;

class BFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, List<Integer>> graph = new HashMap<>();

        System.out.println("Enter the number of nodes:");
        int nodes = sc.nextInt();

        System.out.println("Enter the adjacency list (e.g., '0 1 2' for node 0 with edges to 1 and 2):");
        for (int i = 0; i < nodes; i++) {
            int node = sc.nextInt();
            List<Integer> neighbors = new ArrayList<>();
            while (sc.hasNextInt()) {
                neighbors.add(sc.nextInt());
            }
            sc.nextLine(); // Clear the line
            graph.put(node, neighbors);
        }

        System.out.println("Enter the starting node for BFS:");
        int start = sc.nextInt();

        bfs(graph, start);
    }

    public static void bfs(Map<Integer, List<Integer>> graph, int start) {
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");

            for (int neighbor : graph.getOrDefault(node, new ArrayList<>())) {
                if (!visited.contains(neighbor)) {
                    queue.add(neighbor);
                    visited.add(neighbor);
                }
            }
        }
    }
}









int num = 4;
    boolean flag = false;
    if (num == 0 || num == 1) {flag = true;}
    for (int i = 2; i <= num / 2; ++i){
      if (num % i == 0) {
        flag = true; break;
      }}if (!flag)
      System.out.println(num + " is a prime number.");


hcf
for(int i = 1; i <= a || i <= b; i++) {
if( a%i == 0 && b%i == 0 )
hcf = i;}



lcm
while (n1 != n2) {
            if (n1 > n2) n1 -= n2;
            else n2 -= n1;}

fibo
if(n==0){
            System.out.println("0");
            }if(n==1) {
            System.out.println("0"+"1");}
        int n1=0;
        int n2=1;
        int n3;
        System.out.print("0"+" "+"1"+" ");
        n=n-2;
        while(n>0){n3=n2+n1;
            System.out.print(n3+" ");
            n1=n2;n2=n3;n--;}


selection sort

import java.util.Scanner;

class GfG {
    static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }
    }

    static void printArray(int[] arr) {
        for (int val : arr) System.out.print(val + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.print("Original array: ");
        printArray(arr);
        selectionSort(arr);
        System.out.print("Sorted array: ");
        printArray(arr);
    }
}



bubble sort


import java.util.Scanner;

class GFG {
    static void bubbleSort(int arr[], int n) {
        int i, j, temp;
        boolean swapped;
        for (i = 0; i < n - 1; i++) {
            swapped = false;
            for (j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
    }

    static void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++) System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        bubbleSort(arr, n);
        System.out.println("Sorted array:");
        printArray(arr, n);
    }
}



insertion sort


import java.util.Scanner;

public class InsertionSort {
    void sort(int arr[]) {
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }

    static void printArray(int arr[]) {
        for (int i = 0; i < arr.length; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        InsertionSort ob = new InsertionSort();
        ob.sort(arr);
        System.out.println("Sorted array:");
        printArray(arr);
    }
}


merge sort


import java.util.Scanner;

class GfG {
    static void merge(int arr[], int l, int m, int r) {
        int n1 = m - l + 1, n2 = r - m;
        int L[] = new int[n1], R[] = new int[n2];
        for (int i = 0; i < n1; ++i) L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j) R[j] = arr[m + 1 + j];
        int i = 0, j = 0, k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) arr[k++] = L[i++];
            else arr[k++] = R[j++];
        }
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }

    static void sort(int arr[], int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    static void printArray(int arr[]) {
        for (int i = 0; i < arr.length; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        sort(arr, 0, arr.length - 1);
        System.out.println("Sorted array:");
        printArray(arr);
    }
}




quick sort

import java.util.Scanner;

class GfG {
    static int partition(int[] arr, int low, int high) {
        int pivot = arr[high], i = low - 1;
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return i + 1;
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        quickSort(arr, 0, n - 1);
        System.out.println("Sorted array:");
        for (int val : arr) System.out.print(val + " ");
    }
}




strassens
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter matrix size (must be power of 2): ");
        int n = scanner.nextInt();
        int[][] A = new int[n][n];
        int[][] B = new int[n][n];
        System.out.println("Enter elements of matrix A:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = scanner.nextInt();}}
        System.out.println("Enter elements of matrix B:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                B[i][j] = scanner.nextInt();
            }}
        int[][] result = strassenMultiply(A, B);
        System.out.println("Result of Strassen's Multiplication:");
        for (int[] row : result) {
            for (int value : row) {
                System.out.print(value + " ");}
            System.out.println();}
        scanner.close();    }
    public static int[][] strassenMultiply(int[][] A, int[][] B) {
        int n = A.length;
        if (n == 1) {
            return new int[][]{{A[0][0] * B[0][0]}};
        }
        int newSize = n / 2;
        int[][] A11 = new int[newSize][newSize];
        int[][] A12 = new int[newSize][newSize];
        int[][] A21 = new int[newSize][newSize];
        int[][] A22 = new int[newSize][newSize];
        int[][] B11 = new int[newSize][newSize];
        int[][] B12 = new int[newSize][newSize];
        int[][] B21 = new int[newSize][newSize];
        int[][] B22 = new int[newSize][newSize];
        for (int i = 0; i < newSize; i++) {
            for (int j = 0; j < newSize; j++) {
                A11[i][j] = A[i][j];
                A12[i][j] = A[i][j + newSize];
                A21[i][j] = A[i + newSize][j];
                A22[i][j] = A[i + newSize][j + newSize];

                B11[i][j] = B[i][j];
                B12[i][j] = B[i][j + newSize];
                B21[i][j] = B[i + newSize][j];
                B22[i][j] = B[i + newSize][j + newSize];}}
        int[][] P1 = strassenMultiply(add(A11, A22), add(B11, B22));
        int[][] P2 = strassenMultiply(add(A21, A22), B11);
        int[][] P3 = strassenMultiply(A11, subtract(B12, B22));
        int[][] P4 = strassenMultiply(A22, subtract(B21, B11));
        int[][] P5 = strassenMultiply(add(A11, A12), B22);
        int[][] P6 = strassenMultiply(subtract(A21, A11), add(B11, B12));
        int[][] P7 = strassenMultiply(subtract(A12, A22), add(B21, B22));
        int[][] C11 = add(subtract(add(P1, P4), P5), P7);
        int[][] C12 = add(P3, P5);
        int[][] C21 = add(P2, P4);
        int[][] C22 = add(subtract(add(P1, P3), P2), P6);
        int[][] C = new int[n][n];
        for (int i = 0; i < newSize; i++) {
            for (int j = 0; j < newSize; j++) {
                C[i][j] = C11[i][j];
                C[i][j + newSize] = C12[i][j];
                C[i + newSize][j] = C21[i][j];
                C[i + newSize][j + newSize] = C22[i][j];}}
        return C;}
    public static int[][] add(int[][] A, int[][] B) {
        int n = A.length;
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = A[i][j] + B[i][j];
            }}return result;}
    public static int[][] subtract(int[][] A, int[][] B) {
        int n = A.length;
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = A[i][j] - B[i][j];
            }}return result;}}





0/1 knapsack
import java.util.Scanner;
class Knapsack{
    static int knapSack(int W,int wt[],int val[],int n){
        if(n==0||W==0)return 0;
        if(wt[n-1]>W)return knapSack(W,wt,val,n-1);
        else
            return Math.max(knapSack(W,wt,val,n-1),val[n-1]+knapSack(W-wt[n-1],wt,val,n-1));    }
    public static void main(String args[]){
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter the number of items: ");
        int n=scanner.nextInt();
        int[] profit=new int[n];
        int[] weight=new int[n];
        System.out.println("Enter the values (profits) of the items:");
        for(int i=0;i<n;i++){
            profit[i]=scanner.nextInt();        }
        System.out.println("Enter the weights of the items:");
        for(int i=0;i<n;i++){
            weight[i]=scanner.nextInt();}
        System.out.print("Enter the maximum capacity of knapsack: ");
        int W=scanner.nextInt();
        System.out.println("Maximum profit: "+knapSack(W,weight,profit,n));
        scanner.close();}}





jobsecduling using deadlines

import java.util.*;
class Job {char id;
    int deadline, profit;
    public Job(char id, int deadline, int profit) {
        this.id = id;this.deadline = deadline;
        this.profit = profit;}
    void printJobScheduling(ArrayList<Job> arr, int maxDeadline) {
        Collections.sort(arr, (a, b) -> b.profit - a.profit);
        boolean[] result = new boolean[maxDeadline];
        char[] job = new char[maxDeadline];
        for (Job j : arr) {
            for (int i = Math.min(maxDeadline - 1, j.deadline - 1); i >= 0; i--) {
      if (!result[i]) {result[i] = true;
       job[i] = j.id;break;}}}
        System.out.print("Scheduled Jobs: ");
        for (char jb : job) {
            if (jb != '\u0000') {
                System.out.print(jb + " ");}}
        System.out.println();}
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of jobs: ");
        int n = scanner.nextInt();
        ArrayList<Job> arr = new ArrayList<>();
        int maxDeadline = 0;
        for (int i = 0; i < n; i++){
System.out.print("Enter job id (single char),deadline,andprofit for job "+(i+1)+":");
            char id = scanner.next().charAt(0);
            int deadline = scanner.nextInt();
            int profit = scanner.nextInt();
            arr.add(new Job(id, deadline, profit));
            maxDeadline = Math.max(maxDeadline, deadline);}
        Job job = new Job(' ', 0, 0);
        job.printJobScheduling(arr, maxDeadline);
        scanner.close();}}



Dijkstras shortestp

import java.util.Scanner;

class ShortestPath {
    static final int V = 9;

    int minDistance(int dist[], Boolean sptSet[]) {
        int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 0; v < V; v++)
            if (!sptSet[v] && dist[v] <= min) {
                min = dist[v];
                min_index = v;
            }
        return min_index;
    }

    void printSolution(int dist[]) {
        System.out.println("Vertex\tDistance from Source");
        for (int i = 0; i < V; i++)
            System.out.println(i + "\t" + dist[i]);
    }

    void dijkstra(int graph[][], int src) {
        int dist[] = new int[V];
        Boolean sptSet[] = new Boolean[V];

        for (int i = 0; i < V; i++) {
            dist[i] = Integer.MAX_VALUE;
            sptSet[i] = false;
        }
        dist[src] = 0;

        for (int count = 0; count < V - 1; count++) {
            int u = minDistance(dist, sptSet);
            sptSet[u] = true;

            for (int v = 0; v < V; v++)
                if (!sptSet[v] && graph[u][v] != 0 && dist[u] != Integer.MAX_VALUE && dist[u] + graph[u][v] < dist[v])
                    dist[v] = dist[u] + graph[u][v];
        }
        printSolution(dist);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int graph[][] = new int[V][V];

        System.out.println("Enter the adjacency matrix for the graph (0 for no edge):");
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                graph[i][j] = scanner.nextInt();

        ShortestPath t = new ShortestPath();
        System.out.print("Enter the source vertex (0 to " + (V - 1) + "): ");
        int src = scanner.nextInt();
        t.dijkstra(graph, src);

        scanner.close();
    }
}



do using sum of subsets

import java.util.Scanner;

class SubsetSum {
    static boolean isSubsetSumRec(int[] arr, int n, int sum) {
        if (sum == 0) return true;
        if (n == 0) return false;
        if (arr[n - 1] > sum) return isSubsetSumRec(arr, n - 1, sum);
        return isSubsetSumRec(arr, n - 1, sum) || isSubsetSumRec(arr, n - 1, sum - arr[n - 1]);
    }

    static boolean isSubsetSum(int[] arr, int sum) {
        return isSubsetSumRec(arr, arr.length, sum);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) arr[i] = scanner.nextInt();
        System.out.print("Enter the sum to check: ");
        int sum = scanner.nextInt();

        if (isSubsetSum(arr, sum)) System.out.println("True");
        else System.out.println("False");
        
        scanner.close();
    }
}


bellman ford sssp

import java.util.*;

class BellmanFordAlgorithm {
    static int[] bellmanFord(int V, int[][] edges, int src) {
        int[] dist = new int[V];
        Arrays.fill(dist, (int)1e8);
        dist[src] = 0;

        for (int i = 0; i < V; i++) {
            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], wt = edge[2];
                if (dist[u] != 1e8 && dist[u] + wt < dist[v]) {
                    if (i == V - 1) return new int[]{-1};
                    dist[v] = dist[u] + wt;
                }
            }
        }
        return dist;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of vertices: ");
        int V = sc.nextInt();
        System.out.print("Enter the number of edges: ");
        int E = sc.nextInt();

        int[][] edges = new int[E][3];
        System.out.println("Enter the edges (source destination weight):");
        for (int i = 0; i < E; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        System.out.print("Enter the source vertex: ");
        int src = sc.nextInt();
        int[] ans = bellmanFord(V, edges, src);

        if (ans.length == 1 && ans[0] == -1) {
            System.out.println("Graph contains a negative weight cycle.");
        } else {
            System.out.println("Shortest distances from source vertex " + src + ":");
            for (int i = 0; i < ans.length; i++) {
                System.out.println("Vertex " + i + " : " + (ans[i] == (int)1e8 ? "Infinity" : ans[i]));
            }
        }
        sc.close();
    }
}
Enter the number of vertices: 6
Enter the number of edges: 4
Enter the edges (format: source destination weight): 
0 1 2
0 2 4
1 3 7
2 4 1
Enter the source vertex: 0


multistage graph

import java.util.*;

class MultistageGraph {
    static int N;
    static final int INF = Integer.MAX_VALUE;

    public static int shortestDist(int[][] graph) {
        int[] dist = new int[N];
        dist[N - 1] = 0;

        for (int i = N - 2; i >= 0; i--) {
            dist[i] = INF;
            for (int j = i; j < N; j++) {
                if (graph[i][j] != INF) {
                    dist[i] = Math.min(dist[i], graph[i][j] + dist[j]);
                }
            }
        }
        return dist[0];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of nodes in the graph: ");
        N = sc.nextInt();
        sc.nextLine(); // consume newline

        int[][] graph = new int[N][N];
        System.out.println("Enter the adjacency matrix (use 'INF' for no edge):");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                String input = sc.next();
                if (input.equalsIgnoreCase("INF")) {
                    graph[i][j] = INF;
                } else {
                    graph[i][j] = Integer.parseInt(input);
                }
            }
        }

        int result = shortestDist(graph);
        System.out.println("Shortest distance from node 0 to node " + (N - 1) + ": " + (result == INF ? "Infinity" : result));
        sc.close();
    }
}
Enter the number of nodes in the graph: 8
Enter the adjacency matrix (use 'INF' for no edge):
INF 1 2 5 INF INF INF INF
INF INF INF INF 4 11 INF INF
INF INF INF INF 9 5 16 INF
INF INF INF INF INF INF 2 INF
INF INF INF INF INF INF INF 18
INF INF INF INF INF INF INF 13
INF INF INF INF INF INF INF 2
INF INF INF INF INF INF INF INF



all pair shortest path

import java.util.*;

class AllPairShortestPath {
    static final int INF = 99999;

    void floydWarshall(int[][] dist, int V) {
        for (int k = 0; k < V; k++) {
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++) {
                    if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        printSolution(dist, V);
    }

    void printSolution(int[][] dist, int V) {
        System.out.println("The shortest distances between every pair of vertices:");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][j] == INF) {
                    System.out.print("INF ");
                } else {
                    System.out.print(dist[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of vertices: ");
        int V = sc.nextInt();

        int[][] graph = new int[V][V];
        System.out.println("Enter the adjacency matrix (use 'INF' for no edge):");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                String input = sc.next();
                if (input.equalsIgnoreCase("INF")) {
                    graph[i][j] = INF;
                } else {
                    graph[i][j] = Integer.parseInt(input);
                }
            }
        }

        AllPairShortestPath apsp = new AllPairShortestPath();
        apsp.floydWarshall(graph, V);

        sc.close();
    }
}
Enter the number of vertices: 4
Enter the adjacency matrix (use 'INF' for no edge):
0 5 INF 10
INF 0 3 INF
INF INF 0 1
INF INF INF 0

