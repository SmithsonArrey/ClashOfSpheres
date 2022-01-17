from view import sprites
#taking player intent as an input
#activate switch case


#bloblogic
#when ordered to go to a non adj zone. the blob will add the non adj zones in its move queue and to the adj zone
#i can grab the path to the 
#move orders can not be cancelled
#smaller blobs are faster. larger blobs are slower
#fighting state logic 

#portallogic


#return 




def generate_attack_path(context, target):
    #returns queue of zones
    print("attack path generated")

def create_blob(context, attack_path, team):
    return sprites.blob_sprite(context, attack_path, team)


#context and target are zone objects
def input_response(command, context, target):
    if command == "attack":
        attack_path = generate_attack_path(context,target)
        return create_blob(context, attack_path, "Player")