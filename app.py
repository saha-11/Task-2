from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Application</title>

        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Segoe UI, sans-serif;
            }

            body{
                background:#0f172a;
                color:white;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }

            .card{
                background:#1e293b;
                width:400px;
                padding:40px;
                border-radius:20px;
                text-align:center;
                box-shadow:0 10px 30px rgba(0,0,0,0.4);
            }

            .logo{
                font-size:60px;
                margin-bottom:15px;
            }

            h1{
                font-size:32px;
                margin-bottom:10px;
            }

            p{
                color:#cbd5e1;
                margin-bottom:25px;
                line-height:1.5;
            }

            .status{
                background:#22c55e;
                color:white;
                padding:10px;
                border-radius:10px;
                margin-bottom:20px;
                font-weight:bold;
            }

            button{
                background:#3b82f6;
                border:none;
                color:white;
                padding:12px 25px;
                border-radius:10px;
                font-size:16px;
                cursor:pointer;
                transition:0.3s;
            }

            button:hover{
                background:#2563eb;
                transform:scale(1.05);
            }

            .footer{
                margin-top:20px;
                font-size:14px;
                color:#94a3b8;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <div class="logo">⚡</div>

            <h1>Flask Application</h1>

            <p>
                This is a simple web application created using Python Flask.
            </p>

            <div class="status">
                Server Running Successfully
            </div>

            <button onclick="showMessage()">
                Check Status
            </button>

            <div class="footer">
                Developed by Sahana Sharon
            </div>

        </div>

        <script>
            function showMessage(){
                alert("Flask Application is Active!");
            }
        </script>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)