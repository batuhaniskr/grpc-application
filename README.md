# gRPC-applications

Sample gRPC Java And Python client - server application and gRPC authentication application
 
## gRPC Sample Application

gRPC Sample application based client-server model of remote procedure call.

hotelService.proto

<pre>
syntax = "proto3";
option java_multiple_files = true;
package com.example.demo;

message HotelRequest {
    int32 id = 1;
    string hotelName = 2;
}

message HotelResponse {
    string hotelText = 1;
}

service HotelService {
    rpc getHotel(HotelRequest) returns (HotelResponse);
}
</pre>

If you will do project, you can use command:

<pre>protoc -I=$SRC_DIR --java_out=$DST_DIR $SRC_DIR/HelloService.proto</pre>

or you can using maven plugin. </br>
Created HotelService.java for implementation all operations.
</br>
Now, You need to start the GrpcServer.java. Server runs on port 8080.
</br>
Client.java runs for the consuming service.

## gRPC Client with Python

### Prerequisites
<pre>cd grpc-sample-applications/grpc-python-client/</pre>
<pre>pip install -r requirements.txt</pre>

<pre>python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hotelService.proto</pre>

<li>hotelService_pb2.py contains message classes. <li>

<li>hotelService_pb2_grpc.py contains server and client classes. </li>

<li>Added client.py for consume the service</li>

<pre>$ python client.py<br> hotelText: "Hotel, id: 1  name: testHotel"</pre>

