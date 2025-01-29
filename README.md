# My FastAPI Application

This is a simple FastAPI application that handles CORS and returns JSON output with the registered email address, current datetime, and GitHub URL.

## Project Structure

```
my-fastapi-app
├── app
│   ├── main.py          # Entry point of the FastAPI application
│ 
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Celnet-hub/hng12-pub-api.git
    cd hng12-pub-api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the application

1. Start the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/info` to see the JSON output.

## Deployment to AWS

### Using `systemd`

1. **Set Up a Virtual Private Server (VPS):**
   - Log in to your AWS account.
   - Navigate to the EC2 service and create a new instance.
   - Choose an operating system (e.g., Ubuntu).

2. **Connect to Your EC2 Instance:**
   - Use an SSH client (the terminal on macOS/Linux) to connect to your VPS.
   - Example command:
     ```bash
     ssh root@your_vps_ip_address
     ```

3. **Install Dependencies:**
   - Update the package list and install Python and pip:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

   - Install `uvicorn` and `fastapi`:
     ```bash
     pip3 install fastapi uvicorn
     ```

4. **Upload Your FastAPI Application:**
   - git clone the repository.
     ```bash
      git clone https://github.com/Celnet-hub/hng12-pub-api.git
      cd hng12-pub-api
     ```

5. **Create a systemd Service File:**
   - Create a new service file for your FastAPI application:
     ```bash
     sudo nano /etc/systemd/system/fastapi.service
     ```

6. **Add the Service Configuration:**
   - Add the following content to the `fastapi.service` file. Make sure to replace the placeholders with your actual paths and user information:
     ```ini
     [Unit]
     Description=FastAPI application
     After=network.target

     [Service]
     User=your_username
     Group=www-data
     WorkingDirectory=/path/to/your/app
     ExecStart=/usr/bin/env uvicorn app.main:app --host 0.0.0.0 --port 8000
     Restart=always

     [Install]
     WantedBy=multi-user.target
     ```

7. **Reload systemd and Start the Service:**
   - Reload the systemd daemon to recognize the new service:
     ```bash
     sudo systemctl daemon-reload
     ```

   - Start the FastAPI service:
     ```bash
     sudo systemctl start fastapi
     ```

   - Enable the service to start on boot:
     ```bash
     sudo systemctl enable fastapi
     ```

8. **Check the Service Status:**
   - You can check the status of your FastAPI service to ensure it is running correctly:
     ```bash
     sudo systemctl status fastapi
     ```

9. **Set Up a Reverse Proxy (Optional):**
   - To make your application accessible via a domain name, you can set up a reverse proxy using Nginx.
   - Install Nginx:
     ```bash
     sudo apt install nginx
     ```

   - Configure Nginx to proxy requests to your FastAPI application. Edit the Nginx configuration file (e.g., `/etc/nginx/sites-available/default`):
     ```nginx
     server {
         listen 80;
         server_name your_aws_domain.com;

         location / {
             proxy_pass http://127.0.0.1:8000;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     ```

   - Restart Nginx to apply the changes:
     ```bash
     sudo systemctl restart nginx
     ```

10. **Access Your Application:**
    - Your FastAPI application should now be accessible via your domain name or VPS IP address.

## API Endpoints

### GET /info

Returns a JSON object with the following information:
- `email`: Your registered email address.
- `timestamp`: The current datetime as an ISO 8601 formatted timestamp.
- `github_url`: The GitHub URL of the project's codebase.

Example response:
```json
{
    "email": "dubemnwabuisi@gmail.com",
    "timestamp": "2023-10-05T12:34:56.789Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```