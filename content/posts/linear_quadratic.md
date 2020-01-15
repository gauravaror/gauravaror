---
title: "Linear to Quadratic and back"
date: 2019-11-18T21:37:37+11:00
draft: false
---

Can a single for loop be running with quadratic time complexity?

<!--more-->


{{< figure src="/linear_quad_1.png" title="What's wrong" >}}

I wrote a shell script to generate data for a test I was writing. The script goes something like this:

#### Script A

```shell
#!/bin/sh
data=""
for i in `seq 1 6000`;
do
data="${data}newdata=$i";
done
##Time for this script  
##./new.sh  9.01s user 0.02s system 99% cpu 9.049 total
```

It sure looks like a script which can run in O(n) time, a single for loop.
It was bit baffled when I got review comment saying this is quadratic or O(n2) in time complexity. I initially thought it's something to do with shell!! Maybe it does some advanced representation thing and stuff.

#### Script B

```shell
#!/bin/sh
data=""
for i in `seq 1 6000`;
do
data="newdata=$i";
done
##Time for this script  
##./new.sh  0.05s user 0.00s system 97% cpu 0.051 total
```

The script A above takes 9.01 second, whereas Script B takes 0.05 seconds.
It's just the assignment operator which was increasing the time complexity of this script.

**How?**
Since it has to assign whole data of string to the new variable.
It has to traverse the whole data generated from 1 to 5999 and append data of 6000th iteration. So 6000th iteration is equivalent to generating data from the whole loop. **Quadratic!!**

#### Back to Linear space, we seem to like them.
In advanced shells, we can just change the script to:

##### Script C

```shell
data=""
for i in `seq 1 6000`;
do
data+="newdata=$i";
done
##Time for this script  
##./new.sh  0.07s user 0.01s system 97% cpu 0.075 total
```

It would make it linear. But the version of shell we use for test script doesn't support append operation like Script C. Yet to figure out how to solve it.

#### Just a reminder to me: Think and code
It is interesting how substitution instead of **append** can increase performance time with the same result.

These small mistakes can make your program unusable. Though our example is in the shell script, doing this mistake in other languages is possible but less probable as people are used to += operators.

But the various version of bash with different features these mistakes highly probable in shell scripting.
