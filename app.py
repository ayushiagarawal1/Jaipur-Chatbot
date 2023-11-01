from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello , how are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["Yes, sure I can help you ",]
    ],
     [
        r"(.*)your name",
        ["I dont have any name, but Ayushi gave me a nickname - Chatzy ",]
    ],
    [
        r"how are you(.*)?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry(.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*)created(.*)",
        ["Ayushi Agarwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*)(location|city)(.*)",
        ['Jaipur, India',]
    ],
    [
        r"(.*)(located| situated)(.*)",
        ["Jaipur is the capital city of the northwestern Indian state of Rajasthan."]
    ],
    [
        r"what(.*)nickname(.*)",
        ["Jaipur is often referred to as the 'Pink City' due to the pink color of its historical buildings."]
    ],
    [
        r"(.*)(tourist attractions| famous tourist places | tourist places)(.*)",
        ["Jaipur is known for its historical landmarks, including the Hawa Mahal, City Palace, Amber Fort, Jantar Mantar, and Nahargarh Fort."]
    ],
    [
        r"(.*)(culture|traditions)(.*)",
        ["Jaipur has a rich cultural heritage, with traditional music, dance, and art forms. The city is known for its vibrant festivals, including Diwali and Holi."]
    ],
    [
        r"(.*)(best time|visit)(.*)",
        ["The best time to visit Jaipur is during the winter months, from October to March, when the weather is pleasant and comfortable."]
    ],
    [
        r"(.*)cuisine(.*)",
        ["Jaipur offers a variety of traditional Rajasthani dishes, including Dal Baati Churma, Gatte ki Sabzi, and the famous Rajasthani sweets like Ghevar and Mawa Kachori."]
    ],
    [
        r"(.*)(history|background|backstory)(.*)",
        ["Jaipur was founded in 1727 by Maharaja Sawai Jai Singh II and is known for its well-planned layout and architecture."]
    ],
    [
        r"(.*)(significance|importance)(Hawa Mahal)(.*)",
        ["Hawa Mahal, or the 'Palace of Winds,' is an iconic structure in Jaipur known for its unique architecture with numerous small windows. It was built for the royal women to observe street festivals and processions without being seen."]
    ],
    [
        r"(.*)reach(.*)",
        ["Jaipur is well-connected by air, rail, and road. The city has an international airport, a major railway station, and good road connectivity."]
    ],
    [
        r"(.*)(famous markets|shopping areas )(.*)",
        ["Yes, Jaipur is famous for its markets, such as Johari Bazaar and Bapu Bazaar, where you can buy traditional Rajasthani jewelry, textiles, and handicrafts."]
    ],
    [
        r"(.*)(nearby tourist)(destinations|places)",
        ["You can visit places like Jodhpur, Udaipur, Ajmer, Pushkar, and Ranthambore National Park, which are easily accessible from Jaipur."]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
        [
        r"(.*)top festivals(.*)",
        ["Some of the major festivals celebrated in Jaipur include Diwali, Holi, Teej, and Gangaur, which are marked with grand processions and cultural events."]
    ],
    [
        r"(.*)(government|administration| govt| gov|admin)(.*)",
        ["Jaipur serves as the capital of the Indian state of Rajasthan and is governed by a Chief Minister Ashok Gehlot and a legislative assembly. It is an important administrative and political center for the state."]
    ],
    [
        r"(.*)(activities for tourists)(.*)",
        ["Tourists in Jaipur can enjoy activities like elephant rides at Amber Fort, hot air balloon rides, shopping in the local markets, and exploring the rich heritage of the city."]
    ],
    [
        r"(.*)(architecture style)(Jantar Mantar)(.*)",
        ["Jantar Mantar is an astronomical observatory in Jaipur and is known for its unique and intricate stone instruments used for measuring time and tracking celestial bodies. It's a UNESCO World Heritage site."]
    ],
    [
        r"(.*)(annual| cultural | tourists | attend) events (.*) ",
        ["Yes, the Jaipur Literature Festival and Jaipur International Film Festival are popular annual cultural events that attract tourists and scholars from around the world."]
    ],
    [
        r"(.*)historical facts(.*)",
        ["Jaipur is named after Maharaja Sawai Jai Singh II, who founded the city in 1727. It was one of the earliest planned cities in India and is known for its grid-based layout and stunning architecture."]
    ],
    [
        r"(.*) (significance)(.*) (City Palace)(.*)",
        ["The City Palace is a historic royal residence in Jaipur, known for its stunning architecture and the Chandra Mahal and Mubarak Mahal. It also houses a museum showcasing royal artifacts."]
    ],
    [
        r"(.*)(attire| clothing| clothes| traditional attire)(.*)",
        ["The traditional attire for women in Jaipur includes the vibrant and colorful Rajasthani sarees and lehengas. Men often wear turbans (safas) and dhotis."]
    ],
    [
        r"(.*)(historical significance)(Amber Fort)(.*)",
        ["Amber Fort is a majestic hilltop fort near Jaipur. It was the capital of the Kachwaha Rajputs and is renowned for its artistic elements and panoramic views of the surrounding area."]
    ],
    [
        r"(.*)traditional dance(.*)",
        ["Jaipur is known for the traditional dance form of 'Kathak,' which is characterized by intricate footwork and storytelling through dance movements."]
    ],
    [
        r"(.*)",
        ['I am not sure about the answer. I m really sorry']
    ],
]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']
    response = chat.respond(user_query)
    return render_template('index.html', response=response)

if __name__ == "__main__":
    # Create Chat Bot
    chat = Chat(pairs, reflections)
    app.run(debug=True)
