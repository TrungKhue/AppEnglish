import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Nói một câu:")
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
    print("Tỷ lệ từ bạn nói đúng: ", accuracy, "%")
except sr.UnknownValueError:
    print("Không thể nhận dạng giọng nói.")
except sr.RequestError as e:
    print("Lỗi trong quá trình gửi yêu cầu đến Google: {0}".format(e))
