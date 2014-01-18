Programmer's Notepad 2
version 2.4.0-2378-duke-DBR -- *entirely unofficial*
====================================================

Dear unfortuante reader,


This "fork" of sorts, if you can call it that, rides entirely on the selfless 
and marvelous work of Simon Steele, who is the creator of the original program
and is, evidently, its sole contributor at the time of writing.


What is this?
-------------

This project is an attempt to hack away at the binary distribution of 
Programmer's Notepad 2 (x86 version 2.4.0-2378-duke at the time of writing), 
with very limited experience in the underlying technologies. It stems from my
hopes in hopes of achieving at least some of the following:

- Improved support for AutoIt3, including the use of an updated AutoIt3 scheme
  circa ~2011-12 rather than 2008 which is presently included.
  
- A wider array of AutoIt3 tools, to more closely approximate the SciTE4AutoIt
editing experience (but with the flexibility and nice UI of Programmer's
Notepad)

- A wider array of development tools configured out of the box in general
  for common langauges (such as Python and AutoIt) ... the goal eventually being
  to provide an easy UI for setting them all up at once, i.e. gathering
  the relevant paths on the actual end user's machine to the requisite tools.

- More familiarity with PyPN and Python in general, included in this
  distribution.
  
- More familiarity with the Scintilla IDE "core" component, especially custom
  Lexers and how they operate together with the PN "scheme" files to create
  a useful and productive environment for working source files of the
  relevant type(s).
  
- An excuse for reckless experimentation.


Why didn't you start by forking the source code proper?
-------------------------------------------------------

I anticipate at some point (probably soon) that I will be downloading the
Programmer's Notepad source, as it is already generously provided on Github. 
Starting from the binary is just the quickest way that occurred to me of hacking
an environment together for AutoIt3 development and assembling a quick
peripheral halo of supporting tools using the existing PN mechanisms provided
to the user (langauge-specific "Tool" configurations, and PyPN scripts).


Everything else
---------------

- I don't know if it even will work yet, but my plan is to symlink the
"AppData/Roaming/Echo Software/PN2" directory to the "user-data" folder
in this repository in hopes that the application will still start.

- I expect you also may need to create a symlink to the file "python26.dll"
in the "application" folder which corresponds to the actual location of it
on your machine, probably "C:\Python26" if you went with the defaults. This
is to enable the PyPN extension to work.


I will refer to this codebase and, variously, the files in the user-data
component as well, as PN2-DBR for the sake of brevity.

The actual source code for Programmer's Notepad can be found on its official
GitHub page:
https://github.com/simonsteele/pn

And the official website, along with lots of documentaiton and resources, is
located here:
http://www.pnotepad.org/


I am only starting this project because of how much I love Programmer's
Notepad, and how many years of headache-free development it has brought me.

Sincerely,
--David Reilly
