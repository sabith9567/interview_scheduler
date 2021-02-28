# interview_scheduler

### interview scheduler using django rest framework - DRF

## Endpoints

### 1. api/register-time-slot
POST METHOD

PARAMS  

user
start_time
end_time
available_date

Creates time slot for candidate/interviewer

### 2. api/get-time-slot
POST METHOD

PARAMS

candidate_id
interviewer_id

Filter and return the available time slots of both interviewer and candidate

## To run this project locally

## Dependencies
- python3.5+

1.Clone this repo
```bash
https://github.com/sabith9567/interview_scheduler.git && cd interview_scheduler
```
2.Install requirements
```bash
pip install -r requirements.txt
```
3.Migrate
```bash
python manage.py migrate
```
4.Create superuser
```bash
python manage.py createsuperuser
```
loging into django admin via admin/ endpoint with admin credentials you created also create user as candidate and interviewer ( with field is_interviewer=True ). and using the api  create TimeSlots corresponding to user

5.Run
```bash
python manage.py runserver
```
check the api using postman 




