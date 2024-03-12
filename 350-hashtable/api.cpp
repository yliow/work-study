\sectionthree{API}

Like I said, it's not easy designing hash functions.
Furthermore, different scenarios might require different hash functions
even for the same type of values.
For instance strings representing human names might
require a hash function that is different from
strings representing book titles.
It might therefore be a good idea when designing a hash table 
to have a class that allows you to specify specific hash functions.

We of course want to insert, delete, search in our hashtable.
In the following, \verb!h! is a hash table object.
\begin{console}
h.insert(key, value) Insert key-value into hash table. 
                     Exception is thrown if key is 
                     already in the hash table.
h.erase(key)         Delete key-value from hash table of 
                     given key.
                     Exception is thrown if key is not 
                     found.
h[key]               Reference to value of given key.
                     If not found exception is thrown.
h.get(key, default)  Return value of given key. If not 
                     found, default is returned.
\end{console}
So if \verb!height! is a hash table of name-height pairs,
we can do this:
\begin{console}
height["Abe"] = 6.5;
\end{console}
Here are some auxiliary methods:
\begin{console}
h.clear()            Remove all keys.
h.size()             Number of keys in the hash table.
h.keys()             Returns an iterable list of keys.
h.values()           Returns an iterable list of values.
h.has_key(key)       Returns true if key is present.
h.update(h1)         Update h with hash table h1.
\end{console}


For constructor, we want to allow users to specify initial size.
If not specified, let's use a default that is stored as a static 
in the class that can be modified. 
Let's say the default is initially set to 97.




\newpage
