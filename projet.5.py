from flask import Flask
from flask_ask import Ask, statement, question
app = Flask(__name__)
ask = Ask(app, '/')
@ask.launch
def start():
    return question('Quel playlist désirez vous?')
@ask.intent('HelloIntent')
def bonjour(nom):
    if nom is None:
        return statement('Je ne connais pas ce nom, désolé')
    return statement("Bonjour {}".format(nom))
@ask.intent('MusicIntent')
def son(activite):
    if activite is None:
        return statement('je ne comprend pas ce type')
    elif 'dormir' in activite:
        return statement ('controla by drake, lavish lullaby by masego, sweet thing by Ylti and time goes down by flipp Dinero ')

    elif 'soirée' in activite:
        return statement ('baller by Luke Nasty, Time by Darrell Cole, Umbrella by rhianna, Hold the Line by toto and Come as you are by Nirvana ')

    elif 'étude' in activite:
        return statement('yosemite by Travis scott, Wake up by travis scott, Lac des sygnes by Laura silberberg, Tadow by masego and Trip by Ella may')

    elif 'sport' in activite:
        return statement('El chapo by The game, In Da club by fifty cents, No stylist by French Montana, I like It by cardi B and Potentiel by Lefa')

@ask.intent('NoteIntent')
def point(note):
    if note <= 5:
        return statement('Merci , nous allons nous améliorer')
    else:
        return statement('merci de votre confiance')

if __name__ == '__main__':
    app.run()