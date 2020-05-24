# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import crud_pb2 as crud__pb2


class crudStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create = channel.unary_unary(
        '/crud/create',
        request_serializer=crud__pb2.Message.SerializeToString,
        response_deserializer=crud__pb2.Message.FromString,
        )
    self.retrieve = channel.unary_unary(
        '/crud/retrieve',
        request_serializer=crud__pb2.Message.SerializeToString,
        response_deserializer=crud__pb2.Message.FromString,
        )
    self.update = channel.unary_unary(
        '/crud/update',
        request_serializer=crud__pb2.Message.SerializeToString,
        response_deserializer=crud__pb2.Message.FromString,
        )
    self.delete = channel.unary_unary(
        '/crud/delete',
        request_serializer=crud__pb2.Message.SerializeToString,
        response_deserializer=crud__pb2.Message.FromString,
        )


class crudServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def retrieve(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_crudServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create': grpc.unary_unary_rpc_method_handler(
          servicer.create,
          request_deserializer=crud__pb2.Message.FromString,
          response_serializer=crud__pb2.Message.SerializeToString,
      ),
      'retrieve': grpc.unary_unary_rpc_method_handler(
          servicer.retrieve,
          request_deserializer=crud__pb2.Message.FromString,
          response_serializer=crud__pb2.Message.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=crud__pb2.Message.FromString,
          response_serializer=crud__pb2.Message.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=crud__pb2.Message.FromString,
          response_serializer=crud__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'crud', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
