# NoA_I
Influenced by Arnold Schönbergs dodecaphonism.
 ## Python requirements 
 - pip3 install opencv-python
 - pip3 install python-osc
 - pip3 install numpy
 ## Install processing
 https://processing.org/
 - install osc5 (external library)
 ## Get MaxMsp
 https://cycling74.com/
 ## Download Rave and follow Instructions for training and compiling the external
 https://github.com/acids-ircam/RAVE
 ## How to use
 - From Terminal or Visual Studio Code launch NoA_1.py
 - Open the Sequencer_Grid.pde with processing
 - Open the MaxMsp patches (use your own RAVE models) 
 ## How it works
 - This is an installation, which uses camera input. 
 - When it detects a face it starts the actual processing.
 - For every 50 x 50 pixel it performs the mean.
 - It saves every 50 x 50 pixel and computes the mean and adds it to the part before.
 - The highest pixel mean will play a sound.
 - The highest pixel will be reset to 0.
 - Like this every sound has a higher possibility to get played.
 ## Why...
 - This was part of an university project.
 

