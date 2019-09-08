from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_dojo_survey.html')

@app.route('/result', methods=['POST'])
def user_survey():
    print('Got Post Info')
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    experience_from_form = request.form['experience']
    learn_from_form = request.form.getlist('learn')
    
    return render_template('show_dojo_survey.html', name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comment_on_template=comment_from_form, experience_on_template=experience_from_form, learn_on_template=learn_from_form)


if __name__=="__main__":
    app.run(debug=True)
