import csv
from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)
print(__name__)

@app.route('/')  #root directory--points to home/base of the application when it opens on browser
def savory_home():
    return render_template('index_savory.html')

# @app.route('/about_savory.html')  #root directory--points to home/base of the application when it opens on browser
# def about():
#     return render_template('about_savory.html')
#
#
# @app.route('/components.html')  #root directory--points to home/base of the application when it opens on browser
# def components():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')  #root directory--points to home/base of the application when it opens on browser
# def contact():
#     return render_template('contact.html')

#
# @app.route('/services.html')  #root directory--points to home/base of the application when it opens on browser
# def services():
#     return render_template('services.html')


@app.route('/<string:page_name>') #to dynamically create html page as entered from browser
def html_page(page_name):
    return render_template(page_name)

def write_to_database(data):
    with open ('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database2.csv', newline='', mode='a') as database2: #to add entries to new line below header in csv file
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=(['POST','GET'])) #to capture user entered data in contact.html
def submit_form():
    #return 'Form submitted !!!'
    if request.method=="POST":
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')
    else:
        return "Somehing went wrong, please try again :("






