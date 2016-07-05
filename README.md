Online Password Cracking

I wrote my program in Python so I did not need to include a makefile to 
compile it. I also wrote a tester program test.py that I used to ensure that 
my subprograms being called within my program were doing what I expected. 

Within my program, I call the password fooPasswordKeeper program and if I find 
the password, I write the credentials found to the stolen_creds.txt within 
my program. 

I initially ran my program with this command: 

    $ nice john --wordlist=/usr/share/dict/american-english --stdout | ./fooCracker

This failed to uncover the password and no stolen_creds.txt was created. 

I tried again with this command: 

    $ nice john --wordlist=/usr/share/dict/words --rules --stdout | ./fooCracker

This program was taking a very long time to run, and I decided that it must not be the correct input and aborted the process. 

Next, I tried using the john markov tool for input with this command: 

    $ nice john --markov --stdout | ./fooCracker

But this generated too many password candidates and resulted in a segmentation 
fault. 

I then tried this command: 

    $ nice john --wordlist --rules --stdout | ./fooCracker

And this also failed to uncover the password. 

I then went to Jan Werner's google plus page and individually tested the 
information found there, such as the university attended, current job, etc. 
I tested them by individually putting them directly into the fooPasswordKeeper 
program. None of these tests were successful. 

I then decided to try using the output from part 1 of the assignment as password candidates for part 2. So I copied the results from part 1 into my project 
folder using the following command: 

    $ cp ~/submissions/homework2/mnemonic/results.out results.out

I then tested these results on my program: 

    $ nice cat results.out | ./fooCracker

Success! This time the stolen_creds.txt file was created and contained the 
information in the format I was expectng. The cracked password is N2bpitg0.  
  
