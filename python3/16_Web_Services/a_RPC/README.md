# RPC

## Types of RPCs

1. XML-RPC

    Uses XML to encode its calls and HTTP as a transport mechanism.
2. JSON-RPC

    Uses JSON to encode its calls, allowing for simplicity and ease of use.
3. gRPC

    A high-performance RPC framework that uses Protocol Buffers as its interface definition language, supporting multiple programming languages.

4. SOAP (Simple Object Access Protocol)
    
    A protocol for exchanging structured information in the implementation of web services, using XML as its messaging format.

5. REST (Representational State Transfer)
    
    Although not a traditional RPC, it uses standard HTTP methods to perform operations on resources, often mimicking RPC behavior.

6. Thrift
    
    Developed by Facebook, it combines a software framework with a code generation mechanism for building cross-language services.

7. Apache Avro
    
    A framework for data serialization that can also be used for RPC, particularly in data-intensive applications.

8. MessagePack-RPC
    
    An efficient binary serialization format that can be used for RPC, similar to JSON-RPC but more compact.

9. BERT-RPC
    
    A binary-encoded serialization format that can be used for RPC, often used in Erlang environments.
10. Cap’n Proto
    
    A data interchange format that allows for high-performance RPC and serialization.

11. Protocol Buffers (Protobuf)
    
    Developed by Google, used for serializing structured data, often used with gRPC.

12. RMI (Remote Method Invocation)
    
    A Java-specific protocol for invoking methods on remote objects.

13. CORBA (Common Object Request Broker Architecture)
    
    A standard for software componentry that allows communication between various programming languages.

14. D-Bus
    
    An IPC (Inter-Process Communication) system that allows communication between multiple programs running concurrently.


## XML-RPC vs JSON-RPC

| Feature                | XML-RPC                          | JSON-RPC                           |
|------------------------|----------------------------------|-------------------------------------|
| **Data Format**        | XML                              | JSON                                |
| **Readability**        | Less human-readable              | More human-readable                 |
| **Transport**          | Typically uses HTTP              | Typically uses HTTP                 |
| **Serialization**      | More verbose and complex         | Lightweight and easier to parse     |
| **Method Calling**     | Uses `<methodCall>` and `<methodResponse>` tags | Simple method names with parameters in JSON format |
| **Error Handling**     | Uses `<fault>` element           | Uses an `error` object              |
| **Data Types**         | Limited data types (string, int, boolean, array, struct) | Supports a richer set of data types including arrays and objects |
| **Versioning**         | Typically not versioned          | Can include versioning in JSON-RPC 2.0 |
| **Security**           | Can be more complex due to XML parsing | Simpler due to JSON; relies on underlying transport security |
| **Use Cases**          | Legacy systems, SOAP-like services | Modern web APIs, microservices      |
