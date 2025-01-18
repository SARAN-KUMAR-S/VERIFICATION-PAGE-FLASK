from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load certificate data (Replace with your actual data)
certificate_data = pd.read_csv("certificates1.csv")

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Certificate Verification Portal</title></head>
        <body>
            <h1>🎓 Certificate Verification Portal</h1>
            <form action="/verify" method="post">
                <label for="cert_code">Enter Certificate Code:</label>
                <input type="text" id="cert_code" name="cert_code" placeholder="E.g., ABC123" required>
                <input type="submit" value="Verify Certificate">
            </form>
        </body>
    </html>
    '''

@app.route('/verify', methods=['POST'])
def verify_certificate():
    cert_code = request.form['cert_code']

    if cert_code:
        # Check if the certificate code exists in the data
        record = certificate_data[certificate_data['user_nicename'] == cert_code]
        if not record.empty:
            return f"""
            <html>
                <body>
                    <div style="background-color: #d4edda; padding: 10px; border-radius: 5px; border: 1px solid #c3e6cb;">
                        <h2>Certificate Verified Successfully! 🎉</h2>
                        <ul>
                            <li><b>Name:</b> {record.iloc[0]['user_email']}</li>
                            <li><b>Course Name:</b> {record.iloc[0]['display_name']}</li>
                            <li><b>Issue Date:</b> {record.iloc[0]['user_nicename']}</li>
                        </ul>
                    </div>
                </body>
            </html>
            """
        else:
            return """
            <html>
                <body>
                    <div style="background-color: #f8d7da; padding: 10px; border-radius: 5px; border: 1px solid #f5c6cb;">
                        <h2>❌ Invalid Certificate Code!</h2>
                        <p>Please check your code and try again.</p>
                    </div>
                </body>
            </html>
            """
    else:
        return '''
        <html>
            <body>
                <div style="background-color: #fff3cd; padding: 10px; border-radius: 5px; border: 1px solid #ffeeba;">
                    <h2>⚠️ Please enter a certificate code to verify.</h2>
                </div>
            </body>
        </html>
        '''

if __name__ == '__main__':
    app.run(debug=True)
