# db-pdf-generator
To create executable for RLG, run:

pip install -r requirements.txt (if you're not rox)
pyinstaller --onefile roxlovesgus.py

FOR GUS:
Add a comment in each page with the format of --
[//]: # (Order:%s)
Where %s is the id of the page (as decided by the database) that needs to follow after that one
Set the first page of the document to --
[//]: # (Z.Order:%s)