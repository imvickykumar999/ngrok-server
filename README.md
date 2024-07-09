## Steps to Set Up ngrok with an Authtoken

1. **Sign Up for an ngrok Account**:
   - Go to [ngrok.com](https://ngrok.com/) and sign up for a free account.

2. **Retrieve Your Authtoken**:
   - After signing up and verifying your account, log in to the ngrok dashboard.
   - Go to the "Your Authtoken" section under the "Getting Started" page.
   - Copy your authtoken.

3. **Install Your Authtoken**:
   - Open a terminal on your local machine.
   - Run the following command to install your authtoken (replace `YOUR_AUTHTOKEN` with the token you copied):
     ```bash
     ngrok authtoken YOUR_AUTHTOKEN
     ```

4. **Start an HTTP Tunnel**:
   - Now you can start an HTTP tunnel using the following command:
     ```bash
     ngrok http 8000
     ```

5. **Use the Provided URL**:
   - After running the command, ngrok will provide a forwarding URL (e.g., `http://abcd1234.ngrok.io`).
   - Share this URL with your friends to allow them to connect to your server.

### Detailed Instructions

#### 1. Sign Up for ngrok

- Visit [ngrok.com](https://ngrok.com/) and click on "Sign up".
- Complete the registration process by providing the required details and verifying your email.

#### 2. Retrieve Your Authtoken

- Log in to your ngrok account.
- Navigate to the "Getting Started" section.
- Copy the authtoken provided.

#### 3. Install Your Authtoken

- Open a terminal.
- Run the command to set up your authtoken:
  ```bash
  ngrok authtoken YOUR_AUTHTOKEN
  ```

  Replace `YOUR_AUTHTOKEN` with the actual token you copied from the ngrok dashboard.

#### 4. Start an HTTP Tunnel

- With your authtoken set up, start the HTTP tunnel:
  ```bash
  ngrok http 8000
  ```

- ngrok will display output similar to this:
  ```
  ngrok by @inconshreveable

  Session Status                online
  Session Expires               1 hour, 59 minutes
  Version                       2.3.35
  Region                        United States (us)
  Web Interface                 http://127.0.0.1:4040
  Forwarding                    http://abcd1234.ngrok.io -> http://localhost:8000
  Forwarding                    https://abcd1234.ngrok.io -> http://localhost:8000

  Connections                   ttl     opn     rt1     rt5     p50     p90
                                 0       0       0.00    0.00    0.00    0.00
  ```

- Use the `http://abcd1234.ngrok.io` URL provided by ngrok for external access.

By following these steps, you can make your local server accessible over the internet without the need for a credit card. This method will allow your friends to connect to your game server globally. If you encounter any issues, please let me know, and I can help troubleshoot further.

---

Here's an example of how to extend the previous script to handle a simple form submission dynamically:

### HTML File (index.html)

Update your `index.html` file to include a simple form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Web Page</title>
</head>
<body>
    <h1>Welcome to My Web Page</h1>
    <p>This is a simple web page served using Python and ngrok.</p>
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

### Modified Python Script

Extend your Python script to handle form submission:

```python
#!/usr/bin/env python

from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
from pyngrok import ngrok
import urllib.parse

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.protocol_version = "HTTP/1.1"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        try:
            with open("index.html", "rb") as file:  # Open the HTML file
                body = file.read()  # Read the HTML file content
            self.send_header("Content-Length", len(body))
            self.end_headers()
            self.wfile.write(body)  # Send the HTML content
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(bytes(f"Error: {str(e)}", "utf-8"))

    def do_POST(self):
        self.protocol_version = "HTTP/1.1"
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode('utf-8'))
        
        name = data.get('name', [''])[0]

        response = f"Hello, {name}!"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(response))
        self.end_headers()
        self.wfile.write(bytes(response, "utf-8"))

logging.basicConfig(level=logging.INFO)
server = HTTPServer(("localhost", 8000), HelloHandler)

# Open a ngrok tunnel to the HTTP server
http_tunnel = ngrok.connect(8000)
print("ngrok tunnel \"{}\" -> \"http://localhost:8000\"".format(http_tunnel.public_url))

server.serve_forever()
```

### Explanation

1. **Form in HTML**: The `index.html` file now includes a simple form that submits to `/submit` via POST.
2. **Handler Modification**: The `HelloHandler` class is extended to handle POST requests.
3. **do_POST Method**:
   - Reads the content length and the POST data.
   - Parses the POST data to extract form values.
   - Generates a response based on the submitted data.
   - Sends the response back to the client.

### Running the Script

Run the script as before:

```bash
export NGROK_AUTHTOKEN=2iz***********************74b
python example.py
```

### Accessing the Web Page and Submitting the Form

1. **Start the Script**: Make sure the script is running.
2. **Open the Public URL**: Use the URL provided by ngrok (e.g., `http://abcd1234.ngrok.io`).
3. **Submit the Form**: Enter a name in the form and submit it.
4. **View the Response**: You should see a dynamic response that greets you with the name you entered.

This setup demonstrates how to handle both static content and dynamic form submissions with a simple HTTP server in Python, making your web page interactive. If you need further customization or more advanced features, feel free to ask!
