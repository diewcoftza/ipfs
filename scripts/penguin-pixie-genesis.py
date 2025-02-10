from pprint import pprint as pp
import json

NAME = "Penguin Pixie Genesis"
DESC = "A tiny girl with blue eyes and her penguin pals, waking up to the soft morning glow in the polar frost."
FROM_ID = 0
SUPPLY = 888
IMG_IPFS = "https://diewcoftza.github.io/ipfs/penguin-pixie-genesis/asset.png"
VID_IPFS = "https://diewcoftza.github.io/ipfs/penguin-pixie-genesis/asset.mp4"
OUTPUT_PATH = "../docs/penguin-pixie-genesis/json/{}"

for i in range(0, SUPPLY):
    token_id = i + FROM_ID
    dest = OUTPUT_PATH.format(token_id)

    # craft data
    data = {
        "name": "{} #{}".format(NAME, token_id),
        "description": DESC,
        "image": IMG_IPFS,
        "animation_url": VID_IPFS,
        #"attributes": [
        #    {
        #        "trait_type": "Rarity",
        #        "value": "Common",
        #    },
        #],
    }

    # write file
    print(dest)
    #pp(data)
    with open(dest, "w") as f:
        json.dump(data, f)
