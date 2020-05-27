---
title: "gdb Demystified"
description: "gdb is one of the useful commands to debug what's going wrong with your program. Let's try to demystify it!!"
date: 2019-09-29T16:29:48+10:00
---

**gdb** is one of the useful commands to debug what's going wrong with your program.
<!--more-->


Let's try to understand how we can demystify where and what is making your code hang in a running program.

#### Step 1
Check the process id of your program:

```shell
ps -ef | grep program
```


#### Step 2
Attach to the stuck process via gdb, when it is in a stuck state

```shell
gdb --pid=PID
```

#### Step 3

Check the stack trace of the hanging process.
```
bt
```

#### Step 4
If your process is hanged in a library point and you are not able to get the context in your code, i.e file which is
```shell
# to go one level down in stack trace
frame 1
# to go two level down in stack trace
frame 2
# to go three level down in stack trace
frame 3
```

#### Step 5
Print the variable to check the context, i.e what input made the program stuck.
```shell
# dump is here the main variable which is making the replace operation stuck for me.
p dump
```

#### Step 6
Take the corrective action by understanding the nature of the problem by changing the reference of frames and see what the variable (input) making you program stuck.
- Will add more use cases, as I come along.
