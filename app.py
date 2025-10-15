from flask import Flask, request, jsonify
from deterministic_engine import DeterministicInterventionEngine  # Import your V8 class

app = Flask(__name__)

# Default state (customize with user sessions later)
default_state = {
    'IntrinsicState': {'Mood': 5.0, 'CognitiveClarity': 5.0, 'PhysicalEnergy': 5.0},
    'ExternalFitness': {'ResourceBalance': 5.0, 'SocialCohesion': 5.0, 'EnvironmentalImpact': 5.0},
    'MeritScore': {'ProSocialActions': 5.0, 'NoHarmCompliance': 5.0}
}

@app.route('/advise', methods=['POST'])
def advise():
    data = request.json
    P = data.get('problem', 'General harmony boost')
    state = data.get('state', default_state)
    
    engine = DeterministicInterventionEngine(state)
    # Run engine and get result (adapt from your run_engine)
    F_A, F_B = engine.decompose_problem(P)
    candidates = engine.generate_candidates(F_A, F_B)
    filtered = engine.filter_candidates(candidates)
    best_a, message = engine.optimize_action(filtered)
    
    if best_a:
        response = {
            'action': best_a['name'],
            'message': message,
            'new_harmony': engine.calculate_harmony()  # Simulate update
        }
    else:
        response = {'action': 'Breathe deeply with Mettā', 'message': 'Fallback for harmony'}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
