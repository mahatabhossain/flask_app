from apscheduler.schedulers.background import BackgroundScheduler
from flask import request, jsonify
from model import Job_schedular
from dotenv import load_dotenv
from datetime import datetime,timedelta

load_dotenv()
scheduler = BackgroundScheduler()
scheduler.start()

# date: use when you want to run the job just once at a certain point of time
# interval: use when you want to run the job at fixed intervals of time
# cron: use when you want to run the job periodically at certain time(s) of day

seconds = 2
minutes = 1
hours = 1

def hello_world():
    print("Data stored into database",datetime.now() )

def create_job():
    try:
        body = request.get_json()
        name = body['job_name']
        current_time = datetime.now() + timedelta(seconds=155555)
        print(f'App schedular is running in every {seconds} seconds')
        print('Current time', current_time)
        job_details = Job_schedular(job_name=name, time=current_time)
        job_details.save()
        scheduler.add_job(hello_world, 'date',run_date=current_time,id=str(job_details.id))
        return 'Data saved'
    except Exception as e:
        print( e)
        return 'data saved failed'

def edit_job(id):
    try:
        job_id = id
        print('Edit job called', job_id)
        job_details = Job_schedular.Objects.get_or_404(_id=job_id)
        print('Job details fetched')
        return jsonify({'status': 'success', 'job_details':job_details})
    except Exception as e:
        print('job details error', e)
        return e

def populate_jobs():
    # TODO: fetch all the schedules older than current time then populate to apscheduler
    
    return

