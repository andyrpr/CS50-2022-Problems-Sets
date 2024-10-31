
def main():
    text = input("Write something: ")
    text = convert(text)
    print(text)
    
    
def convert(x):
    if ":)" in x:
        x = x.replace(":)", "😁")
        return x
    elif  ":(" in x:
        x = x.replace(":(", "🫤")
        return x
    else:
        return x

        
        
main()
