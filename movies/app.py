import json
import boto3
import requests
from plexapi.server import PlexServer
from plexapi.utils import download
from movie import Movie

plex = PlexServer(baseurl, token)

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # operation = event['httpMethod']

    movies = plex.library.section('Películas')
    movies_u = []
    for video in movies.recentlyAdded(maxresults=6, libtype='movie'):
        m = Movie(video.thumb, video.title)
        movies_u.append(m)
    return {
        "statusCode": 200,
        # "body": moviesU
        "body": json.dumps({
            "movies": [obj.to_dict() for obj in movies_u]
        }),
    }
    # operations = {
    #     'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
    #     'GET': lambda dynamo, x: dynamo.scan(**x),
    #     'POST': lambda dynamo, x: dynamo.put_item(**x),
    #     'PUT': lambda dynamo, x: dynamo.update_item(**x),
    # }

    # print(operation)
    # if operation in operations:
    #     payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    #     return respond(None, operations[operation](dynamo, payload))
    # else:
    #     return respond(ValueError('Unsupported method "{}"'.format(operation)))
