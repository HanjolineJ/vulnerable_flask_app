from flask import Flask, request, escape, jsonify, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session handling

# Sample "database" of users
users = {
    'user1': {'password': 'password123', 'data': 'This is user1’s data'},
    'user2': {'password': 'pass456', 'data': 'This is user2’s data'}
}

@app.route('/')
def home():
    return "Welcome to the Vulnerable Flask App!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Comment out remove the admin_bypass section to fix the vulnerability
        Admin bypass section for reference
        if username == 'admin_bypass':
            session['username'] = 'admin'
            return redirect(url_for('dashboard'))
        # Debug print statements
        print(f"Attempting login with username: {username} and password: {password}")
        
        # Regular authentication process
        #if username in users and users[username]['password'] == password:
            #session['username'] = username
            #print(f"Login successful for user: {username}")
            #return redirect(url_for('dashboard'))
        
        print(f"Login failed for user: {username}")
        return "Invalid credentials!", 401
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    # Vulnerable: Allow user to specify 'username' parameter in the URL
    # This line introduces the vulnerability by allowing users to specify any username in the URL
    # username = session.get("username")   # Secure
    username = request.args.get('username') # Insecure
    # username = request.args.get('username')  # To secure, replace this line with 'username = session.get("username")'
    
    # If there’s no logged-in user, redirect to login
    if not username:
        return redirect(url_for('login'))
    
    # Allow access to data based on the URL parameter, creating an IDOR vulnerability
    # To secure, only allow access to session-based user data
    if username in users:
        return f"Hello, {username}! Here is your data: {users[username]['data']}"
    
    return "User not found!", 404


@app.route('/search', methods=['GET'])
def search():
    # XSS vulnerability: directly display the 'query' parameter without sanitizing
    query = request.args.get('query', '')  # Insecure
    return f"Search results for: {query}"  # Insecure
    #sanitized_query = escape(query)   # Secure
    #return f"Search results for: {sanitized_query}" # Secure


#sanitized_query = escape(query)  # Escape HTML tags to prevent XSS
    #return f"Search results for: {sanitized_query}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
