import grpc
from concurrent import futures
import time

from crud_pb2 import Message
from crud_pb2_grpc import crudServicer, add_crudServicer_to_server

class CrudService(crudServicer):
    def create(self, request, context):
        print("Invoked")
        return Message()

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

add_crudServicer_to_server(CrudService(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)