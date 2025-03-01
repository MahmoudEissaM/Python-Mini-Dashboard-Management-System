
<div class="container">
    <h1>📌 Project Management CLI</h1>
    <p>A simple <strong>Python-based CLI application</strong> for managing projects, allowing users to <strong>register, sign in, create, edit, view, and delete projects</strong>.</p>

    <h2>🚀 Features</h2>
    <ul>
        <li>✅ <strong>User Authentication</strong>: Register & log in with email and password validation.</li>
        <li>✅ <strong>Project Management</strong>: Add, edit, delete, and view projects.</li>
        <li>✅ <strong>Data Storage</strong>: JSON-based database.</li>
        <li>✅ <strong>Input Validation</strong>: Strong password, email format, and date validation.</li>
    </ul>

    <h2>🛠 Technologies Used</h2>
    <ul>
        <li>Python 🐍</li>
        <li>JSON (Data Storage)</li>
        <li>Regex (Input Validation)</li>
        <li>Datetime (Date Handling)</li>
    </ul>

    <h2>📥 Installation & Setup</h2>
    <h3>1️⃣ Clone the Repository</h3>
    <pre><code>git clone https://github.com/MahmoudEissaM/project-management-cli.git
cd project-management-cli</code></pre>

    <h3>2️⃣ Create a Virtual Environment (Optional)</h3>
    <pre><code>python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows</code></pre>

    <h3>3️⃣ Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>4️⃣ Run the Application</h3>
    <pre><code>python main.py</code></pre>

    <h2>📌 Usage Guide</h2>
    <p>Once you run the application, you will see:</p>
    <pre><code>1. Sign In
2. Register
3. View Projects
4. Add Project
5. Edit Project
6. Delete Project
7. Exit</code></pre>

    <h2>📊 Project Data Structure</h2>
    <h3>User Schema</h3>
    <pre><code>{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "hashed_password",
    "phone": "+201234567890"
}</code></pre>

    <h3>Project Schema</h3>
    <pre><code>{
    "title": "AI Startup",
    "details": "An AI-based recommendation system.",
    "target": 50000,
    "start_date": "2025-03-01",
    "end_date": "2025-06-01",
    "owner_email": "john.doe@example.com"
}</code></pre>

    <h2>🔮 Future Enhancements</h2>
    <ul>
        <li>🚀 Encrypt passwords instead of storing them in plain text.</li>
        <li>🚀 Convert CLI-based interaction into a Web or GUI-based application.</li>
        <li>🚀 Move from JSON storage to PostgreSQL or MySQL.</li>
        <li>🚀 Implement project search & filtering options.</li>
    </ul>

    <h2>👨‍💻 Author</h2>
    <p><strong>Mahmoud Eissa</strong></p>
    <p>🔗 <strong>GitHub</strong>: <a href="https://github.com/MahmoudEissaM" target="_blank">MahmoudEissaM</a></p>
    <p>📧 <strong>Email</strong>: mahmoudessa8200@gmail.com</p>

    <h2>📜 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>
</div>

</body>
</html>
