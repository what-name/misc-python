# Load API Key from APIKey file
apiKeyFile = open("APIKey")
apiKey = apiKeyFile.read()

# Ask for city's name
print("Which city do you want the weather for?")
city = input()
# FIXME validate that input is a string

def getWeather(city):
	# FIXME make API call
	print("Nice and shiny weather we have today in", city)

getWeather(city)