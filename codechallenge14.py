anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")

    if anime.lower() == 'exit':
        break

    anime_list.append(anime)
    print(f"'{anime}' has been added to your anime list.")

print("You have exited the anime entry program.")
print("Your anime list includes:")
for alist in anime_list:
    print("-", alist)
  

   
