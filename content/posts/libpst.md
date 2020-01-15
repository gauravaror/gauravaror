---
title: "WIP:A short tour of libpst"
date: 2019-11-28T17:45:50+11:00
draft: false
---

The `libpst` is a library to extract text from microsoft properitery format `.pst`, which is used to storing emails, attachments. There isn't a good documentation for `libpst`. 
This is a simple tour writing a `c++` program from scratch to extract an email and it's attachment from `.pst` file using `libpst`.

<!--more-->

Most of this code is taken/rewrite from command line tool `readpst` from same library.

### Library setup.

We will start with installing the libraries and then write a simple `.cpp` program and link it with `libpst`. Let's get started!

#### Install the `libpst` and `libpst-dev` package

```
~> sudo apt-get install libpst-dev
```

First, natural question to ask is why do we need to install `libpst-dev` package and what files does it installed. It installs header files of publically exposed function from library and shared libraries with implementations.

```
~> dpkg-query -L libpst-dev | egrep "libpst\.a|include"                                                                                       
/usr/include
/usr/include/libpst-4/libpst/libpst.h  // Main header file which is included.
/usr/lib/x86_64-linux-gnu/libpst.a   // Main shared library.
```

#### Link `libpst` library

First thing while using a library is to setup a test program which can link the libs and includes correctly. Best way to findout about cpp and library flags is to use `pkg-config` to see how to link headers and shared library. 

**include and libary flags:**
```
~> pkg-config --cflags libpst
-I/usr/include/libpst-4
~> pkg-config --libs  libpst
-lpst

```

Let's consider, we have a code file `extract_pst.cpp` which we want to link `libpst`. Let's write a `g++` command which can use to compile our program.
```
g++  extract_pst.cpp -I/usr/include/libpst-4 -lpst
```
