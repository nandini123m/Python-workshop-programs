def extract_email_components(email):
    parts=email.split("@")

    if len(parts) == 2:
        username = parts[0]
        service_provider, domain = parts[1].split(".")
        return username, service_provider, domain
    else:
        return None
email=input("Enter an email  address:")

components=extract_email_components(email)

if components:
    username,service_provider,domain=components
    print("Username:",username)
    print("Service Provider:",service_provider)
    print("Domain:",domain)
else:
    print("Invalid email address format")
