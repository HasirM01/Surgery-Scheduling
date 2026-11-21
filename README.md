# Surgery Scheduling System

A Flask and MySQL web application prototype for managing the users and records associated with an organ donation and surgery scheduling workflow.

## Project overview

The supplied project abstract describes an automated organ-donation scheduling concept that aims to match donors and recipients using factors such as blood-group compatibility, organ viability, medical urgency, and historical outcomes. The abstract also discusses a Deep Q-Learning (DQL) approach.

**Implementation note:** The source code included in this repository currently provides Flask pages and database operations for administrator, doctor, donor, and patient registration/login workflows. A DQL model or donor-recipient matching implementation was not present in the supplied Python source files, so this README does not claim that those algorithmic features are implemented.

## Technology stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Database driver:** PyMySQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap and bundled frontend libraries

## Current application modules

- Home page
- Administrator login and dashboard page
- Doctor login and dashboard page
- Donor login and registration
- Doctor registration by administrator
- Patient registration by doctor
- MySQL database tables for administrators, doctors, donors, and patients

## Repository structure

```text
Surgery-Scheduling-System/
├── main.py                         # Flask application and routes
├── ar_master.py                    # MySQL helper and email utility
├── database.sql                    # Database schema and sample admin record
├── requirements.txt                # Python dependencies
├── .env.example                    # Example environment configuration
├── .gitignore
├── README.md
├── Surgery-Project-Abstract.pdf
└── templates/                      # HTML templates and frontend assets
```

## Prerequisites

- Python 3.9 or later
- MySQL Server
- pip

## Setup and installation

1. Clone the repository:

   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd <YOUR_REPOSITORY_FOLDER>
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the MySQL database and import the schema. For example, from the MySQL command line:

   ```sql
   CREATE DATABASE python_surgery_scheduling;
   ```

   Then import `database.sql` into the `python_surgery_scheduling` database using MySQL Workbench or:

   ```bash
   mysql -u root -p python_surgery_scheduling < database.sql
   ```

5. Configure environment variables using `.env.example` as a reference. Copy it to `.env` and set your local values. Do not commit `.env`.

   The application reads environment variables directly from the process environment; the `.env` file is a reference template. If using a `.env` file, export/load its values in your terminal or configure them in your IDE run configuration.

   Required database variables:

   - `DB_HOST`
   - `DB_USER`
   - `DB_PASSWORD`
   - `DB_NAME`

   Set `FLASK_SECRET_KEY` to a long, random value. Email settings are only needed if the email utility is used.

6. Run the application from the repository root:

   ```bash
   python main.py
   ```

7. Open the local development URL shown in the terminal (normally `http://127.0.0.1:5000/`).

## Database

The supplied SQL dump creates these tables:

- `admin_details`
- `doctor_details`
- `donar_details`
- `patient_details`

The SQL file includes a sample administrator record (`admin` / `admin`). Change or remove this sample credential before using the application beyond a local demonstration. Do not use the sample credentials on a public deployment.

## Important security and production notes

This repository is prepared for source-code review and local demonstration, not production deployment. The supplied application contains legacy database-query construction using string concatenation and stores passwords in plaintext. Before handling real patient, donor, or medical data, the application needs (at minimum):

- Parameterized SQL queries to prevent SQL injection.
- Secure password hashing and credential migration.
- Authentication and authorization checks on protected routes.
- Secure session and CSRF configuration.
- Validation, access controls, and privacy safeguards appropriate for sensitive health information.
- Production-grade error handling, logging, and deployment configuration.

Never commit real credentials, personal data, database backups, or `.env` files.

## Notes

- The project source uses the table name `donar_details` (spelling preserved from the supplied code and SQL schema).
- The original project documentation and IDE/virtual-environment folders were not included in this GitHub-ready source package, to keep the repository focused and avoid uploading generated dependencies. The legacy `master_key.txt` check was removed from the database helper because it blocked clean setup and depended on the current year.
- The project has not been fully runtime-tested against a configured MySQL server.

## License

No license was supplied with the original project. Add a license only after confirming that the project owner has permission to publish the source and selecting the intended reuse terms.
