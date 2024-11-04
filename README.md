# **Secure Coding Demo**

This repository contains a Dockerized Flask application to demonstrate common web application vulnerabilities, including ***Broken Authentication***, ***Insecure Direct Object References (IDOR)***, and ***Cross-Site Scripting (XSS)***. Each vulnerability is showcased with a vulnerable version and a patched version to demonstrate how to identify, exploit, and secure each flaw.

---

## **Phases**

### ***Phase 1: Setting Up the Environment***
1. Docker and Flask setup allows for easy manipulation and resetting of vulnerable and secure states.
2. Burp Suite is used for intercepting and modifying requests to demonstrate each vulnerability.

### ***Phase 2: Vulnerabilities Demonstrated***
- **Broken Authentication**: Demonstrates a login bypass where entering a specific username bypasses authentication.
- **Insecure Direct Object References (IDOR)**: Allows unauthorized data access by manipulating parameters in the URL.
- **Cross-Site Scripting (XSS)**: Demonstrates how unsanitized user input can lead to script injection.

### ***Phase 3: Build, Exploit, and Patch***
1. **Build**: Vulnerable code is built using Docker and VS Code.
2. **Exploit**: Burp Suite is used to intercept and exploit each vulnerability.
3. **Patch and Re-Test**: Vulnerabilities are fixed, and functionality is re-tested to confirm the fix.

---

## **Vulnerabilities and Fixes**

### **1. Broken Authentication**
- ***Vulnerability***: Bypassing login credentials by using a specific username (`admin_bypass`).
- ***Exploit***: Login as `admin_bypass` without a password to gain access.
- ***Fix***: Remove the `admin_bypass` condition in the login route.
- ***Outcome***: Only users with valid usernames and passwords can log in.

### **2. Insecure Direct Object Reference (IDOR)**
- ***Vulnerability***: Allows users to access other users' data by changing the `username` parameter in the URL.
- ***Exploit***: Log in as `user1` and modify the URL to access `user2`'s data.
- ***Fix***: Use session-based access by replacing `username` parameter with `session.get("username")`.
- ***Outcome***: Only the logged-in user can access their own data.

### **3. Cross-Site Scripting (XSS)**
- ***Vulnerability***: Unsanitized user input is displayed directly, allowing for JavaScript injection.
- ***Exploit***: Inject `<script>alert('XSS')</script>` in the `query` parameter to trigger an alert.
- ***Fix***: Use Flask’s `escape()` function to sanitize the input.
- ***Outcome***: Input is displayed as plain text, preventing script execution.

---

## **Demo Guide: Steps to Demonstrate and Fix Each Vulnerability**

### **Broken Authentication**
1. ***Set the Vulnerable Code***: Uncomment `admin_bypass` in the login route.
2. ***Explain the Vulnerability***: Describe how the `admin_bypass` condition allows unauthorized access.
3. ***Demonstrate***: Log in with `admin_bypass` and any password to show bypass.
4. ***Apply the Fix***: Remove `admin_bypass` from the login route.
5. ***Explain the Fix***: Only valid credentials are now allowed.
6. ***Verify***: Attempt to log in with `admin_bypass`—it should be rejected.

### **Insecure Direct Object Reference (IDOR)**
1. ***Set the Vulnerable Code***: Use `username = request.args.get('username')` in the dashboard route.
2. ***Explain the Vulnerability***: Describe how URL manipulation allows unauthorized data access.
3. ***Demonstrate***: Log in as `user1`, then modify the URL to access `user2`'s data.
4. ***Apply the Fix***: Use `session.get("username")` in the dashboard route.
5. ***Explain the Fix***: Data access is now restricted to the session user.
6. ***Verify***: Log in as `user1`, modify the URL—only `user1`'s data should show.

### **Cross-Site Scripting (XSS)**
1. ***Set the Vulnerable Code***: Display `query` directly in the `search` route.
2. ***Explain the Vulnerability***: Describe how unsanitized input allows script injection.
3. ***Demonstrate***: Inject `<script>alert('XSS')</script>` to trigger an alert.
4. ***Apply the Fix***: Use `escape(query)` in the `search` route.
5. ***Explain the Fix***: Input is now displayed as text, preventing script execution.
6. ***Verify***: Inject the script again—it should display as plain text.

---

## **Getting Started**

### **Prerequisites**
- [Docker](https://www.docker.com/get-started)
- [VS Code](https://code.visualstudio.com/)
- [Burp Suite](https://portswigger.net/burp)

### **Installation**
1. Clone the repository.
2. Build and start the Docker container:
   ```bash
   docker-compose up --build
