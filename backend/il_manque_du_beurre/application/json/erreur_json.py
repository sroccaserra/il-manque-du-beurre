import json


def serialise_erreur(description):
    return json.dumps({
        'erreur': {
            'description': description
        }
    })
