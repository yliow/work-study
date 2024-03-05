# ryan-harvey-ws
# work-study

^moved the following from README.txt ...^

Clean up 350-heap/heap/.
Use 350-asymptotics/asymptotics/ as example.

# update fedora using fedora-installation
# run the bash executables as well

# run texhash as root to update files

# if error, try make c to clean the old files

# cp solutions.py and pyutil.py to both of the following directories:
/usr/lib/python3.7/site-packages/
/usr/lib64/python3.7/site-packages/

# then chmod these by doing the following:
chmod a+rwx /usr/lib/python3.7/site-packages/solutions.py
chmod a+rwx /usr/lib/python3.7/site-packages/pyutil.py
chmod a+rwx /usr/lib64/python3.7/site-packages/solutions.py
chmod a+rwx /usr/lib64/python3.7/site-packages/pyutil.py

necessary packages for liow's pdfs

using dnf install: 

texlive-comment
texlive-tikz-cd
texlive-pythontex
texlive-fvextra

using pip install --user:

pygments
