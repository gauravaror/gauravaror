---
title: "Cpp concepts"
date: 2020-04-30T11:10:25+10:00
draft: true
---

explicit
========
https://stackoverflow.com/questions/121162/what-does-the-explicit-keyword-mean
This describe with interesting example when to use explicit.

static
======
When using a variable just inside a single cpp file, we should declare the variable as static.

@my description
Using static function in a file descibe variable as internal linkage

https://docs.microsoft.com/en-us/cpp/cpp/storage-classes-cpp?view=vs-2019#static
We seem to define the internal linkage for this variable which is true but if we don't define it as static, is there chances for it to get exposed externally?
I following about using static in this situation here (https://stackoverflow.com/a/52511865/328897):
All variables declared at file scope should be declared static, for the purpose of private encapsulation and to reduce namespace clutter.
Each translation unit gets its own copy of the static variable, but here omega.cc is the entry point.


@Olly Betts (Xapian):
Yeah, that's about right.  More specifically:
It's useful to the compiler as it then knows that the variable can only be used by code in this file (unless a pointer or reference is passed to a function defined in another file) and it can often optimise better knowing that.
It avoids problems if two different files have their own variable with the same name which is intended to be private.  If they are marked static then they really are different variables.  If they aren't then the two end up being linked together, which can result in undefined behaviour (e.g. if the two variables actually have different types - you may get a linker error for that, but not with all compilers).  We actually had a bug in xapian-core not long ago due to this, though that was for inline functions with the same name in different source files.
It's also a clear way to document to people reading the code that the variable is only used in this file (and in a way that you can be sure that's genuinely the case, since the code wouldn't compile otherwise).
