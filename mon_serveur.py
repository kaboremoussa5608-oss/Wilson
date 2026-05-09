from flask import Flask, request

app = Flask(__name__)

# Page d'accueil avec un formulaire
@app.route('/')
def home():
    return '''
            <h1>Pizzeria en ligne</h1>
                    <form action="/commande" method="post">
                                <p>Quel est votre nom ?</p>
                                            <input type="text" name="client_name">
                                                        <input type="submit" value="Commander">
                                                                </form>
                                                                    '''

                                                                    # Page qui reçoit les données du formulaire
@app.route('/commande', methods=['POST'])
def commande():
                                                                        # On récupère le nom tapé dans le formulaire
        nom = request.form.get('client_name')
        return f"<h1>Merci {nom} !</h1><p>Votre pizza est en préparation... 🍕</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
                                                                                                                                                                         
    app.run(host='0.0.0.0', port=5000)                
    
