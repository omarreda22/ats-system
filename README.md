
# APPLICATION TRACKING SYSTEM ( ATS ) with Django <img src="https://c.tenor.com/SOVMSXmWB1kAAAAi/tony-star-jumping.gif" width="35"><br>

ATS simplifies recruitment, With smarter search, AI-powered ranking, and seamless candidate management, ATS is transforming recruitment into a faster, more transparent, and candidate-friendly journey.

### 📌 Home Page View (The user enters a job description and uploads a resume): 
![APPLICATION TRACKING SYSTEM Home](https://github.com/omarreda22/ats-system/blob/main/core/static/images/one.PNG)



### 📌 Results Page View (Match Percentage - Skills to Improve - Final Thoughts - Recommendations): 
![APPLICATION TRACKING SYSTEM Results](https://github.com/omarreda22/ats-system/blob/main/core/static/images/two.PNG)

### 📌 Video Demo:
<p align="center">
  <img align="center" src="https://github.com/omarreda22/ats-system/blob/main/core/static/images/ats.gif">
</p>

## How it work <img src="https://media.giphy.com/media/mBYkXvLxkHZFmqBHIC/giphy.gif" width=50px height=40px> 
The user enters a job description and uploads a resume.
- The resume (PDF or DOCX) is converted into a clean text string for processing.
- Both the job description and resume text are then passed to the AI model for analysis.
- The AI response is processed and refined into clear outputs:
  - Match Percentage
  - Skills to Improve
  - Final Thoughts
  - Recommendations
- Modern UI Templates – Results are displayed in clean, user-friendly templates for recruiters and candidates.



## How to install on Windows <img src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Rocket.gif" width="29px">
1. clone this project
2. install virtualenv
```
pip install virtualenv
```
3. create new virtual environment
```
py -m venv venv
```
4. activate the new virtual
```
.\venv\Scripts\activate
```
5. install requirements.txt
```
pip install -r requirements.txt
```
6. run local server to begin
 ```
 py manage.py runserver
 ```
 7. go live with [localhost:8000](http://localhost:8000/)
 
 ### To install on Unix/macOS  [see this document](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments)
 
