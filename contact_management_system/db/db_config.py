from dotenv import dotenv_values


def load_db_config():
    config = {
        **dotenv_values("contact_management_system/db/env/.env.shared"),
        **dotenv_values("contact_management_system/db/env/.env.secret")
    }
    return config

# print(load_db_config())
# with open("contact_management_system/db/env/.env", 'r') as f:
#     print(f.read())
