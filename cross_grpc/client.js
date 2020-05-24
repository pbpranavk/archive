const grpc = require('grpc')
const PROTO_PATH = './crud.proto'
const NoteService = grpc.load(PROTO_PATH).crud
const client = new NoteService('localhost:50051', grpc.credentials.createInsecure())

client.create({}, (error, res) => {
  if (!error) {
    console.log('successfully fetch List notes')
    console.log(res)
  } else {
    console.error(error)
  }
})
