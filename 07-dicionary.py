countries_and_capiotalies = {
    "Poland":"Warsaw",
    "Germany":"Berlin",
    "USA":"Washington DC"
}
# standard using dic
print(countries_and_capiotalies["Germany"])
print()
# we can use function get this allow us form error over of this we will get "country not found"  
print(countries_and_capiotalies.get("Russia", "country not found"))

