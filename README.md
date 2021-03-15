The goal of this exercise is to learn some basics of debugging Python code.

# Contents

-   [Getting set up](#getting-set-up)
-   [Learning objective](#learning-objective)
-   [The goal](#the-goal)
-   [The script](#the-script)
-   [Best practice 1: Put code into functions](#best-practice-1-put-code-into-functions)
-   [Best practice 2: Write modules not scripts](#best-practice-2-write-modules-not-scripts)
-   [Best practice 3: Use docstrings to document your code](#best-practice-3-use-docstrings-to-document-your-code)
-   [Best practice 4: Add tests to your docstrings](#best-practice-4-add-tests-to-your-docstrings)
-   [Acknowledgments](#acknowledgments)
-   [License](#license)


# Getting set up

At this point, you should have
(1) an account on [Github](https://github.com/) and
(2) been introduced to the very basics of [Git](https://git-scm.com/).

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository](https://github.com/joaks1/python-debugging), by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

1.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

1.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        $ git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

1.  Next, `cd` into the directory:

        $ cd the-name-of-directory-you-just-cloned

1.  At this point, you should be in your own local copy of the repository.

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* copy of the repo hosted on
    GitHub. Don't enter these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin master

# Learning objective 

Learn how to use the Python debugging module.


# The Python debugger

Almost all programs have bugs.
Following good coding practices can help you minimize bugs, and using `print`
statements can go a long way in helping you find and fix them.
However, some bugs are tricky to find, and scattering `print` statements all
over your code is not an efficient solution.

Thankfully, Python has a powerful debugger build right in:
The `pdb` module (which stands for Python debugger).
For this exercise, we will learn how to use the `pdb` to fix bugs in the
`area_of_rectangle.py` script included in this repo.


## Running the script through the debugger

First, open the `area_of_rectangle.py` script and read it over to get a sense
of what it should be doing.
Then, try running it:

    $ python3 area_of_rectangle.py 
    area_of_rectangle.py: Expecting one or two command-line arguments:
    	the height of a square or the height and width of a rectangle

We got a message saying that the script expects one or two arguments: the
height of a square or the height and width of a rectangle.
Let's try running it again with two arguments:

    $ python3 area_of_rectangle.py 3 6
    Traceback (most recent call last):
      File "area_of_rectangle.py", line 49, in <module>
        area = area_of_rectangle(height, width)
      File "area_of_rectangle.py", line 34, in area_of_rectangle
        area = height * width
    TypeError: can't multiply sequence by non-int of type 'str'

Oop, we definitely have some bugs to fix.

Now, let's try running the script through the Python debugger:

    $ python3 -m pdb area_of_rectangle.py 3 6

You will see output like:

    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(3)<module>()
    -> "A script for calculating the area of a rectangle."
    (Pdb) 

You are now inside the script, inside the Python debugger.
The first `pdb` you should now is `h` or `help`. Type `h` and hit enter:

    (Pdb) h

    Documented commands (type help <topic>):
    ========================================
    EOF    c          d        h         list      q        rv       undisplay
    a      cl         debug    help      ll        quit     s        unt      
    alias  clear      disable  ignore    longlist  r        source   until    
    args   commands   display  interact  n         restart  step     up       
    b      condition  down     j         next      return   tbreak   w        
    break  cont       enable   jump      p         retval   u        whatis   
    bt     continue   exit     l         pp        run      unalias  where    
    
    Miscellaneous help topics:
    ==========================
    exec  pdb
    
This shows you all of the `pdb` commands. You can get help for any of them
typing them after `h`. For example:


    (Pdb) h l
    l(ist) [first [,last] | .]
    
            List source code for the current file.  Without arguments,
            list 11 lines around the current line or continue the previous
            listing.  With . as argument, list 11 lines around the current
            line.  With one argument, list 11 lines starting at that line.
            With two arguments, list the given range; if the second
            argument is less than the first, it is a count.
    
            The current line in the current frame is indicated by "->".
            If an exception is being debugged, the line where the
            exception was originally raised or propagated is indicated by
            ">>", if it differs from the current line.

The `l(ist)` command is very helpful for seeing where you are in the script.
Try it:

    (Pdb) l
      1  	#! /usr/bin/env python3
      2  	
      3  ->	"A script for calculating the area of a rectangle."
      4  	
      5  	import sys
      6  	
      7  	
      8  	def area_of_rectangle(height, width = None):
      9  	    """
     10  	    Returns the area of a rectangle.
     11  	

The `->` shows us that we are at the first line of code in the file, which is
the docstring for the file.

Two useful commands to continue execution through the script are `n(ext)` and `s(tep)`.
Both will execute the next line of code. They differ in what they do when that
line of code calls a function.
`s(tep)` will "step into" the function, whereas `n(ext)` will simply call the
function and advance to the next line of code in the current context.

Let's use `n(ext)` to work our way through some of the script. Type `n` 5 times
and take note of how it is advancing through the script:

    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(5)<module>()
    -> import sys
    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(8)<module>()
    -> def area_of_rectangle(height, width = None):
    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(37)<module>()
    -> if __name__ == '__main__':
    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(38)<module>()
    -> if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(44)<module>()
    -> height = sys.argv[1]

We are now on the `height = sys.argv[1]` line. Use `l` to confirm this:

    (Pdb) l
     39  	        message = (
     40  	                "{script_name}: Expecting one or two command-line arguments:\n"
     41  	                "\tthe height of a square or the height and width of a "
     42  	                "rectangle".format(script_name = sys.argv[0]))
     43  	        sys.exit(message)
     44  ->	    height = sys.argv[1]
     45  	    width = height
     46  	    if len(sys.argv) > 3:
     47  	        width = sys.argv[1]
     48  	
     49  	    area = area_of_rectangle(height, width)

Use `n` one more time to define the `height` variable:

    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(45)<module>()
    -> width = height

Now, you can use the `p` command to print the value of `height`:

    (Pdb) p height
    '3'

If you try to print the value of `width` you will get an error, because it's not defined yet:

    (Pdb) p width
    *** NameError: name 'width' is not defined

If you use `l` you will see that you are currently on the line that defines `width`:

    (Pdb) l
     40  	                "{script_name}: Expecting one or two command-line arguments:\n"
     41  	                "\tthe height of a square or the height and width of a "
     42  	                "rectangle".format(script_name = sys.argv[0]))
     43  	        sys.exit(message)
     44  	    height = sys.argv[1]
     45  ->	    width = height
     46  	    if len(sys.argv) > 3:
     47  	        width = sys.argv[1]
     48  	
     49  	    area = area_of_rectangle(height, width)
     50  	

Go ahead and run the next line with `n` and then try printing `width` again:

    (Pdb) n
    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(46)<module>()
    -> if len(sys.argv) > 3:
    (Pdb) p width
    '3'

You can also use Python code within the debugger. Let's do that to check the
type of `height` and `width`:

    (Pdb) type(height)
    <class 'str'>
    (Pdb) type(width)
    <class 'str'>

Note, you can also change variables dynamically within the debugger.
For example:

    (Pdb) height = int(height)
    (Pdb) p height
    3
    (Pdb) type(height)
    <class 'int'>

Whenever you want to exit the debugger, simply use the `q(uit)` command.

## Using breakpoints

Rather than run the entire script through the debugger, we can add a single
line of code to drop us into the debugger at any place in our code.

Open the `area_of_rectangle.py` script with your text editor and
change the code in the `area_of_rectangle` function from:

```python
    if width:
        width = height
    area = height * width
    return area
```

To:

```python
    if width:
        width = height
    import pdb; pdb.set_trace()
    area = height * width
    return area
```

We simply added `import pdb; pdb.set_trace()` just before we calculate the area
of the rectangle.

Now, you can run the script as you normally would:

    $ python3 area_of_rectangle.py 3 6

(Notice, we did not have to invoke the pdb module like above; that is done by
`pdb.set_trace()`)
Notice that you get dropped into the `pdb` debugger:

    > /home/jamie/Dropbox/projects/python-debugging/area_of_rectangle.py(35)area_of_rectangle()
    -> area = height * width
    (Pdb)

Now we can use `l` to see where we are:

    (Pdb) l
     30  	    14
     31  	    """
     32  	    if width:
     33  	        width = height
     34  	    import pdb; pdb.set_trace()
     35  ->	    area = height * width
     36  	    return area
     37  	
     38  	if __name__ == '__main__':
     39  	    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
     40  	        message = (

We are at the line immediately after our `pdb.set_trace()` call.  Now, we can
use the debugger to inspect variables and continue to execute the script, just
like we learned above. For example, use `p` and `type` to inspect the variables
`height` and `width`:

    (Pdb) p height
    '3'
    (Pdb) p width
    '3'
    (Pdb) type(height)
    <class 'str'>
    (Pdb) type(width)
    <class 'str'>


# The exercise

Now that you know the basics of the Python debugger,
use it to debug the `area_of_rectangle.py` script.


# Acknowledgments

## Support
This work was made possible by funding provided to [Jamie
Oaks](http://phyletica.org) from the National Science Foundation (DEB 1656004).


# License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.
