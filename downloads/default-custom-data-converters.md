# Default and Custom Data Converters

> For the complete documentation index, see [llms.txt](https://docs.temporal.io/llms.txt).
> Any documentation page is available as raw Markdown by appending `.md` to its URL.

> Learn about the default Data Converter in Temporal SDKs and how to implement a custom Data Converter for custom serialization and encoding needs.

This page discusses the following:

- [Default Data Converter](#default-data-converter)
- [Custom Data Converter](#custom-data-converter)

## What is a default Data Converter? 

Each Temporal SDK includes and uses a default Data Converter.
The default Data Converter converts objects to bytes using a series of Payload Converters and supports binary, Protobufs, and JSON formats.
It encodes values in the following order:

- Null
- Byte array
- Protobuf JSON
- JSON

In SDKs that cannot determine parameter types at runtime (for example, TypeScript), Protobufs aren't included in the default converter.

For example:

- If a value is an instance of a Protobuf message, it is encoded with [proto3 JSON](https://developers.google.com/protocol-buffers/docs/proto3#json).
- If a value isn't null, binary, or a Protobuf, it is encoded as JSON. Most common input types — including strings, integers, floating point numbers, and booleans — are serializable as JSON. If any part of it is not serializable as JSON,  an error is thrown.

The default Data Converter serializes objects based on their root type, rather than nested types.
The JSON serializers of some SDKs cannot process lists with Protobuf children objects without implementing a [custom Data Converter](#custom-data-converter).

## What is a custom Data Converter? 

A custom Data Converter extends the default Data Converter with custom logic for [Payload](/dataconversion#payload) conversion or encoding.

You can create a custom Data Converter to alter formats (for example, using [MessagePack](https://msgpack.org/) instead of JSON) or add compression and encryption.

A Payload Codec encodes and decodes [Payloads](/dataconversion#payload), with bytes-to-bytes conversion.
To use custom encryption or compression logic, create a custom Payload Codec with your encryption/compression logic in the `encode` function and your decryption/decompression logic in the `decode` function.
To implement a custom Payload Codec, you can override the default Data Converter, or create a customized Data Converter that defines its own Payload Converter.

Custom Data Converters are not applied to all data; for example, [Search Attributes](/search-attribute) are persisted unencoded so they can be indexed for searching.

A customized Data Converter can have the following three components:

- [Payload Converter](/payload-converter)
- [Payload Codec](/payload-codec)
- [Failure Converter](/failure-converter)

For details on how to implement custom encryption and compression in your SDK, see [Data Encryption](/production-deployment/data-encryption).
