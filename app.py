from flask import Flask, render_template

app = Flask(__name__)

portfolio_data = {
    'name': 'Aditya B Pattavardhanam',
    'bio': '1st Sem ECE | Avgeek | Python Enthusiast',
    'interests': ['Web Development ', 'Guitar', 'Table Tennis'],
    'experience': [
        {'title': 'MARVEL R&D Lab',
            'description':'Student of Batch 4 in the Design and Prototyping Domain'},
        {'title': 'TEDxUVCE',
            'description': 'Member of the Relations and Sponsorship team'},
    ],
    'projects': [
        {'title': 'Smart City Project',
            'description': 'Designed a smart city in the Thar desert using Minecraft:Education Editition. Presented the idea at IIHS, Bengaluru'},
        {'title': 'Microsoft Imagine Cup Junior 2020',
            'description': 'Designed a pair of glasses which does multiple tasks and helps the blind person.'},
        {'title': 'KAGADA - 2023 by IEEE UVCE',
            'description':'Designed a prototype that converts waste heat from railway tracks to electricity. Won 1st place'},
    ],
    'social_media': {
        'GitHub': 'https://github.com/Pattavardhanam',
        'Instagram': 'https://www.instagram.com/pattavardhanam17/',
        'LinkedIn':'https://www.linkedin.com/in/aditya-pattavardhanam/',
        'Twitter':'https://twitter.com/pattavardhanam'
    },
}


@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)


if __name__ == '__main__':
    app.run(debug=True)
