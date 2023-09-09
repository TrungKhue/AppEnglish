import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say a word:")
    audio = recognizer.listen(source)
try:
    spoken_text = recognizer.recognize_google(audio)
    print("You say: " + spoken_text)
    spoken_words = spoken_text.split()
    target_sentence = "I'm learning to play the guitar"
    target_words = target_sentence.split()
    total_words = len(target_words)
    correct_words = sum(1 for word in spoken_words if word in target_words)
    accuracy = (correct_words / total_words) * 100
    print("The percentage of words you say right: ", accuracy, "%")
except sr.UnknownValueError:
    print("Can't recognize voice.")
except sr.RequestError as e:
    print("Error submitting request to Google: {0}".format(e))
