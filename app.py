import os
from flask import Flask, jsonify, render_template
from routes.auth_routes import auth_bp
from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(patient_bp, url_prefix='/api/patient')
app.register_blueprint(doctor_bp, url_prefix='/api/doctor')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/dashboard/patient')
def patient_dashboard():
    return render_template('patient_dashboard.html')

@app.route('/dashboard/doctor')
def doctor_dashboard():
    return render_template('doctor_dashboard.html')

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
