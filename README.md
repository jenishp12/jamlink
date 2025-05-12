# JamLink

This is a university team project. Built for musicians to network, showcase their portfolios, and collaborate with others in real time. Think of it as "LinkedIn for Musicians," featuring dynamic profiles, embedded content, and direct messaging.


- **Backend**: Built with Flask, handles user authentication, profile data, and messaging logic using SQLite as the database.
- **Frontend**: HTML/CSS and JavaScript-driven interface.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jenishp12/jamlink.git
2. **Navigate into the project directory:**
   ```bash
   cd jamlink
3. **Setup the virtual environment:**

   *It's recommended to use a virtual environment for better dependency management:*

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
6. **Run the Flask app:**
   ```bash
   python3 app.py
This will start the app locally at [http://127.0.0.1:5000](http://127.0.0.1:5000)
