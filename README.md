<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>HireXpress</h1>

<h2>Overview</h2>
<p><strong>HireXpress</strong> is an offer letter generator website designed to streamline the process of creating, managing, and sharing offer letters. This project was developed for a hackathon and includes features such as user authentication, PDF generation, and sharing options.</p>

<h2>Features</h2>
<ul>
    <li><strong>User Authentication:</strong> Secure login and registration system to protect sensitive data.</li>
    <li><strong>Offer Letter Generation:</strong> Easily create customized offer letters using predefined templates.</li>
    <li><strong>PDF Export:</strong> Convert offer letters to PDF format for easy sharing and record-keeping.</li>
    <li><strong>Share Option:</strong> Directly share generated offer letters via email or a shareable link.</li>
</ul>

<h2>Tech Stack</h2>
<ul>
    <li><strong>Backend:</strong> Django, Django-tailwind</li>
    <li><strong>Frontend:</strong> HTML, CSS, JavaScript,tailwind css</li>
    <li><strong>Database:</strong> SQLite (for development)</li>
    <li><strong>PDF Generation:</strong> pdfkit  (or any other library used)</li>
    <li><strong>Version Control:</strong> Git</li>
</ul>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre><code>git clone https://github.com/yourusername/HireXpress.git
cd HireXpress</code></pre>
    </li>
    <li><strong>Create and Activate a Virtual Environment:</strong>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
    </li>
    <li><strong>Install Dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Apply Migrations:</strong>
        <pre><code>python manage.py migrate</code></pre>
    </li>
    <li><strong>Create a Superuser:</strong> (for accessing the admin panel)
        <pre><code>python manage.py createsuperuser</code></pre>
    </li>
    <li><strong>Run the Development Server:</strong>
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li><strong>Access the Website:</strong> Open your browser and go to <code>http://127.0.0.1:8000</code>.</li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Register/Login:</strong> Create an account or log in with existing credentials.</li>
    <li><strong>Create Offer Letter:</strong> Fill in the required details and generate an offer letter.</li>
    <li><strong>Export as PDF:</strong> Download the offer letter as a PDF document.</li>
    <li><strong>Share:</strong> Use the provided options to share the offer letter via email or a generated link.</li>
</ol>

<h2>Project Structure</h2>
<pre><code>HireXpress/
├── core/               # Core app containing main logic
├── users/              # User authentication and management
├── templates/          # HTML templates for the frontend
├── static/             # Static files (CSS, JS, images)
├── db.sqlite3          # SQLite database (development)
├── manage.py           # Django management script
└── README.md           # Project README file</code></pre>

<h2>Contribution</h2>
<p>Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create your feature branch (<code>git checkout -b feature/YourFeature</code>).</li>
    <li>Commit your changes (<code>git commit -am 'Add some feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/YourFeature</code>).</li>
    <li>Create a new Pull Request.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contact</h2>
<p>For any inquiries or questions, please contact <a href="mailto:vishalsinha.inbox@gmail.com">vishalsinha.inbox@gmail.com</a>.</p>

<hr>
<p><em>This project was developed as part of a hackathon. We appreciate your interest and support!</em></p>

</body>
</html>
