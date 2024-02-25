HW3 IMPORTS - contains files imported from ec2 instance including 0-9.py and test-output.txt.
SSH COMMAND TO SEND FROM EC2 -> Folder in hw3 called hw3imports
sudo scp -r -i /mnt/c/EECS481/ewoj_2.pem ubuntu@ec2-3-80-206-109.compute-1.amazonaws.com:~/hw3 /mnt/c/EECS481/hw3/hw3Imports
\n
change paths as needed.

scp command to send potentially updated mutate.py -> ec2 instance
sudo scp -i ewoj_2.pem /mnt/c/EECS481/hw3/hw3Files/starter.py ubuntu@ec2-3-80-206-109.compute-1.amazonaws.com:~/hw3

hw3files contains the unchanged starter code
