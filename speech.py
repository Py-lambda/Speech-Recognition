import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source: 
	print("Speak Anything: ")
	audio = r.listen(source)

	try:
		test=r.recognise_google(audio)
		print("You said : {}".format(text))
	except:
		print("Sorry could not recognise your voice")
		

