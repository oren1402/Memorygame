'''
import os
import time
import random
import streamlit as st



def effacer_ecran():
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def generation_nombre(n):
    global sequence
    for i in range(4):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)
    return sequence


effacer_ecran()
st.title("Jeu Memoire👋")
#print("Bienvenue dans le jeu du Simon ")
print()
niveau = input("Veuillez choisir un niveau de difficultes de 1 à 3")
sequence = ""
generation_nombre(4)


score = 0
while True:
    print("Votre sequence : ")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    effacer_ecran()
    reponse_util = input("Votre reponse : ")
    if reponse_util == sequence:
        score +=1
        print(f"Votre score : {score}")
    else:
        break

    if niveau == "1":
        n = 1
    elif niveau == "2":
        n = 2
    else:
        n = 3

    generation_nombre(n)
    effacer_ecran()


print("Mauvaise reponse")
print(f"La bonne réponse était : {sequence}")
print(f"Votre score était : {score}")

'''



import streamlit as st
import random
import time

def generation_nombre(n):
    for i in range(n):
        chiffre = random.randint(0, 9)
        st.session_state.sequence += str(chiffre)

# Initialisation des variables de session
if 'niveau' not in st.session_state:
    st.session_state.niveau = None
if 'sequence' not in st.session_state:
    st.session_state.sequence = ""
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_sequence' not in st.session_state:
    st.session_state.show_sequence = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'clear_input' not in st.session_state:
    st.session_state.clear_input = False
if "show_sequence" not in st.session_state:
    st.session_state.show_sequence = False
if "restart" not in st.session_state:
    st.session_state.restart = False

if st.session_state.restart:
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


st.title("Jeu de mémoire - Simon 🧠")

# Choix du niveau de difficulté
if st.session_state.niveau is None:
    niveau = st.selectbox("Choisissez un niveau de difficulté :", ["1", "2", "3"])
    if st.button("Valider le niveau"):
        st.session_state.niveau = int(niveau)
        generation_nombre(4)  # première séquence
        st.session_state.show_sequence = True
        st.rerun()

# Affichage de la séquence à mémoriser
elif st.session_state.show_sequence:
    st.subheader("Mémorisez cette séquence :")
    st.write(f"**{st.session_state.sequence}**")
    time.sleep(3)  # pause pour laisser le temps de lire
    st.session_state.show_sequence = False
    st.rerun()

# Nettoyage du champ de réponse si nécessaire
if st.session_state.clear_input:
    st.session_state.user_input = ''
    st.session_state.clear_input = False

# Champ pour la réponse de l'utilisateur
reponse = st.text_input("Entrez la séquence que vous avez retenue :", key="user_input")

# Soumettre la réponse
if st.button("Valider votre réponse"):
    if reponse == st.session_state.sequence:
        st.session_state.score += 1
        st.success(f"Bravo ! Score actuel : {st.session_state.score}")

        # Préparer le tour suivant
        generation_nombre(st.session_state.niveau)
        st.session_state.clear_input = True
        st.session_state.show_sequence = True
        st.rerun()
    else:
        st.error("Mauvaise réponse 😢")
        st.write(f"La bonne réponse était : **{st.session_state.sequence}**")
        st.write(f"Votre score final est : **{st.session_state.score}**")
        st.write("Rechargez la Page pour une Nouvelle Partie ")