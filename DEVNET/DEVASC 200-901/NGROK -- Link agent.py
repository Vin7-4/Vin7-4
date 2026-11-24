############################################################################################


########   (py)FUNCTION DI CONNESSIONE NGROK

# (BASH)
# crea file
# $ nano [file]
# edtita con la def sotto


############################################################################################


import ngrok

def connect_ngrok():
    forwarder = ngrok.forward("localhost:8085", authtoken_from_env=True,
                              NGROK_AUTHTOKEN='3MYLh7PcrUuxvF4APiRFgHTJaer_7fEpuMRFu8t2x5HnnyKbq' , domain="spearmint-violator-excluding.ngrok-free.dev")
    print(f"Available at: {forwarder.url()}")

connect_ngrok()



#  (esecuzione da pycharm) output login error :

# ValueError: ('failed to connect session', 'This ngrok session is not authenticated. ngrok requires an account and a valid credential to start a session.
# \nSign up for an account: https://dashboard.ngrok.com/signup\nGet your credential: https://dashboard.ngrok.com/get-started/your-authtoken', 'ERR_NGROK_4018')