import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-for-medtrack')
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# DynamoDB Table Names
DYNAMODB_PATIENTS_TABLE = os.environ.get('DYNAMODB_PATIENTS_TABLE', 'MedTrack_Patients')
DYNAMODB_DOCTORS_TABLE = os.environ.get('DYNAMODB_DOCTORS_TABLE', 'MedTrack_Doctors')
DYNAMODB_APPOINTMENTS_TABLE = os.environ.get('DYNAMODB_APPOINTMENTS_TABLE', 'MedTrack_Appointments')
DYNAMODB_DIAGNOSIS_TABLE = os.environ.get('DYNAMODB_DIAGNOSIS_TABLE', 'MedTrack_Diagnosis')

# SNS Topic ARN
SNS_NOTIFICATION_TOPIC_ARN = os.environ.get('SNS_NOTIFICATION_TOPIC_ARN')
