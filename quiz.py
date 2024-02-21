import random
topics=["history", "science", "math", "sports", "music"]
questions= {
    "history":{
        "multiple_choice":[
            {
                "question": 'who is known for the famous saying "i have a dream": ',
                "options":['Martin Luther King', 'Malcom X', "Barrack Obama", "Micheal Jackson"],
                "answer": "Martin Luther king Jr"
            },
            {
                "question": "Who was the first female Prime Minister of the United Kingdom? ",
                "options": ["Margaret Thatcher", "Queen Elizabeth I", " Angela Merkel", "Golda Meir"],
                "answer": "Margaret Thatcher"
            },
            {
                "question": "How many countries are there in africa? ",
                "options":["34", "45", "54", "12"],
                "answer": "54"
            },
            {
                "question": "The construction of which famous landmark was completed in 1889 in Paris? ",
                "options": [" Colosseum", "Eiffel Tower", "Statue of Liberty", "Big Ben"],
                "answer": "Eiffel Tower"
            },
            {
                "question": "Which ancient civilization built the Great Pyramid of Giza, one of the Seven Wonders of the Ancient World? ",
                "options": ["Benin civilization", "Nubian civilization", "Carthaginian civilization", "Egyptian civilization"],
                "answer": "Egyptian civilization"
            }
        ],
        "theory":[
            {
                "question": "Who was the first man to walk on the moon? ",
                "answer": "Neil Armstrong."
            },
            {
                "question": "What is the capital city of France? ",
                "answer": "Paris"
            },
            {
                "question": "Who wrote the play Romeo and Juliet ?",
                "answer": "William Shakespeare."
            },
            {
                "question": "What year did the Titanic sink? ",
                "answer": "1912"
            },
            {
                "question": "What is the second largest continent? ",
                "answer": ""
            }
        ]
    },
    "science":{
        "multiple_choice": [
            {
                "question": "What is the chemical symbol for water? ",
                "options":[" CH4", " CO2", " H2O2", " H2O"],
                "answer": " H2O"
            },
            {
                "question": "What is the process by which plants make their food called? ",
                "options":["Decomposition", "Photosynthesis", "Respiration", "Transpiration"],
                "answer": "Photosynthesis"
            },
            {
                "question": "What force keeps objects on the Earth's surface? ",
                "options":[" Gravity", "Friction", "Inertia", " Magnetism"],
                "answer": " Gravity"
            },
            {
                "question": "Which organ in the human body is responsible for pumping blood? ",
                "options":["Nose", "Kidney", "Lungs", "Heart"],
                "answer": "Heart"
            },
            {
                "question": "What is the closest planet to the Sun? ",
                "options":["Earth", "Mercury", " Mars", "Venus"],
                "answer": "Mercury"
            }
        ],
        "theory":[
            {
                "question": "What is the center of an atom called? ",
                "answer": "nucleus"
            },
            {
                "question": "What type of energy is stored in a battery? ",
                "answer": " Chemical energy"
            },
            {
                "question": "What is the hardest natural substance on Earth? ",
                "answer": "Diamond"
            },
            {
                "question": "What is the process of liquid turning into vapor at the surface of a liquid called? ",
                "answer": "Evaporation"
            },
            {
                "question": "What is the largest organ in the human body? ",
                "answer": "skin"
            }
        ]
    },
    "math":{
        "multiple_choice":[
            {
                "question": "The ratio of boys to girls in a class is 3:5. If there are 24 students in the class, how many girls are there? ",
                "options" : ["9", "12", "15", "18"],
                "answer" : "18"
            },
            {
                "question": "A circle has a radius of 6 cm. What is its circumference? ",
                "options" : ["6π cm", "12π cm", "36π cm", " 18π cm"],
                "answer" : "12π cm"
            },
            {
                "question": "What is 5+3? ",
                "options" : ["6", "8", "22", "4"],
                "answer" : "8"
            },
            {
                "question": "What is 2×4? ",
                "options" : ["3", "5", "8", "9"],
                "answer" : "8"
            },
            {
                "question": "What is 10÷2? ",
                "options" : ["0.5", "5", "7", "45"],
                "answer" : "5"
            }
        ],
        "theory":[
            {
                "question": "What is the sum of the angles in a quadrilateral? ",
                "answer": "360"
            },
            {
               "question": "What is the formula for the circumference of a circle? ",
                "answer": "2πr" 
            },
            {
                "question": "What is the smallest prime number? ",
                "answer": "2"
            },
            {
                "question": " What is the next number in the sequence: 2, 4, 6, 8, ___? ",
                "answer": "12"
            },
            {
                "question": "What is the value of the square root of 16? ",
                "answer": " 4"
            }
        ]
    },
    "sports":{
        "multiple_choice":[
            {
                "question": "Which country won the FIFA World Cup in 2018? ",
                "options" : ["Germany", "Argentina", "Brazil", "France"],
                "answer" : "France"
            },
            {
                "question": "In which sport is the term slam dunk commonly used? ",
                "options" : ["Basketball", "Tennis", " Golf", "Soccer"],
                "answer" : "Basketball"
            },
            {
                "question": "Who holds the record for the most Olympic gold medals of all time? ",
                "options" : ["Usain Bolt", "Carl Lewis", "Simone Biles", "Michael Phelps"],
                "answer" : "Michael Phelps"
            },
            {
                "question": "Who won the 2020 NBA Finals? ",
                "options" : ["Toronto Raptors", " Los Angeles Lakers", "Miami Heat", "Golden State Warriors"],
                "answer" : " Los Angeles Lakers"
            },
            {
                "question": "Which of the following countries has won the FIFA World Cup the most times? ",
                "options" : ["Argentina", "Germany", " Brazil", "Nigeria"],
                "answer" : " Brazil"
            }
        ],
        "theory":[
            {
                "question": " What sport is played at Wimbledon? ",
                "answer": "Tennis"
            },
            {
               "question": " In soccer, how many players are on the field for each team during a match? ",
                "answer": "11" 
            },
            {
                "question": "What sport is known as The Gentleman's Game? ",
                "answer": "cricket"
            },
            {
                "question": "What is the term used in soccer for intentionally using one's head to direct the ball? ",
                "answer": "Heading"
            },
            {
                "question": "In which sport is the term deuce used to indicate a tied score?",
                "answer": "Tennis"
            }
        ]
    },
    "music":{
        "multiple_choice":[
            {
                "question": "In which African country did the music genre known as Afrobeat originate, popularized by artists like Fela Kuti? ",
                "options" : ["Senegal", "Ghana", "Nigeria", "Tanzania"],
                "answer" : "Nigeria"
            },
            {
                "question": "What is the name of the Nigerian musician who won the Grammy Award for Best World Music Album in 2019 for his album African Giant? ",
                "options" : ["Davido", "BurnaBoy", "Tems", "Maggix"],
                "answer" : "BurnaBoy"
            },
            {
                "question": "Who is often referred to as the King of Pop and is known for hit songs like Thriller, Billie Jean, and Beat It? ",
                "options" : ["Micheal Jackson", "SZA", "Lewis Capaldi", "Elvis Presley"],
                "answer" : "Micheal Jackson"
            },
            {
                "question": "Who composed the famous classical piece Symphony No. 5 in C minor, known for its distinctive opening motif ?",
                "options" : ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Pyotr Ilyich Tchaikovsky"],
                "answer" : "Ludwig van Beethoven"
            },
            {
                "question": "Who is known as the Queen of Soul and is famous for songs like Respect and Natural Woman? ",
                "options" : ["Aretha Franklin", "Diana Ross", "Whitney Houston", "Etta James"],
                "answer" : "Aretha Franklin"
            }
        ],
        "theory":[
            {
                "question": "Who was the lead vocalist of the band Queen? ",
                "answer": " Freddie Mercury."
            },
            {
               "question": "What term is used to describe the written symbols representing music's pitch, duration, and other musical elements? ",
                "answer": "Musical notation." 
            },
            {
                "question": "What is the name of the woodwind instrument known for its distinctive curved shape and rich, mellow tone? ",
                "answer": "Saxophone"
            },
            {
                "question": "What is the name of the string instrument that is the smallest and highest-pitched member of the violin family?",
                "answer": "Violin"
            },
            {
                "question": "What is the name of the instrument often referred to as the king of instruments due to its versatility and range? ",
                "answer": "Piano"
            }
        ]
    }
}