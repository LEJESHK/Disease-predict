from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict_disease():
    final_prediction = None
    final_specialist = None
    symptoms_entered = ''
    symptoms = [
        "Headache", "Fever", "Cough", "Cold", "Fatigue", "Vomiting", "Dizziness", "Chest pain",
        "Shortness of breath", "Nausea", "Back pain", "Loss of appetite", "Muscle pain"
    ]  # Add more symptoms if needed

    if request.method == 'POST':
        symptoms_entered = request.form['symptoms']
        
        # Dummy prediction logic for now
        final_prediction = "Typhoid"  # Replace with actual prediction logic
        final_specialist = "General Physician"

    return render_template("index.html",
                           symptoms_entered=symptoms_entered,
                           final_prediction=final_prediction,
                           final_specialist=final_specialist,
                           symptoms=symptoms,
                           request=request)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
