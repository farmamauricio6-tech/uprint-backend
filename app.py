from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('DB_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.getenv('DB_NAME', 'edufast')

mysql = MySQL(app)

# Import controllers
from controllers.estudiantes_controller import estudiantes_bp

# Register blueprints
app.register_blueprint(estudiantes_bp)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'EduFast API - Sistema de Gestión de Estudiantes'}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint no encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)