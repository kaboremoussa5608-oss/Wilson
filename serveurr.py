from flask import Flask, request

app = Flask(__name__)

# On définit un style CSS pour que ce soit beau
STYLE_CSS = '''
<style>
    body { font-family: sans-serif; background-color: #f4f4f4; text-align: center; padding: 50px; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
            h1 { color: #e67e22; }
                select, input { padding: 10px; margin: 10px; border-radius: 5px; border: 1px solid #ddd; width: 80%; }
                    input[type="submit"] { background-color: #27ae60; color: white; border: none; cursor: pointer; font-weight: bold; }
                        input[type="submit"]:hover { background-color: #2ecc71; }
                        </style>
                        '''

@app.route('/')
def home():
    return STYLE_CSS + '''
                                    <div class="card">
                                                <h1>🍕 Ma Pizzeria Interactive</h1>
                                                            <form action="/commande" method="post">
                                                                            <p>Votre nom :</p>
                                                                                            <input type="text" name="client_name" placeholder="Ex: Moussa" required>

                                                                                                                            <p>Choisissez votre pizza :</p>
                                                                                                                                            <select name="pizza_type">
                                                                                                                                                                <option value="Royale 👑">Royale</option>
                                                                                                                                                                                    <option value="4 Fromages 🧀">4 Fromages</option>
                                                                                                                                                                                                        <option value="Végétarienne 🥗">Végétarienne</option>
                                                                                                                                                                                                                            <option value="Piquante 🔥">Piquante</option>
                                                                                                                                                                                                                                            </select>

                                                                                                                                                                                                                                                                            <br>
                                                                                                                                                                                                                                                                                            <input type="submit" value="Envoyer la commande">
                                                                                                                                                                                                                                                                                                        </form>
                                                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                                                    '''

@app.route('/commande', methods=['POST'])
def commande():
    nom = request.form.get('client_name')
    pizza = request.form.get('pizza_type')
    return STYLE_CSS + f'''
                                                                                                                                                                                                                                                                                                                                        <div class="card">
                                                                                                                                                                                                                                                                                                                                                    <h1>Confirmation ✅</h1>
                                                                                                                                                                                                                                                                                                                                                                <p>Merci <b>{nom}</b> !</p>
                                                                                                                                                                                                                                                                                                                                                                            <p>Ta pizza <b>{pizza}</b> arrive dans 20 minutes.</p>
                                                                                                                                                                                                                                                                                                                                                                                        <a href="/">Passer une autre commande</a>
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                                                                                                                                                                                                                                                                                                                                                                                    '''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
                                                                                                                                                                                                                                                                                                                                                                                                        
