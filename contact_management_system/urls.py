# Domain
import pprint

PROTOCOL = "http://"
DOMAIN = "localhost:8000"


# Root PATH
CONTACT_PATH = "/contact"
USER_PATH = "/user"

# Sub PATH
ADD_CONTACT_PATH = CONTACT_PATH + "/add"
DELETE_CONTACT_PATH = CONTACT_PATH + "/delete"

# URLs
FETCH_CONTACTS_URL = PROTOCOL + DOMAIN + CONTACT_PATH
ADD_CONTACT_URL = PROTOCOL + DOMAIN + ADD_CONTACT_PATH
DELETE_CONTACT_URL = PROTOCOL + DOMAIN + DELETE_CONTACT_PATH


# u = {'Date': 'Mon, 06 May 2024 13:32:32 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 'Content-Type': 'text/html; charset=ISO-8859-1', 'Content-Secu rity-Policy-Report-Only': "object-src 'none';base-uri 'self';script-src 'nonce-LTKZBjIplxsrZggI8ZXCIA' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-in line' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp", 'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 'Content-En coding': 'gzip', 'Server': 'gws', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': 'AEC=AQTF6Hx2zYiE-wssxzedHuwHvjzAmUL-1688g0lOGgFyk9iJd CAlGTzClc4; expires=Sat, 02-Nov-2024 13:32:32 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax, NID=514=UtVPo_07AfPbGh8QvYNPTfCoM5Q2y0BVMAoMvG3j- ZL_udyY8PsQprIru9uyzSoep-E_KgwFKR3Fh5YsTHoNAkBtggWsedNNIuHjKvtSfUVYCbdWAi8fi617TbsQR-dJEnNUul42TDh4MW9ZfYtmm3rF4xxxOW5tGuvQH1TVM28; expires=Tue, 05-Nov-2024 13:32:32 GMT; path=/; domain=.google.com; HttpOnly', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000', 'Transfer-Encoding': 'chunked'}
# pprint.pprint(u)