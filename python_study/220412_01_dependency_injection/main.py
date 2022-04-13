from containers import Readers, Clients, Configs

if __name__ == "__main__":
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "william.suzuki@myemail.com",
        "password": "mylittlesecret",
        "mailbox": "A mail box?"
    })

    email_reader = Readers.email_reader()

    print(email_reader.read())

