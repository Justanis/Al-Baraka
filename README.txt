Execute this on powershell (ADMIN) Set-ExecutionPolicy RemoteSigned

1. **Copy the template** to a new project folder.
2. **Run the setup script**:
   - On Windows, double-click `run_flask.ps1` or run:
     ```
     .\run_flask.ps1
     ```
3. **Open your browser** and go to `http://127.0.0.1:5000/`.


# Setup you DB :
1- Open you SSMS and then right click on Databases / new / name database "Baraka"


# Run migrations : \
whenever you update your models you need to create a migration :
  1- flask db init (the first time only)
  2- flask db migrate -m "Initial migration"
  3- flask db upgrade


Enjoy coding! 🚀
