# Import the Translator function from the translate module
from translate import Translator

# Specify the input and output languages
translator = Translator(from_lang="en",to_lang="zh")
# Do the actual translation
translation = translator.translate("hello all")
print(translation)
# Specify the input and output languages
translator = Translator(from_lang="zh",to_lang="en")
# Do the actual translation
translation = translator.translate("请再说一遍")
print(translation)
