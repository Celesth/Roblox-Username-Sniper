import random
import string

def generate_username(min_length=4, max_length=6):
    length = random.randint(min_length, max_length)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def save_usernames(count=1000, filename="usernames.txt", min_length=6, max_length=6):
    with open(filename, "w") as file:
        file.writelines(f"{generate_username(min_length, max_length)}\n" for _ in range(count))
    print(f"Generated {count} usernames saved to {filename}")

if __name__ == "__main__":
    save_usernames()
    