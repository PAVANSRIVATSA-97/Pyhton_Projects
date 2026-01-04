# Pyhton_Projects
1. 🏥 Health Reminder (Water & Stretch)
A background automation script that sends desktop notifications at set intervals to encourage healthy habits.

Key Features: Uses notify-py for cross-platform alerts and time for scheduling.

Concepts: Infinite loops, try-except for clean exit, and background process management.

2. 📄 PDF Master (Merger & Rotator)
A tool to manipulate PDF files locally.

Key Features: Merges multiple PDFs into a single file and can rotate pages by 90-degree increments.

Concepts: PyPDF2 library, file I/O, and list iteration.

3. 💰 Who Wants to Be a Millionaire
A terminal-based quiz game using complex data structures.

Key Features: Tracks score, uses nested lists for questions, and handles user input errors.

Concepts: Truthiness (while q:), match-case statements, and input validation.

4. 📂Intelligent File Organizer
Automates file sorting by mapping extensions to directories.

Logic: Uses os.makedirs(exist_ok=True) to handle existing directories without crashing.

Path Handling: Implements dynamic path construction to resolve FileNotFoundError during cross-directory moves.

5. 🗞️ News & AI Integration
A dual-purpose tool that fetches news and processes text.

JSON Parsing: Extracts nested data such as article["source"]["name"].

Security: API keys are injected via .env files using load_dotenv

6. 📱 Dynamic QR Code Generator
A utility for generating high-resolution, customizable QR codes for URLs, text, or contact information.

Logic: Utilizes the QRCode class for fine-grained control over versioning (matrix size) and error correction levels.

