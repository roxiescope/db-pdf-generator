# db-pdf-generator
To use the app, download everything in the "dist" folder and run the .exe file.

To create executable for RLG, run:

pip install -r requirements.txt (if you're not rox)
pyinstaller --onefile roxlovesgus.py

FOR GUS:
Add a comment in each page with the format of <br>
[//]: # (Order:%s) <br>

Where %s is the id of the page (as decided by the database) that needs to follow after that one.

Set the first page of the document to <br>
[//]: # (Z.Order:%s)
