import replicate
# from translate import Translator

client = replicate.Client(api_token="r8_EaenLto4e2ki7lKyHZLH21DqkMSDjmc3SVTnr")

input1 = {
    "image": "https://images.unsplash.com/photo-1455305049585-41b8d277d68a?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "prompt": "describe the picture in detail"
}

output1 = client.run(
    "yorickvp/llava-13b:b5f6212d032508382d61ff00469ddda3e32fd8a0e75dc39d8a4191bb742157fb",
    input=input1
)
# print("lang_code language \n en English(India) \n gu-IN Gujarati(India) \n hi-IN Hindi(India) \n kn-IN Kannada(India) \n kok-IN Konkani(India) \n mr-IN Marathi(India) \n pa-IN Punjabi(Indiak) \n sa-IN Sanskrit(India) \n ta-IN Tamil(India) \n te-IN Telugu(India)")

# convert_lang="hi"

# input("\nENTER THE LANGUAGE YOU WANT TO CONVERT INTO (ENTER THE LANG_CODE) :")

output="".join(output1)
#
# translator=Translator(from_lang = "en",to_lang=convert_lang)
# translation=translator.translate(output)
#
# data="".join(translation)
