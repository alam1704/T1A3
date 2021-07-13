#!/bin/bash
echo "Can i make changes to your computer? Y/N"
read response
if test "$response" = "y" -o "$response" = "Y";
then  
    python3 -m ensurepip --upgrade
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 example.py
fi

"""note that this only works on macs. We saw in class that 
different OS that it might cause errors. 
So please mention in the scope that although
the python code might work, the bash script will
need to be tweaked to work on different OS"""