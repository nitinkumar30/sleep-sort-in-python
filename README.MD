# The Sleep sort algorithm

> - [Sleep sort algorithm](https://www.quora.com/What-is-sleep-sort) implemented in Python  
> - It is currently not implemented in Python language as per my knowledge  
> - Sleep algorithm basically works on sleeping system for a particular time & waking it up  
> - This sorting algorithm is a perfect demonstration of multi-threading and scheduling done by OS.  
> - The phrase “Sorting while Sleeping” itself sounds very unique. Overall it is a fun, lazy, weird algorithm. But as rightly said by someone- “If it works then it is not lazy”.


# What interested me most in this?

> 1. "Sleep" sort algorithm, I was thinking of some algorithm to work on.  
> 2. Sleep sort is a joke sorting algorithm that became popular on the 4chan, the same place where world's dangerous hacker group originated.  
> 3. Complexity is not defined in constants. Time complexity is ```O(n^2 + max(args))``` as per the info I got in google.   
> 4. Got implementation in many languages but not in Python.   
> 5. Very less information about this psycho sorting algorithm.  
> 6. Algorithm is simple:
```
       procedure printNumber(n) 
            sleep n seconds 
            print n 
        end 

        for arg in args 
            run printNumber(arg) in background 
        end 
        wait for all processes to finish
```

# Modules used

1. ```from time import sleep```
2. ```from threading import Timer```

Both of them are system-installed modules


# Working 

1) In this sorting technique, we create different threads for each individual element present in the array. 
2) The thread is then made to sleep for an amount of time that is equal to value of the element for which it was created.  
3) This sorting technique will always sort in ascending order as the thread with the least amount of sleep time wakes up first and the number gets printed. 
4) The largest number will get printed in the end when its thread wakes up.  
5) It is also called as a Mysterious Sorting Algorithm because all the multithreading process happens in background and at the core of the OS.


# Limitations

1) This algorithm won’t work for negative numbers as a thread cannot sleep for a negative amount of time.
2) Since this algorithm depends on the input elements, so a huge number in the input array causes this algorithm to slow down drastically (as the thread associated with that number has to sleep for a long time). So even if the input array element contains only 2 elements, like- {1, 100000000}, then also we have to wait for a much longer duration to sort.
3) This algorithm doesn’t produce a correct sorted output every time. This generally happens when there is a very small number to the left of a very large number in the input array.  
For example – {34, 23, 1, 12253, 9}.
The output after sleep sorting is {9, 1, 23, 34, 1223}
4) A wrong output also occurs when the input array is reverse sorted initially, like- {10, 9, 8, 7, 6, 5}.   
The reason for such an unexpected output is because some time is taken between scanning through each element as well as some other OS operations (like inserting each threads in a priority queue for scheduling). We cannot simply ignore the time taken by all these things.  


# How to fix this ?
1) We can fix this by repeatedly sleep sorting on the new output until the output becomes sorted. Every time it will sort the elements more accurately.
2) The wrong output as discussed earlier happens due to the time taken by other OS works and scanning through each element.

# Author


|                                                                                                                                                                                                         <a href="https://nitin-kr.onrender.com/"><img src="https://github.com/nitinkumar30/nitscv/blob/main/image/nitin-1.jpg" width="150px " height="150px" /></a>                                                                                                                                                                                                          |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                                                                                                                                                                                                                                 **[Nitin Kumar](https://nitin-kr.onrender.com/)**                                                                                                                                                                                                                                                                  |
| <a href="https://twitter.com/nitinkumar30"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/twitter.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/b1AcK6AG16"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/nitin30kumar/"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/linkedin.png" width="32px" height="32px"></a> |