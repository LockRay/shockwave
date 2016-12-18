#Shockwave celluar automata

Shockwave is a cellular automata created by Lock. The rules are as follows.

```A becomes B
B becomes A, unless next to an A: then it becomes 0
0 becomes 0, unless next to an A: then it becomes A```

It was initially created to create a sort of rippling effect with the simplest starting position. See below.

```00000A00000
0000ABA0000
000AB0BA000
00AB000BA00
0AB00000BA0
AB0000000BA
```

It creates this rippling effect with 1d and 2d automata alike, and I postulate that the same will occur for n dimensional automata under the above ruleset.

There are many nontrivial and interesting behaviors that this cellular automata have. One of these is that it is reversable--there is only 1 position that will stem to another position. It has been proven that to reverse it (to step backwards in time), all you have to do is swap the As and Bs in the rule and apply them. This means that a single isolated A (000A000) must be reached from the following sequence: 000B000.

Yet another non-trivial behavior that may interest you is that it is impossible for all matter to die--that is it is impossible for a sea of zeroes to occur on any geometry of any dimension given any starting position other than the sea of zeroes.
